// Render still thumbnails (1280x720) from concepts/thumbs.json with the doodle player.
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
(async () => {
  const exe = fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined;
  const b = await chromium.launch(exe ? { executablePath: exe } : {});
  const all = JSON.parse(fs.readFileSync(path.join(__dirname, process.env.THUMBS || 'thumbs.json')));
  fs.mkdirSync(path.join(__dirname, 'out', 'thumbs'), { recursive: true });
  for (const th of all) {
    const sz = th.size || [1280, 720]; const p = await b.newPage({ viewport: { width: sz[0], height: sz[1] } });
    await p.goto('file://' + path.join(__dirname, 'doodle.html')); await p.evaluate(() => document.fonts.ready);
    const ep = { id: th.id, size: sz, captions: false, lines: [{ who: 'none', text: '', scene: { group: 'g', items: th.items, cam: [1, 1] } }] };
    const tl = { duration: 6, fps: 30, env: [0], lines: [{ i: 0, who: 'none', text: '', s: 0, e: 0.1, words: [], scene: {} }] };
    await p.evaluate(([e, t]) => { window.setup(e, t); window.render(4); }, [ep, tl]);
    await p.screenshot({ path: path.join(__dirname, 'out', 'thumbs', th.id + '.png') }); await p.close();
  }
  await b.close();
})();
