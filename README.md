<p align="center">
  <img src="public/screenshot.png" alt="Gitvana — 원작 스크린샷" width="100%" />
</p>

<h1 align="center">Gitvana (한국어판)</h1>

<p align="center">
  <code>⚠️ ALPHA — 원작이 알파 단계입니다. 버그와 거친 부분, 가끔 화난 수도승이 있을 수 있습니다. ⚠️</code>
</p>

<p align="center">
  <strong>놀이로 배우는 git.</strong> 실제 터미널에 실제 git 명령어를 입력해 버전 관리 수도원의 퍼즐을 푸는 레트로 브라우저 게임입니다.
</p>

<p align="center">
  🎮 <a href="https://sigco3111.github.io/gitvana-ko/"><strong>지금 플레이 — sigco3111.github.io/gitvana-ko</strong></a>
</p>

---

## 이 저장소는 무엇인가요?

이 저장소는 [pixari/gitvana](https://github.com/pixari/gitvana) (MIT 라이선스)의 **한국어 번역판**입니다. 원작의 게임 코드를 바탕으로 한국어 로케일(`src/i18n/ko/`)을 추가하고, 기본 언어를 한국어로 설정했습니다. 원작은 영어, 스페인어, 프랑스어, 브라질 포르투갈어를 지원합니다. 언어는 게임 안에서 언제든 바꿀 수 있습니다.

- 원작 저장소: https://github.com/pixari/gitvana
- 원작자: [Raffaele Pizzari](https://pixari.dev) ([@pixari](https://github.com/pixari))
- 이 한국어판은 원작자의 공식 판이 아닙니다. 번역과 배포 설정은 sigco3111이 맡았습니다.

## 게임 소개

Gitvana는 38개의 점점 어려워지는 레벨을 통해 git을 가르치는 브라우저 게임입니다. 슬라이드나 영상 없이, 실제 git 명령어를 입력하고 결과를 실시간으로 확인합니다. 당신은 깨달음을 향해 산을 오르는 수도승이 됩니다. 수석 수도승이 임무를 내리고, 고양이가 당신의 커밋을 심사합니다.

**실제 git, 브라우저 안에서**
- isomorphic-git + lightning-fs 기반의 완전한 git 엔진이 클라이언트에서 실행됩니다.
- `git add`, `git rebase`, `git bisect` 등 입력한 명령어가 실제로 실행됩니다.
- 원작 기준 git 명령어 21종 구현 (init, add, commit, status, log, diff, branch, checkout, merge, reset, rm, tag, cherry-pick, show, revert, stash, reflog, rebase, blame, bisect, update-ref).

**6막 38개 레벨**
- 1막: 각성 — 기초
- 2막: 중도 — tag, cherry-pick, revert, stash
- 3막: 현실 다시 쓰기 — rebase, amend, squash, 비밀 제거
- 4막: 안전망 — reflog, blame, bisect, 복구
- 5막: 고급 기법 — 정밀 스테이징, 의존 체인
- 6막: Gitvana — 최후의 시련

**배우기 위한 도구**
- 실시간 파일 상태 패널 (작업 디렉터리 / 스테이징 / 저장소)
- 커밋 그래프 시각화
- 개념 가이드와 명령어 참조가 들어 있는 내장 문서
- 탭 완성, 명령어 기록, 충돌 편집기

**설치 불필요**
- 브라우저에서 모두 실행됩니다. 백엔드, 데이터베이스, 회원가입이 없습니다.
- 오프라인에서도 동작합니다 (PWA).
- 진행 상황은 브라우저의 localStorage에 저장됩니다.

## 번역 범위

| 항목 | 상태 |
| --- | --- |
| `src/i18n/ko/ui.json` (화면 문구, 랜딩 페이지) | 번역 완료 |
| `src/i18n/ko/stages.json` (20단계 이름과 설명) | 번역 완료 |
| `src/i18n/ko/hints.json` (힌트와 오류 안내) | 번역 완료 |
| 레벨 내용 `levels.json` (스토리, 목표, 힌트) | **미번역 — 영문 원문 표시** |
| 문서 `docs-commands.json`, `docs-guides.json` | **미번역 — 영문 원문 표시** |

명령어 자체(`git commit`, `edit <file>` 등)는 번역하지 않았습니다. 설명 문구만 번역했습니다.

## 한국어판에서 바꾼 점

- 기본 언어를 한국어로 설정했습니다. 저장된 언어 선택이 있으면 그 언어를 따릅니다.
- 한국어 글자를 위해 Noto Sans KR 글꼴을 추가했습니다 (원작 픽셀 글꼴 Press Start 2P에는 한글 글리프가 없습니다).
- 원작의 방문 통계 스크립트(외부 분석 서버)를 제거했습니다. 게임 플레이 이벤트를 외부 서버로 보내는 텔레메트리 코드도 비활성화했습니다.
- 페이지 메타 정보와 canonical 주소를 이 저장소의 배포 주소로 바꾸고, 원작 출처를 명시했습니다.
- 빌드 시 `/gitvana-ko/` 경로를 쓰도록 설정했습니다 (GitHub Pages 프로젝트 사이트용).
- 원작의 `/api` 서버(통계 페이지 데이터 등)는 이 정적 배포에 없으므로, 통계 화면은 데이터가 비어 보일 수 있습니다.

## 로컬에서 실행하기

```bash
git clone https://github.com/sigco3111/gitvana-ko.git
cd gitvana-ko
bun install
bun run dev
```

브라우저에서 [http://localhost:5173](http://localhost:5173)을 여세요.

테스트:

```bash
bun test
```

## 프로젝트 구조

```
src/
├── components/   # Svelte UI 컴포넌트 (terminal, graph, level, docs, landing ...)
├── i18n/         # 언어 파일: en/, es/, fr/, pt-BR/, ko/ (ko는 이 번역판에서 추가)
├── lib/          # 게임 엔진 (git 엔진, 셸, 레벨 로더, 오디오)
├── levels/       # 38개 레벨 JSON
├── docs/         # 명령어 문서와 개념 가이드
└── main.ts       # 진입점
```

## 크레딧

- **원작 Gitvana**: [Raffaele Pizzari](https://pixari.dev) ([@pixari](https://github.com/pixari)) — 원작 저장소 https://github.com/pixari/gitvana
- 픽셀 아트: 원작에서 [PixelLab](https://pixellab.ai)으로 생성
- 한국어 번역 및 배포: sigco3111
- 사용한 기술: [Svelte 5](https://svelte.dev), [isomorphic-git](https://isomorphic-git.org), [lightning-fs](https://github.com/isomorphic-git/lightning-fs), [xterm.js](https://xtermjs.org), [Vite](https://vitejs.dev), [UnoCSS](https://unocss.dev), Web Audio API
- 원작이 도움이 되었다면 원작자에게 [커피 한 잔](https://buymeacoffee.com/pixari) ☕ 을 보내 주세요.

## 라이선스

MIT. 원본 라이선스 전문은 [LICENSE](LICENSE) 파일에 그대로 있습니다. 저작권은 원작자 Raffaele Pizzari에게 있으며, 한국어 번역 부분도 같은 MIT 조건으로 배포합니다.
