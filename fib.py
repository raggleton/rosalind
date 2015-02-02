"""
http://rosalind.info/problems/fib/

Given: Positive integers n <= 40 and k <= 5.

Return: The total number of rabbit pairs that will be present after n months if 
we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

"""

import common

sample_data = "5 3"
sample_output = "19"

# Formula: F_n = F_{n-1} + kF_{n-2}

def fib(inp):
    n = int(inp.split()[0])
    k = int(inp.split()[1])
    return str(term(n, k))

def term(i, k):
    if i == 1 or i == 2:
        return 1
    else:
        return term(i-1, k) + (k*term(i-2, k))

common.test(fib, sample_data, sample_output)

common.runit(fib)