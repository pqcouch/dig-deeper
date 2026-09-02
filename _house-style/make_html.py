#!/usr/bin/env python3
"""Markdown -> the house two-pane reading HTML.

  python3 make_html.py report.md [report.html]

Sticky left Contents sidebar beside a main column, wrapped as
<div class="wrap"><nav>...</nav><main>...</main></div>. The sidebar is built
from the H1 title plus every H2, using the headings' own ids. lang="en-GB".
CSS applied verbatim from dig-deeper-html-house-style.md.
"""
import html, os, re, subprocess, sys

CSS = ''':root{--ink:#24211c;--muted:#6b6459;--rule:#e3ddd1;--accent:#7a5c2e;--bg:#fbf9f4;--card:#fff;}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
   font-family:"Liberation Serif","Georgia",serif;font-size:18px;line-height:1.5;}
  .wrap{max-width:1150px;margin:0 auto;display:grid;grid-template-columns:270px 1fr;gap:0;}
  nav{position:sticky;top:0;align-self:start;height:100vh;overflow:auto;
   padding:1.4rem 1rem 3rem 1.4rem;border-right:1px solid var(--rule);font-size:14.5px;line-height:1.35;}
  nav h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:1.2rem 0 .4rem;}
  nav a{display:block;color:var(--ink);text-decoration:none;padding:.18rem 0;border-bottom:1px dotted transparent;}
  nav a:hover{color:var(--accent);border-bottom-color:var(--rule);}
  nav ul{list-style:none;margin:0;padding:0;}
  nav ul ul a{padding-left:.9rem;color:var(--muted);font-size:13.5px;}
  main{padding:2.2rem clamp(1rem,4vw,3rem) 6rem;max-width:820px;}
  h1{font-size:1.9rem;line-height:1.15;margin:.2rem 0 1.4rem;}
  h2{font-size:1.4rem;margin:2.4rem 0 .5rem;padding-top:1rem;border-top:2px solid var(--rule);color:var(--accent);}
  h3{font-size:1.12rem;margin:1.5rem 0 .3rem;}
  h4{font-size:1rem;margin:1.1rem 0 .2rem;color:var(--muted);}
  p{margin:.5rem 0;}
  blockquote{margin:.8rem 0;padding:.4rem 0 .4rem 1rem;border-left:3px solid var(--accent);color:#40392e;background:#f4efe4;}
  code{background:#f0ebdf;padding:.05em .35em;border-radius:3px;font-size:.85em;
   font-family:"Liberation Mono",ui-monospace,monospace;color:#5a4a2a;}
  table{border-collapse:collapse;width:100%;margin:.9rem 0;font-size:15px;}
  th,td{border:1px solid var(--rule);padding:.4rem .55rem;text-align:left;vertical-align:top;}
  th{background:#efe9dc;}
  tr:nth-child(even) td{background:#faf7f0;}
  hr{border:none;border-top:1px solid var(--rule);margin:2.2rem 0;}
  strong{color:#332e26;}
  main>ul,main>ol{padding-left:1.3rem;}
  li{margin:.25rem 0;}
  .tag{white-space:nowrap;}
  @media(max-width:820px){.wrap{grid-template-columns:1fr}nav{position:static;height:auto;border-right:none;border-bottom:1px solid var(--rule)}main{padding-top:1.2rem}}'''

def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def main():
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '.html'
    md = open(src, encoding='utf-8').read()
    # Pre-flight: a bare --- rule can be swallowed as YAML or a table rule.
    n_rules = len(re.findall(r'(?m)^[ \t]*-{3,}[ \t]*$', md))
    md = re.sub(r'(?m)^[ \t]*-{3,}[ \t]*$', '***', md)
    n_h2_src = len(re.findall(r'(?m)^## (?!#)', md))
    frag = subprocess.run(['pandoc', '-f', 'markdown', '-t', 'html5'],
                          input=md, capture_output=True, text=True, check=True).stdout
    # Headings quoted inside a blockquote are proposed text, not sections of
    # this document: they must not reach the sidebar or the section count.
    body = re.sub(r'<blockquote>.*?</blockquote>', '', frag, flags=re.S)
    heads = re.findall(r'<(h[12]) id="([^"]+)"[^>]*>(.*?)</\1>', body, re.S)
    title = next((strip_tags(t) for tag, i, t in heads if tag == 'h1'), os.path.basename(src))
    items = '\n'.join('    <li><a href="#%s">%s</a></li>' % (i, html.escape(strip_tags(t)))
                      for tag, i, t in heads)
    doc = ('<!DOCTYPE html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
           '<title>%s</title>\n<style>\n%s\n</style>\n</head>\n<body>\n'
           '<div class="wrap">\n<nav>\n  <h2>Contents</h2>\n  <ul>\n%s\n  </ul>\n</nav>\n'
           '<main>\n%s\n</main>\n</div>\n</body>\n</html>\n'
           % (html.escape(title), CSS, items, frag))
    # Verify before delivering
    ids = set(re.findall(r'id="([^"]+)"', frag))
    anchors = re.findall(r'href="#([^"]+)"', doc)
    dangling = [a for a in anchors if a not in ids]
    n_h2_out = len(re.findall(r'<h2 id=', body))
    trapped = re.findall(r'<td[^>]*>\s*<h[1-6]', frag)
    print('rules normalised: %d | H2 in source: %d | H2 in body: %d | nav links: %d'
          % (n_rules, n_h2_src, n_h2_out, len(anchors)))
    problems = []
    if dangling:
        problems.append('dangling anchors: %s' % dangling)
    if n_h2_out != n_h2_src:
        problems.append('H2 count mismatch (pandoc may have dropped a section)')
    if trapped:
        problems.append('heading trapped in a table cell')
    if problems:
        print('FAILED VERIFICATION:'); [print('  -', p) for p in problems]; sys.exit(1)
    open(dst, 'w', encoding='utf-8').write(doc)
    print('verified OK -> %s' % dst)

if __name__ == '__main__':
    main()
