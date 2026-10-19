"""Typeset the maths on the site with LaTeX as SVG, in IBM Plex Sans Italic.

Pages that have `math: true` in their front matter can contain formulas written
between double dollar signs:

    inline:   the rest state is stable for $$\\varepsilon < 0.44$$.
    display:  a line containing only $$ ... $$

This script finds every formula, typesets it with LaTeX and saves it as
_maths/<hash>.svg. When the site is built, _plugins/maths.rb puts each SVG in
place of its formula, drawn in the text colour (so it follows light/dark mode).

The site's GitHub build runs it automatically. To preview maths locally, run it
after adding or changing a formula (committing the new files in _maths/ is optional):

    python3 tools/render_maths.py

Requires XeLaTeX with the unicode-math, plex and firamath packages, and dvisvgm
(all part of TeX Live and MacTeX). Formulas already typeset are skipped; --force redoes all.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_maths")
SKIP = {"_site", "vendor", "node_modules", ".git", "_maths", "tools"}

# Letters in IBM Plex Sans Italic and digits in IBM Plex Sans, to match the text;
# Plex has no maths symbols and almost no Greek, so those come from Fira Math,
# a sans-serif maths font (Plex's own pi and partial sign are kept).
PREAMBLE = r"""\documentclass[10pt]{article}
\usepackage{amsmath}
\usepackage{unicode-math}
\setmathfont{FiraMath-Regular.otf}
\setmathfont[range={it/{latin,Latin}}]{IBMPlexSans-Italic.otf}
\setmathfont[range={up/{num}}]{IBMPlexSans-Regular.otf}
\setmathfont[range={"03C0,"2202}]{IBMPlexSans-Italic.otf}
\hoffset=-1in \voffset=-1in
\begin{document}
"""

DISPLAY = re.compile(r"^[ \t]*\$\$(.+?)\$\$[ \t]*$", re.M)
INLINE = re.compile(r"\$\$(.+?)\$\$", re.S)


def key(mode, tex):
    """Must match the key computed in _plugins/maths.rb."""
    return hashlib.sha1(f"{mode}:{tex.strip()}".encode()).hexdigest()[:16]


def formulas():
    found = {}
    for top, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for f in files:
            if not f.endswith((".md", ".markdown", ".html")):
                continue
            text = open(os.path.join(top, f), encoding="utf-8").read()
            m = re.match(r"---\n(.*?)\n---", text, re.S)
            if not m or not re.search(r"^math:\s*true\s*$", m.group(1), re.M):
                continue
            body = text[m.end():]
            for d in DISPLAY.findall(body):
                found[key("display", d)] = ("display", d.strip())
            for i in INLINE.findall(DISPLAY.sub("", body)):
                found[key("inline", i)] = ("inline", i.strip())
    return found


def typeset(items):
    """One DVI page per formula, exactly the size of TeX's box. TeX reports width,
    height and depth, so inline formulas can sit on the text's baseline."""
    pages = []
    for k, (mode, tex) in items:
        style = r"\displaystyle " if mode == "display" else ""
        pages.append(r"\sbox0{$" + style + tex + r"$}"
                     r"\typeout{DIM:\the\wd0:\the\ht0:\the\dp0}"
                     r"\edef\ps{papersize=\the\wd0,\the\dimexpr\ht0+\dp0\relax}"
                     r"\shipout\vbox{\special{\ps}\box0}")
    tmp = tempfile.mkdtemp()
    try:
        with open(os.path.join(tmp, "m.tex"), "w") as fh:
            fh.write(PREAMBLE + "\n".join(pages) + "\n\\end{document}\n")
        run = subprocess.run(["xelatex", "-no-pdf", "-interaction=nonstopmode", "-halt-on-error", "m.tex"],
                             cwd=tmp, capture_output=True, text=True)
        if run.returncode:
            sys.exit("LaTeX failed:\n" + "\n".join(l for l in run.stdout.splitlines() if l.startswith("!") or l.startswith("l.")))
        subprocess.run(["dvisvgm", "--no-fonts", "--bbox=papersize", "--page=1-",
                        "-o", "p-%4p.svg", "m.xdv"], cwd=tmp, check=True, capture_output=True)
        dims = re.findall(r"DIM:([\d.]+)pt:([\d.]+)pt:([\d.]+)pt", open(os.path.join(tmp, "m.log")).read())
        for n, ((k, _), (w, h, d)) in enumerate(zip(items, dims), start=1):
            svg = open(os.path.join(tmp, f"p-{n:04d}.svg")).read()
            svg = svg[svg.index("<svg"):]
            # sizes in em of 10pt, so the formula scales with the surrounding text
            w, h, d = float(w) / 10, float(h) / 10, float(d) / 10
            svg = re.sub(r"\s(width|height)=['\"][^'\"]*['\"]", "", svg, count=2)
            svg = svg.replace("<svg ", f'<svg style="width:{w:.3f}em;height:{h + d:.3f}em;'
                              f'vertical-align:-{d:.3f}em" fill="currentColor" aria-hidden="true" ', 1)
            # many formulas share one page: give each its own glyph names, or a formula
            # can borrow another's glyphs (e.g. a digit from a larger display equation)
            svg = re.sub(r"\bid=(['\"])", rf"id=\1m{k}-", svg)
            svg = re.sub(r"href=(['\"])#", rf"href=\1#m{k}-", svg)
            svg = re.sub(r"url\(#", f"url(#m{k}-", svg)
            svg = re.sub(r"\s*\n\s*", " ", svg).strip()      # one line, safe inside Markdown
            with open(os.path.join(OUT, k + ".svg"), "w") as fh:
                fh.write(svg + "\n")
    finally:
        shutil.rmtree(tmp)


def main():
    os.makedirs(OUT, exist_ok=True)
    found = formulas()
    force = "--force" in sys.argv
    todo = [(k, v) for k, v in sorted(found.items())
            if force or not os.path.exists(os.path.join(OUT, k + ".svg"))]
    if todo:
        typeset(todo)
    unused = [f for f in os.listdir(OUT) if f.endswith(".svg") and f[:-4] not in found]
    for f in unused:
        os.remove(os.path.join(OUT, f))
    print(f"{len(found)} formulas: {len(todo)} typeset, {len(found) - len(todo)} already done, "
          f"{len(unused)} unused removed")


if __name__ == "__main__":
    main()
