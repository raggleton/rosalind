"""
http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

import common

sample_data = "AAAACCCGGT"
sample_output = "ACCGGGTTTT"

comp = dict(A="T", T="A", C="G", G="C")

def complement(dna):
    return "".join([x.replace(x,comp[x]) for x in dna[::-1]])

common.test(complement, sample_data, sample_output)

common.runit(complement)