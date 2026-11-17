import { chromium } from 'playwright';

const url = process.env.TARGET_URL || 'https://sigco3111.github.io/gitvana-ko/';
const browser = await chromium.launch();
const page = await browser.newPage();
page.on('console', (m) => console.log('[console.' + m.type() + ']', m.text()));
page.on('pageerror', (e) => console.log('[pageerror]', e.stack || e.message));
page.on('requestfailed', (r) => console.log('[requestfailed]', r.url(), r.failure()?.errorText));
page.on('response', (r) => { if (r.status() >= 400) console.log('[http ' + r.status() + ']', r.url()); });

await page.goto(url, { waitUntil: 'networkidle' });
console.log('STEP before click, landing text visible:', await page.getByText('Monastery of Version Control').count());
const btn = page.getByRole('button', { name: '지금 플레이' }).first();
console.log('STEP button count:', await btn.count());
await btn.click();
console.log('STEP clicked');
await page.waitForTimeout(4000);
console.log('STEP after click, landing text visible:', await page.getByText('Monastery of Version Control').count());
const body = await page.evaluate(() => document.body.innerText.slice(0, 600));
console.log('STEP body text head:', JSON.stringify(body));
await page.screenshot({ path: 'after-click.png', fullPage: false });
await browser.close();
