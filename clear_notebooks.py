# -*- coding: utf-8 -*-
"""
Clear all the output parts of cells in the notebooks

Fuller script for vaious ipython/jupyter versions:
https://github.com/toobaz/ipynb_output_filter/blob/master/ipynb_output_filter.py
"""
from IPython.nbformat.current import read, write
from glob import glob


def clear_nb(lecture):
    nb = read(open(lecture))
    for worksheet in nb['worksheets']:
        for cell in worksheet['cells']:
            if 'outputs' in cell:
                cell['outputs'] = []
            if "prompt_number" in cell:
                del cell["prompt_number"]
    write(nb, open(lecture, 'w'))

if __name__ == '__main__':
    for lecture in sorted(glob("Lecture*.ipynb")):
        clear_nb(lecture)