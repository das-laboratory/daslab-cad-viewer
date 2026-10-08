#!/usr/bin/env python3
"""DAS Lab 도면 뷰어 빌드 — src/viewer.html 과 의존성을 HTML 파일 하나로 묶습니다.

사용법:  npm install  →  python3 build.py
결과물:  dist/daslab-cad-viewer.html   더블클릭으로 여는 단독 실행 파일
         dist/site/                    웹 버전 (index.html · CNAME · .nojekyll) — scripts/publish_site.sh 가 gh-pages 브랜치로 올림
         dist/artifact-body.html       doctype 없이 본문만 (웹 게시 서비스용)

Copyright (C) 2026 주식회사 다스랩 (DAS Lab) — GPL-3.0-or-later
"""
import base64, gzip, html, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent
NM = ROOT / 'node_modules'
OUT_NAME = 'daslab-cad-viewer.html'
SOURCE_URL = 'https://github.com/das-laboratory/daslab-cad-viewer'
SITE_DOMAIN = 'cad-viewer.daslab.co.kr'
SITE_URL = f'https://{SITE_DOMAIN}/'
DESCRIPTION = '설치 없이 브라우저에서 DWG · DXF · PDF · SVG · 이미지 도면을 여는 무료 뷰어. 파일은 기기 안에서만 처리돼요.'

ENGINE_BANNER = ('/*! libredwg-web 0.7.15 (GPL-3.0) (c) MLight Lee; LibreDWG (GPL-3.0-or-later) '
                 '(c) Free Software Foundation, Inc. Source: https://github.com/mlightcad/libredwg-web/tree/v0.7.15 */')


def bundle_engine(out: pathlib.Path) -> str:
    subprocess.run(['npx', 'esbuild', str(ROOT / 'src' / 'entry.mjs'), '--bundle', '--format=iife', '--minify',
                    '--platform=browser', '--define:import.meta.url="https://local/"',
                    '--external:fs', '--external:path', '--external:module', '--external:url', '--external:worker_threads',
                    f'--banner:js={ENGINE_BANNER}', f'--outfile={out}'], check=True, cwd=ROOT)
    return out.read_text(encoding='utf-8')


def main() -> None:
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    site = dist / 'site'
    site.mkdir(exist_ok=True)
    tpl = (ROOT / 'src' / 'viewer.html').read_text(encoding='utf-8')

    engine = bundle_engine(dist / 'dwg-engine.js')
    pdfjs = (NM / 'pdfjs-dist' / 'build' / 'pdf.min.js').read_text(encoding='utf-8')
    worker_b64 = base64.b64encode((NM / 'pdfjs-dist' / 'build' / 'pdf.worker.min.js').read_bytes()).decode()
    wasm = (NM / '@mlightcad' / 'libredwg-web' / 'wasm' / 'libredwg-web.wasm').read_bytes()
    wasm_b64 = base64.b64encode(gzip.compress(wasm, compresslevel=9, mtime=0)).decode()
    logo = 'data:image/png;base64,' + base64.b64encode((ROOT / 'assets' / 'daslab_logo.png').read_bytes()).decode()
    sample = (ROOT / 'assets' / 'sample.dxf').read_text(encoding='utf-8')
    gpl = html.escape((ROOT / 'LICENSE').read_text(encoding='utf-8'))
    apache = html.escape((ROOT / 'licenses' / 'Apache-2.0.txt').read_text(encoding='utf-8'))
    source_line = ''
    if SOURCE_URL:
        u = html.escape(SOURCE_URL)
        shown = html.escape(SOURCE_URL.replace('https://', ''))
        source_line = f' 이 뷰어의 전체 소스: <a href="{u}" target="_blank" rel="noopener">{shown}</a>'

    for name, blob in [('engine', engine), ('pdf.js', pdfjs), ('sample', sample)]:
        assert '</script' not in blob.lower(), f'{name} contains a closing script tag'

    page = (tpl.replace('__LOGO_DATA_URI__', logo)
               .replace('__SOURCE_LINE__', source_line)
               .replace('__GPL_TEXT__', gpl)
               .replace('__APACHE_TEXT__', apache)
               .replace('__SAMPLE_NAME__', '예시_도면.dxf')
               .replace('__SAMPLE_DXF__', sample)
               .replace('__PDFJS__', pdfjs)
               .replace('__DWG_ENGINE__', engine)
               .replace('__PDF_WORKER_B64__', worker_b64)
               .replace('__WASM_GZ_B64__', wasm_b64))
    leftover = set(re.findall(r'__[A-Z][A-Z0-9_]+__', page))
    assert not leftover, f'unfilled placeholders: {leftover}'
    (dist / 'artifact-body.html').write_text(page, encoding='utf-8')

    # Stand-alone document: move <title> into <head> and add share metadata.
    m = re.search(r'<title>(.*?)</title>\n?', page)
    title = m.group(1) if m else 'DAS Lab 도면 뷰어'
    body = page[:m.start()] + page[m.end():] if m else page
    d = html.escape(DESCRIPTION)
    head = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            f'<title>{title}</title>\n<meta name="description" content="{d}">\n'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{d}">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:url" content="{SITE_URL}">\n'
            '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
            '</head>\n<body>\n')
    doc = head + body + '\n</body>\n</html>\n'
    (dist / OUT_NAME).write_text(doc, encoding='utf-8')
    (site / 'index.html').write_text(doc, encoding='utf-8')
    (site / '.nojekyll').write_text('', encoding='utf-8')
    (site / 'CNAME').write_text(SITE_DOMAIN + '\n', encoding='utf-8')
    print(f'built dist/{OUT_NAME} and dist/site/ ({len(doc.encode()) / 1e6:.2f} MB)')


if __name__ == '__main__':
    main()
