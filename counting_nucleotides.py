"""
http://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

"""

alphabet = ["A", "C", "G", "T"]
sample_data = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
sample_output = "20 12 17 21"


def counter(word):
    """brute-force way"""
    counter = dict(A=0, C=0, G=0, T=0)
    for w in word:
        if w in alphabet:
            counter[w] += 1
    print counter["A"], counter["C"], counter["G"], counter["T"]
    return "%s %s %s %s" % (counter["A"], counter["C"], counter["G"], counter["T"])


out = counter(sample_data)
if out != sample_output:
    print "YOU MUCKED UP"
    print out
