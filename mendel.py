"""
http://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing 
k+m+n organisms: k individuals are homozygous dominant for a factor, 
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce 
an individual possessing a dominant allele (and thus displaying the dominant 
phenotype). Assume that any two organisms can mate.
"""

import common
from math import factorial

sample_data = "2 2 2"
sample_output = "0.78333"


def prob(inp):
    # k homozygous dominant (YY)
    # m heterozygous (Yy)
    # n homozygous recessive (yy)
    k, m, n = [float(x) for x in inp.split(" ")]
    N = k + m + n
    Nm = N - 1.0
    p = (k/N) # YY chosen first
    p += (m/N) * ( (k/Nm) + (0.75*(m-1)/Nm) + (0.5*(n/Nm)) )  # Yy first
    p += (n/N) * ( (k/Nm) + (0.5*(m/Nm)) )  #yy first
    return "%.5f" % p


common.test(prob, sample_data, sample_output)

common.runit(prob)