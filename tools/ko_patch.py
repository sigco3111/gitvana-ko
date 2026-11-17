#!/usr/bin/env python3
"""gitvana-ko 한글화 패치 러너 (tools/patches/*.json 을 파일명 순서로 적용).

연산 형식 (파일 하나는 연산 목록):
  {"file": 경로, "type": "text", "old": 원문, "new": 번역}
      old 가 파일에 있으면 new 로 치환. 없고 new 가 이미 있으면 적용 완료로 건너뜀.
      둘 다 없으면 실패.
  {"file": 경로, "type": "json", "path": "a.b.0.c", "expect": 원문 앞부분, "set": 번역}
      JSON 값의 점(.) 경로(숫자는 배열 인덱스)를 찾아, 현재 값이 expect 로 시작하면 set 으로 교체.
      값이 이미 set 과 같으면 건너뜀. 그 밖이면 실패. 결과는 json.dumps 로 다시 쓴다(유효성 보장).

실패가 하나라도 있으면 어떤 파일도 쓰지 않고 exit 1. 끝에 src/ 와 index.html 에
'/sprites/' 절대경로가 남았는지 검사한다.
"""
import json
import pathlib
import re
import sys
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATCH_DIR = ROOT / "tools" / "patches"
SPRITE_ABS = re.compile(r"""["'`(]/sprites/""")
SCAN_SUFFIXES = {".svelte", ".ts", ".js", ".html"}


def get_node(obj, parts):
    for p in parts[:-1]:
        obj = obj[int(p)] if isinstance(obj, list) else obj[p]
    last = parts[-1]
    return obj, (int(last) if isinstance(obj, list) else last)


def apply_json(data, op, label, errors):
    try:
        parent, key = get_node(data, op["path"].split("."))
        cur = parent[key]
    except (KeyError, IndexError, ValueError, TypeError):
        errors.append(f"{label}: 경로 없음 {op['path']}")
        return
    if not isinstance(cur, str):
        errors.append(f"{label}: 문자열이 아님 {op['path']}")
        return
    if cur == op["set"]:
        return
    if not cur.startswith(op["expect"]):
        errors.append(f"{label}: 원문 불일치 {op['path']}: {cur[:60]!r}")
        return
    parent[key] = op["set"]


def apply_text(text, op, label, errors):
    old, new = op["old"], op["new"]
    if text.count(old) > 0:
        return text.replace(old, new)
    if new and text.count(new) > 0:
        return text
    errors.append(f"{label}: 원문 없음 {old[:80]!r}")
    return text


def main():
    errors = []
    files = OrderedDict()  # 경로 -> [내용 또는 JSON 객체]
    ops = []
    for pf in sorted(PATCH_DIR.glob("*.json")):
        for op in json.loads(pf.read_text(encoding="utf-8")):
            ops.append((pf.name, op))

    for pf_name, op in ops:
        rel = op["file"]
        label = f"{pf_name} [{rel}]"
        if rel not in files:
            p = ROOT / rel
            if not p.is_file():
                errors.append(f"{label}: 파일 없음")
                continue
            raw = p.read_text(encoding="utf-8")
            files[rel] = json.loads(raw) if op["type"] == "json" else raw
        if op["type"] == "json":
            apply_json(files[rel], op, label, errors)
        else:
            files[rel] = apply_text(files[rel], op, label, errors)

    if errors:
        print("FAILED: 원문 불일치/없음")
        for e in errors:
            print("  - " + e)
        return 1

    new_texts = {}
    for rel, val in files.items():
        if isinstance(val, str):
            new_texts[rel] = val
        else:
            new_texts[rel] = json.dumps(val, ensure_ascii=False, indent=2) + "\n"

    scan = [ROOT / "index.html"] + [f for f in (ROOT / "src").rglob("*") if f.suffix in SCAN_SUFFIXES]
    leftovers = []
    for f in scan:
        rel = str(f.relative_to(ROOT))
        body = new_texts.get(rel)
        if body is None:
            body = f.read_text(encoding="utf-8")
        for m in SPRITE_ABS.finditer(body):
            leftovers.append(f"{rel}:{body.count(chr(10), 0, m.start()) + 1}")
    if leftovers:
        print("FAILED: '/sprites/' 절대경로가 남아 있음")
        for x in leftovers:
            print("  - " + x)
        return 1

    changed = 0
    for rel, body in new_texts.items():
        p = ROOT / rel
        if p.read_text(encoding="utf-8") != body:
            p.write_text(body, encoding="utf-8")
            print("patched: " + rel)
            changed += 1
    print(f"OK: 연산 {len(ops)}개 처리, 변경 파일 {changed}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
