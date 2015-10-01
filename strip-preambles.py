#!/usr/bin/env python
from glob import glob
import sys

out = open('Scientific-Computing-with-Python.tex', 'w')
preamble = open('Preamble.tex').read()
bodies = []
end = '\\end{document}'

for lecture in sorted(glob("Lecture*.tex")):
    print("Processing:", lecture, file=sys.stderr)
    tex = open(lecture).read()
    _, body = tex.split('\\maketitle')
    body = body.replace('\\end{document}','')
    # Change section types for report document format
    body = body.replace('\\section{', '\\chapter{')
    body = body.replace('\\subsection{', '\\section{')
    body = body.replace('\\subsubsection{', '\\subsection{')
    body = body.replace('\\subsubsubsection{', '\\subsubsection{')
    # Remove logo (added automatically to chapters in new preamble)
    body = body.replace('\\includegraphics{./images/Continuum_Logo_0702.png}~\n', '')
    bodies.append(body)

print(preamble, file=out)
print('\\maketitle', file=out)
for body in bodies:
    print('\\newpage', file=out)
    print(body, file=out)
print(end, file=out)

