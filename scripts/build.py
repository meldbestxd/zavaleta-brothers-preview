#!/usr/bin/env python3
from pathlib import Path
import re, shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
PAGES = ['index.html', 'gallery.html', 'styles.css', 'script.js']
ASSET_PATTERN = re.compile(r'(?:src|href|content)=["\']([^"\']+)["\']|url\(["\']?([^"\')]+)')
SITE_URL = 'https://meldbestxd.github.io/zavaleta-brothers-preview/'

if DIST.exists():
    shutil.rmtree(DIST)
(DIST / 'assets').mkdir(parents=True)

for name in PAGES:
    shutil.copy2(ROOT / name, DIST / name)

assets = set()
for name in ['index.html', 'gallery.html', 'styles.css']:
    text = (ROOT / name).read_text(errors='ignore')
    for a, b in ASSET_PATTERN.findall(text):
        ref = (a or b).split('?')[0]
        if ref.startswith('assets/'):
            assets.add(ref)

assets.add('assets/zavaleta-brothers.vcf')
for ref in sorted(assets):
    src = ROOT / ref
    if src.exists():
        dst = DIST / ref
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

(DIST / '_headers').write_text('''/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Cache-Control: public, max-age=3600
/assets/*
  Cache-Control: public, max-age=31536000, immutable
''')
(DIST / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + SITE_URL + 'sitemap.xml\n')
(DIST / 'sitemap.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{SITE_URL}</loc><priority>1.0</priority></url>
  <url><loc>{SITE_URL}gallery.html</loc><priority>0.8</priority></url>
</urlset>
''')
print(f'Built {DIST}')
print('Files:', sum(1 for _ in DIST.rglob('*') if _.is_file()))
