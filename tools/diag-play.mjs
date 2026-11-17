import { chromium } from 'playwright-core';
import { appendFileSync } from 'node:fs';
const sum = (s) => appendFileSync(process.env.GITHUB_STEP_SUMMARY, s + '\n');
const url = process.env.TARGET_URL;
sum('## 진단: 지금 플레이 (번들 원인 위치)');
const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage();
const errs = [];
page.on('pageerror', (e) => errs.push(e.stack || e.message));
try {
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.getByRole('button', { name: '지금 플레이' }).first().click();
  await page.waitForTimeout(3000);
} catch (e) { sum('- script error: ' + e.message); }
const first = errs.find((x) => /id is not defined/.test(x)) || '';
sum('- first pageerror: ' + first.split('\n')[0]);
const m = first.match(/(https?:\/\/[^\s)]+\.js):(\d+):(\d+)/);
if (m) {
  const bundle = await (await fetch(m[1])).text();
  const ln = bundle.split('\n')[Number(m[2]) - 1] || '';
  const col = Number(m[3]);
  sum('- bundle line ' + m[2] + ' col ' + m[3] + ' context:');
  sum('```');
  sum(ln.slice(Math.max(0, col - 300), col + 300));
  sum('```');
} else { sum('- could not parse bundle location'); }
await browser.close();
