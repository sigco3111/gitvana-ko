<script lang="ts">
  import { onMount } from 'svelte';
  import Navbar from '../shared/Navbar.svelte';

  const entries = [
    {
      id: '2026-04-06-i18n',
      date: '06/04/2026',
      text: `오늘 다국어(i18n) 인프라를 만들었습니다. 모든 UI 문자열(버튼, 레이블, 제목)이 이제 JSON 로케일 파일을 읽는 t() 번역 함수를 거칩니다. 영어가 기준 원문이고, 다른 언어에 빠진 키는 자동으로 영어로 대체됩니다.

언어 선택기는 로케일이 2개 이상일 때만 나타나므로 지금은 보이지 않습니다. 하지만 기반은 갖춰져 있습니다. GitHub에서 pt-BR 지원을 요청한 사람이 있었고, 커뮤니티가 번역에 쉽게 기여할 수 있도록 만들고 싶습니다.

어려운 부분은 코드가 아니라 내용입니다. 38개 레벨의 수도원 유머, 엄격한 고양이, Monkey Island 스타일의 대사가 있습니다. 번역기에 돌린다고 그 느낌이 살아나지는 않습니다. 분위기를 이해하는 사람들이 필요합니다. 도움을 최대한 쉽게 줄 수 있도록 CONTRIBUTING_TRANSLATIONS.md를 작성했습니다.`,
    },
    {
      id: '2026-04-06-bugfixes',
      date: '06/04/2026',
      text: `버그 수정의 날이었습니다. rorar라는 사용자가 한자리에서 이슈를 8개나 남겼습니다. 놀라운 피드백이었습니다. 대부분 고쳤습니다. 화면 너비를 넘어 줄바꿈되는 긴 입력에서 터미널이 깨지던 문제(커서 계산이 줄바꿈을 고려하지 않았음), && 로 nano를 연결하면 "command not found"가 나오던 문제, 커밋 해시가 있는 git diff가 아예 구현되지 않았던 문제, 그리고 목표가 지시하는데도 git status를 쓰면 감점되던 레벨 문제를 고쳤습니다.

색상 구분된 git log 출력(노란 해시, 초록 장식, 청록 작성자)과 문서로 연결되는 man 명령도 추가했습니다. 작은 변화지만 실제 터미널처럼 느껴지도록 만들어 줍니다.`,
    },
    {
      id: '2026-04-03-remotes',
      date: '03/04/2026',
      text: `git push, fetch, pull을 추가했습니다. 모든 것이 브라우저에서 돌아가므로 실제 원격 서버는 없고, 그래서 가짜로 만들었습니다. 같은 IndexedDB 파일 시스템의 /remote/origin에 있는 두 번째 git 저장소입니다. push는 한쪽 방향으로 객체를 복사하고, fetch는 반대 방향입니다. isomorphic-git은 신경 쓰지 않고 내용 주소 blob을 읽고 쓸 뿐입니다.

원격 협업의 기초를 가르치는 새 레벨 3개가 있습니다. 구이브러시 수도승은 여러분이 보지 않을 때 원격에 push하고, 여러분은 그것을 처리해야 합니다. 커밋 그래프에 원격 추적 브랜치도 추가했습니다. 점선 테두리로 표시되어 로컬 브랜치와 구별할 수 있습니다.

이제 되돌리기 시스템이 원격도 처리합니다. push한 뒤 되돌리면 원격도 이전 상태로 돌아갑니다. 이 부분이 push 자체보다 오래 걸렸습니다.`,
    },
    {
      id: '2026-04-02-thousand',
      date: '02/04/2026',
      text: `첫날에 천 명이 Gitvana를 플레이했습니다. 무슨 일이 일어났는지 잘 모르겠습니다. Reddit에 공유하고 커피를 타러 갔다가 돌아왔는데 텔레메트리 대시보드의 숫자가 이상해 보였습니다. 이상한 게 아니었습니다.

진심으로 감사합니다. git 튜토리얼이 지루하다고 생각해서 밤에 만든 개인 프로젝트입니다. 낯선 사람들이 실제로 플레이하고 그중 일부가 배우고 있다는 사실이 저에게 큰 의미가 있습니다.

여기까지 와 주셨다면 — 감사합니다. 피드백, 아이디어, 불만, 무엇이든 듣고 싶습니다. GitHub에 이슈를 열거나 그냥 연락해 주셔도 됩니다. 모든 글을 읽습니다. 이 프로젝트는 작고, 더 좋게 만들고 싶습니다. 사용하는 분들의 이야기를 듣지 않고서는 그럴 수 없습니다.`,
    },
    {
      id: '2026-03-31-start',
      date: '31/03/2026',
      text: `이걸 시작했습니다. 아이디어는 숙제처럼 느껴지지 않으면서 git을 가르치는 게임입니다. 제가 본 튜토리얼은 모두 같은 패턴입니다. init, add, commit, branch, merge. 그런 방식으로는 아무도 git을 배우지 못합니다.

모험 게임이면 어떨까요. 수도승들이 오래된 코드를 보존하는 수도원. 여러분의 커밋을 심판하는 고양이. 대사 스타일은 Monkey Island에서 영감을 받았습니다. 엉뚱하고, 스스로를 아는 듯하고, 조금 어리석습니다. 유머와 배움이 함께 있을 수 있다고 생각했습니다.

오늘 밤 프로토타입이 돌아가기 시작했습니다. 왼쪽에 터미널, 오른쪽에 커밋 그래프, 위에 목표가 있습니다. 실제 git 명령을 입력하면 그래프가 실시간으로 바뀝니다. 새벽 3시인데 그만해야 하지만 자꾸 기능을 추가하고 있습니다.

뭔가 될 수도 있고 일주일 뒤에 흥미를 잃을 수도 있습니다. 두고 보겠습니다.`,
    },
  ];

  // --- Likes ---
  const SESSION_KEY = 'gitvana-session-id';
  function getSessionId(): string {
    let id = localStorage.getItem(SESSION_KEY);
    if (!id) {
      id = crypto.randomUUID();
      localStorage.setItem(SESSION_KEY, id);
    }
    return id;
  }

  const LIKES_STORAGE_KEY = 'gitvana-blog-likes';

  function loadLocalLikes(): Record<string, boolean> {
    try {
      return JSON.parse(localStorage.getItem(LIKES_STORAGE_KEY) || '{}');
    } catch { return {}; }
  }

  function saveLocalLikes(liked: Record<string, boolean>) {
    localStorage.setItem(LIKES_STORAGE_KEY, JSON.stringify(liked));
  }

  let likeCounts = $state<Record<string, number>>({});
  let likedByMe = $state<Record<string, boolean>>(loadLocalLikes());

  let serverReachable = false;

  async function fetchLikes() {
    try {
      const res = await fetch(`/api/blog/likes?session=${getSessionId()}`);
      if (!res.ok) return;
      const contentType = res.headers.get('content-type') || '';
      if (!contentType.includes('application/json')) return;
      const data = await res.json();
      serverReachable = true;
      likeCounts = data.counts || {};
      // Merge: keep local likes, overlay server truth
      const serverLiked = data.liked || {};
      likedByMe = { ...likedByMe, ...serverLiked };
      saveLocalLikes(likedByMe);
    } catch { /* offline — local state is fine */ }
  }

  async function toggleLike(postId: string) {
    const wasLiked = !!likedByMe[postId];
    // Optimistic update
    likedByMe = { ...likedByMe, [postId]: !wasLiked };
    likeCounts = { ...likeCounts, [postId]: (likeCounts[postId] || 0) + (wasLiked ? -1 : 1) };
    saveLocalLikes(likedByMe);

    try {
      const res = await fetch('/api/blog/likes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          postId,
          sessionId: getSessionId(),
          unlike: wasLiked,
        }),
      });
      if (res.ok) {
        const data = await res.json();
        likeCounts = { ...likeCounts, [postId]: data.count };
      }
    } catch {
      // Keep local state — server will sync next time
    }
  }

  onMount(() => {
    fetchLikes();
  });
</script>

<div class="devblog-page">
  <Navbar currentPage="devblog" />

  <div class="devblog-content">
    <header class="devblog-header">
      <h1 class="devblog-title">GITVANA 개발 일지</h1>
      <p class="devblog-subtitle">Raffaele Pizzari</p>
    </header>

    <div class="entries">
      {#each entries as entry}
        <div class="entry">
          <div class="entry-date">{entry.date}</div>
          <div class="entry-text">{@html entry.text.replace(/\n\n/g, '</p><p>').replace(/^/, '<p>').replace(/$/, '</p>')}</div>
          <button
            class="like-btn"
            class:liked={likedByMe[entry.id]}
            onclick={() => toggleLike(entry.id)}
            aria-label="이 글 좋아요"
          >
            <span class="like-heart">{likedByMe[entry.id] ? '\u2665' : '\u2661'}</span>
            {#if likeCounts[entry.id]}
              <span class="like-count">{likeCounts[entry.id]}</span>
            {/if}
          </button>
        </div>
      {/each}
    </div>

    <footer class="devblog-footer">
      <p>&copy; 2026 Raffaele Pizzari &mdash; <a href="https://github.com/pixari/gitvana">github</a></p>
    </footer>
  </div>
</div>

<style>
  .devblog-page {
    position: fixed;
    inset: 0;
    background: #0a0a0a;
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 200;
    color: #c2c3c7;
    font-family: 'JetBrains Mono', monospace;
  }

  .devblog-content {
    max-width: 640px;
    margin: 0 auto;
    padding: 44px 24px 60px;
  }

  .devblog-header {
    padding: 56px 0 40px;
    border-bottom: 1px solid #1a1a2e;
    margin-bottom: 32px;
  }

  .devblog-title {
    font-family: 'Press Start 2P', monospace;
    font-size: clamp(12px, 3vw, 16px);
    color: #ffa300;
    margin: 0 0 10px;
    letter-spacing: 3px;
  }

  .devblog-subtitle {
    font-size: 12px;
    color: #5f574f;
    margin: 0;
  }

  .entries {
    display: flex;
    flex-direction: column;
    gap: 0;
  }

  .entry {
    padding: 24px 0;
    border-bottom: 1px solid #1a1a2e;
  }

  .entry:last-child {
    border-bottom: none;
  }

  .entry-date {
    font-family: 'Press Start 2P', monospace;
    font-size: 9px;
    color: #5f574f;
    margin-bottom: 14px;
    letter-spacing: 1px;
  }

  .entry-text {
    font-size: 13px;
    color: #a09a93;
    line-height: 1.75;
  }

  .entry-text :global(p) {
    margin: 0 0 12px;
  }

  .entry-text :global(p:last-child) {
    margin-bottom: 0;
  }

  .like-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px 0 0;
    color: #5f574f;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    transition: color 0.15s;
  }

  .like-btn:hover {
    color: #ff004d;
  }

  .like-btn.liked {
    color: #ff004d;
  }

  .like-heart {
    font-size: 16px;
    line-height: 1;
  }

  .like-count {
    font-size: 11px;
    color: #5f574f;
  }

  .like-btn.liked .like-count {
    color: #ff004d88;
  }

  .devblog-footer {
    margin-top: 48px;
    padding: 24px 0;
    border-top: 1px solid #1a1a2e;
  }

  .devblog-footer p {
    font-size: 11px;
    color: #5f574f55;
    margin: 0;
  }

  .devblog-footer a {
    color: #5f574f88;
    text-decoration: none;
  }

  .devblog-footer a:hover {
    color: #ffa300;
  }

  @media (max-width: 600px) {
    .devblog-content {
      padding: 44px 16px 40px;
    }
  }
</style>
