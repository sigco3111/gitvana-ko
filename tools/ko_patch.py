#!/usr/bin/env python3
"""gitvana-ko 한글화 보완 패치 러너.

PATCHES: {파일 경로: [(바꿀 원문, 바꿀 문자열), ...]}. 각 원문은 파일에 반드시 있어야 하며
(str.replace), 하나라도 없으면 실패로 기록하고 어떤 파일도 쓰지 않는다(exit 1).
끝에 src/ 와 index.html 에 '/sprites/' 절대경로가 남았는지 검사한다.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

PATCHES = {
    # ① 이미지 경로: BASE_URL 기준 (base /gitvana-ko/ 에서 404 방지)
    "src/components/progression/MountainPath.svelte": [
        ("'/sprites/monk-tier4.png'", "import.meta.env.BASE_URL + 'sprites/monk-tier4.png'"),
        ("'/sprites/monk-tier3.png'", "import.meta.env.BASE_URL + 'sprites/monk-tier3.png'"),
        ("'/sprites/monk-tier2.png'", "import.meta.env.BASE_URL + 'sprites/monk-tier2.png'"),
        ("'/sprites/monk-tier1.png'", "import.meta.env.BASE_URL + 'sprites/monk-tier1.png'"),
        ('src="/sprites/{levelId}.png"', 'src="{import.meta.env.BASE_URL}sprites/{levelId}.png"'),
    ],
    # ② 레벨 수 정정 (실제 레벨은 src/levels/act0~act6 의 01~38)
    "index.html": [
        ("35 levels from init to mastery", "38 levels from init to mastery"),
    ],
    "README.md": [
        ("35개의 점점 어려워지는 레벨", "38개의 점점 어려워지는 레벨"),
        ("**6막 35개 레벨**", "**6막 38개 레벨**"),
    ],
}

SPRITE_ABS = re.compile(r"""["'`(]/sprites/""")
SCAN_SUFFIXES = {".svelte", ".ts", ".js", ".html"}


def main():
    errors = []
    new_texts = {}
    for path, pairs in PATCHES.items():
        p = ROOT / path
        if not p.is_file():
            errors.append(f"파일 없음: {path}")
            continue
        text = p.read_text(encoding="utf-8")
        for old, new in pairs:
            if text.count(old) == 0:
                errors.append(f"원문 없음 [{path}]: {old[:100]!r}")
                continue
            text = text.replace(old, new)
        new_texts[path] = text
    if errors:
        print("FAILED: 원문 불일치 항목")
        for e in errors:
            print("  - " + e)
        return 1

    scan = [ROOT / "index.html"] + [f for f in (ROOT / "src").rglob("*") if f.suffix in SCAN_SUFFIXES]
    leftovers = []
    for f in scan:
        rel = str(f.relative_to(ROOT))
        body = new_texts.get(rel)
        if body is None:
            body = f.read_text(encoding="utf-8")
        for m in SPRITE_ABS.finditer(body):
            line = body.count("\n", 0, m.start()) + 1
            leftovers.append(f"{rel}:{line}")
    if leftovers:
        print("FAILED: '/sprites/' 절대경로가 남아 있음")
        for x in leftovers:
            print("  - " + x)
        return 1

    for path, text in new_texts.items():
        (ROOT / path).write_text(text, encoding="utf-8")
        print("patched: " + path)
    print(f"OK: {sum(len(v) for v in PATCHES.values())} 항목 적용")
    return 0


if __name__ == "__main__":
    sys.exit(main())
