"""
http://rosalind.info/problems/iev/

Given: Six positive integers, each of which does not exceed 20,000. The integers
correspond to the number of couples in a population possessing each genotype
pairing for a given factor. In order, the six given integers represent the
number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.
"""

import common

sample_data = "1 0 0 1 0 1"
sample_output = "3.5"

# probability of getting dominant phenotype for each of the 6 pairs as above
probs = [1., 1., 1., 0.75, 0.5, 0.]

def calc(inp):
    return str(sum([2*probs[i]*int(j) for i, j in enumerate(inp.split(" "))]))


common.test(calc, sample_data, sample_output)

common.runit(calc)
