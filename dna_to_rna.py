"""
http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t. (T => U)
"""
import common

alphabet = ['A', 'C', 'G', 'U']
sample_data = "GATGGAACTTGACTACGTAAATT"
sample_output = "GAUGGAACUUGACUACGUAAAUU"

def scribe(dna):
    out = dna.replace("T", "U")
    return out


common.test(scribe, sample_data, sample_output)

common.runit(scribe)