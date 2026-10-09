#!/usr/bin/env python3
"""Fill in width/height on every <img> in the given fragments from the real file in ../assets.
Run: python3 _build/imgsize.py _build/sections/s11-*.html   (safe to re-run)"""
import re, sys
from pathlib import Path
from PIL import Image
ASSETS = Path(__file__).resolve().parent.parent / 'assets'
for f in sys.argv[1:]:
    p = Path(f); s = p.read_text(encoding='utf-8')
    def fix(m):
        tag = m.group(0)
        src = re.search(r'src="assets/([^"]+)"', tag)
        if not src: return tag
        img = ASSETS / src.group(1)
        if not img.exists(): sys.exit(f'missing {img}')
        w, h = Image.open(img).size
        tag = re.sub(r'\s(width|height)="\d+"', '', tag)
        return tag.replace('<img', f'<img width="{w}" height="{h}"', 1)
    s2 = re.sub(r'<img\b[^>]*>', fix, s)
    p.write_text(s2, encoding='utf-8'); print('sized', p.name, s2.count('<img'))
