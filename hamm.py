"""
http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

"""

import common
from itertools import izip

sample_data = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""

sample_output = "7"


def hamm(inp):
    s = inp.splitlines()[0]
    t = inp.splitlines()[1]
    return str(sum([ i != j for i,j in izip(s, t)]))

common.test(hamm, sample_data, sample_output)

common.runit(hamm)