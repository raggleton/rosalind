"""
http://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

import common
import re

sample_data = """GATATATGCATATACTT
ATAT"""

sample_output = "2 4 10"


def motif(inp):
    s = inp.splitlines()[0]
    t = inp.splitlines()[1]
    p = re.compile(r'(?=(%s))' % t)
    results = []
    for m in p.finditer(s):
        results.append(str(m.start()+1))
    return ' '.join(results)



common.test(motif, sample_data, sample_output)

common.runit(motif)