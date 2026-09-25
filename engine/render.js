// Render an episode's frames with headless Chromium and pipe them into ffmpeg.
// usage: node render.js <episode.json> <outdir>
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
(async () => {
  const [epPath, out] = process.argv.slice(2);
  const ep = JSON.parse(fs.readFileSync(epPath));
  const tl = JSON.parse(fs.readFileSync(path.join(out, 'timeline.json')));
  const FF = process.env.FFMPEG || 'ffmpeg';
  const exe = process.env.CHROMIUM || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);
  const b = await chromium.launch(exe ? { executablePath: exe } : {});
  const land = ep.format === 'landscape';
  const p = await b.newPage({ viewport: land ? { width: 1920, height: 1080 } : { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'player', 'player.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.evaluate(([e, t]) => window.setup(e, t), [ep, tl]);
  const n = Math.round(tl.duration * tl.fps);
  const only = process.env.FRAMES ? process.env.FRAMES.split(',').map(Number) : null;
  if (only) { // still frames for review
    for (const s of only) { await p.evaluate(t => window.render(t), s); await p.screenshot({ path: path.join(out, 'still-' + s + '.png') }); }
    await b.close(); return;
  }
  const ff = spawn(FF, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(tl.fps), '-i', '-',
    '-c:v', 'libx264', '-preset', land ? 'slow' : 'medium', '-tune', 'animation', '-crf', land ? '24' : '18', '-pix_fmt', 'yuv420p', '-r', String(tl.fps), path.join(out, 'video.mp4')]);
  ff.stderr.on('data', d => process.stderr.write(d));
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => window.render(t), i / tl.fps);
    const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) process.stdout.write(`frame ${i}/${n}\n`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await b.close();
})();
