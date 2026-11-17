import { chromium } from 'playwright-core';
import { appendFileSync } from 'node:fs';

const sum = (s) => appendFileSync(process.env.GITHUB_STEP_SUMMARY, s + '\n');
const err = (s) => console.log('::error::' + s.replace(/\n/g, ' | '));
const url = process.env.TARGET_URL;
sum('## 진단: 지금 플레이');
const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage();
const events = [];
page.on('console', (m) => events.push('console.' + m.type() + ': ' + m.text()));
page.on('pageerror', (e) => events.push('pageerror: ' + (e.stack || e.message)));
page.on('requestfailed', (r) => events.push('requestfailed: ' + r.url() + ' ' + (r.failure() && r.failure().errorText)));
page.on('response', (r) => { if (r.status() >= 400) events.push('http ' + r.status() + ': ' + r.url()); });
try {
  await page.goto(url, { waitUntil: 'networkidle' });
  const before = await page.getByText('Monastery of Version Control').count();
  sum('- landing visible before click: ' + before);
  const btn = page.getByRole('button', { name: '지금 플레이' }).first();
  sum('- play button count: ' + await btn.count());
  await btn.click();
  await page.waitForTimeout(4000);
  const after = await page.getByText('Monastery of Version Control').count();
  sum('- landing visible after click: ' + after);
  const head = await page.evaluate(() => document.body.innerText.slice(0, 300));
  sum('- body head: ' + JSON.stringify(head));
} catch (e) {
  sum('- script error: ' + e.message);
  err('script error: ' + e.message);
}
sum('### 이벤트 (' + events.length + ')');
for (const e of events.slice(0, 80)) sum('- ' + e.replace(/\n/g, ' '));
for (const e of events.filter(x => /pageerror|http [45]|requestfailed/.test(x)).slice(0, 20)) err(e);
await browser.close();
