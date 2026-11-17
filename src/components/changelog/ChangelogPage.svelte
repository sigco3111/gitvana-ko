<script lang="ts">
  import Navbar from '../shared/Navbar.svelte';

  const tagColors: Record<string, string> = {
    release: '#ffa300',
    engine: '#29adff',
    content: '#00e436',
    feature: '#ff77a8',
    docs: '#83769c',
    milestone: '#ffd700',
    fix: '#ff004d',
  };

  const entries = [
    {
      date: '2026-04-10',
      title: '터미널의 길 — 셸 기초 튜토리얼',
      tags: ['feature', 'content'],
      content: 'git 레벨 전에 터미널 기초(echo, cat, touch, grep, 체이닝)를 가르치는 강의 3개로 구성된 선택 사항 0막이 추가되었습니다. 새 플레이어는 처음 방문할 때 "기초 배우기" 또는 "Git으로 건너뛰기"를 고를 수 있습니다. 기존 진행 상황은 자동으로 옮겨집니다 (#33).'
    },
    {
      date: '2026-04-10',
      title: 'UX 개선 및 버그 수정',
      tags: ['fix', 'feature'],
      content: '보이지 않던 터미널 입력을 수정했습니다. 입력한 글자는 처리되었지만 화면에 표시되지 않았습니다 (#37, #39). 인자 없이 "git"만 입력하면 "command not found" 대신 사용법을 보여 줍니다 (#38). 레벨 완료 카드를 최소화할 수 있어, 계속하기 전에 터미널 단계를 다시 확인할 수 있습니다 (#30). 초반 레벨에서 신규 플레이어에게 상황별 힌트가 나타납니다 (#25). 하드코딩된 레벨 수를 동적 상수 TOTAL_LEVELS로 바꿨습니다 (#42).'
    },
    {
      date: '2026-04-06',
      title: '다국어(i18n) 인프라',
      tags: ['feature'],
      content: '다국어 지원이 시작되었습니다. UI 문자열을 JSON 로케일 파일로 번역할 수 있습니다. 로케일이 2개 이상이면 언어 선택기가 나타납니다. 영어가 기준 원문입니다. 커뮤니티 번역을 환영합니다 — CONTRIBUTING_TRANSLATIONS.md를 참고하세요.'
    },
    {
      date: '2026-04-06',
      title: '버그 수정 — 터미널, diff, 레벨',
      tags: ['fix'],
      content: '수정: 연결된 nano/edit 명령 (#36), 커밋 참조가 있는 git diff (#29), 4레벨 별 기준 (#31), Ctrl+L 화면 지우기 (#24), 긴 입력 줄 줄바꿈 (#34), 되돌리기 후 저장소 상태 동기화 (#27). man 명령 (#32)과 색상 구분된 git log (#35)를 추가했습니다.'
    },
    {
      date: '2026-04-06',
      title: '태블릿 지원',
      tags: ['feature'],
      content: 'Gitvana가 가로 방향 태블릿에서 동작합니다. 좁은 화면에서는 패널이 세로로 쌓입니다. 이제 모바일 대체 화면은 휴대폰 크기 화면에서만 나타납니다.'
    },
    {
      date: '2026-04-04',
      title: '버그 수정 — rebase, diff, commit',
      tags: ['fix', 'engine'],
      content: 'rebase 충돌 처리가 충돌 표시 대신 JavaScript 오류로 멈추던 문제를 수정했습니다 (#23). git diff가 바뀐 줄 대신 파일 전체를 추가된 것으로 보여 주던 문제를 수정했습니다 (#22). pathspec을 쓰는 git commit (예: git commit . -m "msg")은 이제 커밋 전에 파일을 자동으로 스테이징합니다.'
    },
    {
      date: '2026-04-03',
      title: '시뮬레이션 원격 저장소 — push, fetch, pull',
      tags: ['feature', 'engine'],
      content: 'git push, fetch, pull이 브라우저 안에서 실행되는 시뮬레이션 원격 저장소로 동작합니다. 원격 협업을 가르치는 새 레벨 3개가 추가되었습니다. 커밋 그래프에 원격 추적 브랜치가 보입니다. 개발 블로그 페이지가 추가되었습니다.'
    },
    {
      date: '2026-04-02',
      title: 'v1.0 — 그랜드 오프닝',
      tags: ['release'],
      content: 'Gitvana가 6막에 걸친 35개 레벨, 21개 git 명령, 픽셀 아트, 칩튠 사운드, 그리고 의심스러운 선택으로 가득한 수도원과 함께 출시되었습니다. 고양이가 흡족해합니다.'
    },
    {
      date: '2026-04-02',
      title: '제대로 된 3-way 병합 엔진',
      tags: ['engine'],
      content: '파일 단위 충돌 감지를 줄 단위 diff3 병합으로 바꿨습니다. 같은 파일의 서로 다른 부분을 고친 변경은 이제 올바르게 자동 병합됩니다. merge, cherry-pick, rebase, revert 모두 이 혜택을 받습니다.'
    },
    {
      date: '2026-04-01',
      title: '레벨 난이도 재설계',
      tags: ['content'],
      content: '15~35 레벨을 실제로 도전적이도록 다시 썼습니다. 후반 레벨은 행동하기 전에 조사(blame, bisect, reflog)가 필요합니다. 보스 레벨에는 연쇄적인 문제가 있습니다. 35 레벨에는 힌트가 하나도 없습니다.'
    },
    {
      date: '2026-04-01',
      title: '새로운 git 명령 9개',
      tags: ['feature'],
      content: 'tag, cherry-pick, show, revert, stash, reflog, rebase, blame, bisect를 추가했습니다. 이제 수도원은 기초뿐 아니라 진짜 git 숙달을 가르칩니다.'
    },
    {
      date: '2026-04-01',
      title: '개념 가이드',
      tags: ['docs'],
      content: 'git이 실제로 어떻게 동작하는지 설명하는 9개의 심층 가이드: 내용 주소 지정 파일 시스템, 세 영역, merge와 rebase 비교, reflog 안전망 등. 게임 안과 /docs에서 볼 수 있습니다.'
    },
    {
      date: '2026-03-31',
      title: '수도원의 문이 열리다',
      tags: ['milestone'],
      content: '6개 레벨, 터미널, 그리고 엄격한 고양이가 있는 첫 플레이 가능 버전. 수석 수도승은 회의적이지만 기회를 한 번 줄 생각이 있습니다.'
    },
  ];

  function getBorderColor(tags: string[]): string {
    return tagColors[tags[0]] ?? '#5f574f';
  }
</script>

<div class="changelog-page">
  <Navbar currentPage="changelog" />

  <div class="changelog-content">
    <header class="changelog-header">
      <h1 class="changelog-title">CHANGELOG</h1>
      <p class="changelog-subtitle">수도원의 개발 기록</p>
    </header>

    <div class="entries">
      {#each entries as entry}
        <article class="entry" style="border-left-color: {getBorderColor(entry.tags)}">
          <div class="entry-meta">
            <span class="entry-date">{entry.date}</span>
            <div class="entry-tags">
              {#each entry.tags as tag}
                <span class="tag" style="background: {tagColors[tag] ?? '#5f574f'}22; color: {tagColors[tag] ?? '#5f574f'}; border-color: {tagColors[tag] ?? '#5f574f'}44">{tag}</span>
              {/each}
            </div>
          </div>
          <h2 class="entry-title">{entry.title}</h2>
          <p class="entry-content">{entry.content}</p>
        </article>
      {/each}
    </div>

    <!-- TODO: Add pagination when there are more entries -->

    <footer class="changelog-footer">
      <p>&copy; 2026 Raffaele Pizzari</p>
    </footer>
  </div>
</div>

<style>
  .changelog-page {
    position: fixed;
    inset: 0;
    background: #0a0a0a;
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 200;
    color: #c2c3c7;
    font-family: 'JetBrains Mono', monospace;
  }

  .changelog-content {
    max-width: 700px;
    margin: 0 auto;
    padding: 44px 24px 60px;
  }

  .changelog-header {
    text-align: center;
    padding: 60px 0 48px;
  }

  .changelog-title {
    font-family: 'Press Start 2P', monospace;
    font-size: clamp(16px, 4vw, 28px);
    color: #ffa300;
    margin: 0 0 16px;
    letter-spacing: 4px;
    text-shadow: 0 0 20px #ffa30044;
  }

  .changelog-subtitle {
    font-size: 13px;
    color: #5f574f;
    margin: 0;
  }

  .entries {
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  .entry {
    border-left: 3px solid #5f574f;
    padding: 16px 0 16px 20px;
  }

  .entry-meta {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
  }

  .entry-date {
    font-size: 11px;
    color: #5f574f;
    letter-spacing: 0.5px;
  }

  .entry-tags {
    display: flex;
    gap: 6px;
  }

  .tag {
    font-size: 9px;
    font-family: 'Press Start 2P', monospace;
    padding: 3px 8px;
    border-radius: 3px;
    border: 1px solid;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }

  .entry-title {
    font-family: 'Press Start 2P', monospace;
    font-size: 12px;
    color: #c2c3c7;
    margin: 0 0 10px;
    line-height: 1.6;
    letter-spacing: 0.5px;
  }

  .entry-content {
    font-size: 13px;
    color: #8a8580;
    line-height: 1.7;
    margin: 0;
  }

  .changelog-footer {
    margin-top: 80px;
    padding: 24px 0;
    text-align: center;
    border-top: 1px solid #1a1a2e22;
  }

  .changelog-footer p {
    font-size: 12px;
    color: #5f574f55;
    margin: 0;
  }
</style>
