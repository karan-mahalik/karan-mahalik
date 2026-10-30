#!/usr/bin/env python3
"""Validate Karan's GitHub profile references, SVG syntax and safe card bounds."""
from pathlib import Path
from xml.etree import ElementTree as ET
import re
import sys
root=Path(__file__).resolve().parents[1]
readme=(root/'README.md').read_text(encoding='utf-8')
issues=[]
required=["assets/branding/profile-header.svg","assets/branding/portfolio-cta.svg",
"assets/diagrams/current-focus.svg","assets/diagrams/data-workflow.svg",
"assets/projects/urbancart.svg","assets/projects/pizza.svg",
"assets/projects/stilique.svg","assets/projects/pulsechat.svg",
"assets/projects/movie.svg","assets/projects/genai.svg",
"generative-ai/README.md","generative-ai/PROJECT_TEMPLATE.md",
"credentials/gats-internship.md","docs/VISUAL_DESIGN.md"]
for name in required:
    if not (root/name).is_file():
        issues.append(f"Missing: {name}")
for x in re.findall(r'<img[^>]*src="([^"]+)"',readme):
    if x.startswith('assets/') and not (root/x).is_file():
        issues.append(f"Missing image reference: {x}")
for name in ('PizzaSalesAnalysis','UrbanCartAnalysis','stilique-frontend','PulseChat','Movie-Suggestion-App'):
    if f'https://github.com/karan-mahalik/{name}' not in readme:
        issues.append(f'Missing source link: {name}')
for path in sorted((root/'assets').rglob('*.svg')):
    try: svg=ET.parse(path).getroot()
    except ET.ParseError as exc:
        issues.append(f'Malformed SVG {path}: {exc}')
        continue
    if 'viewBox' not in svg.attrib:
        issues.append(f'No viewBox: {path}')
    if not any(el.tag.endswith('title') for el in svg):
        issues.append(f'No SVG title: {path}')
    if '/projects/' in str(path):
        if svg.attrib.get('viewBox') != '0 0 720 226':
            issues.append(f'Unexpected project dimensions: {path}')
        for el in svg.iter():
            if not el.tag.endswith('text'): continue
            try:
                x=float(el.attrib.get('x','0')); size=float(el.attrib.get('font-size','0'))
            except ValueError: continue
            text=''.join(el.itertext()).strip()
            if x < 100 and size >= 27 and x+len(text)*size*.59 >= 575:
                issues.append(f'Potential title/icon collision: {path}: {text}')
if issues:
    print('Profile validation FAILED')
    for x in issues: print(' -',x)
    sys.exit(1)
print('Profile links, image assets, SVG syntax, and conservative title/icon bounding checks passed.')
print('A browser-level visual test is still recommended.')
