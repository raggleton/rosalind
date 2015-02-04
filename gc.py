"""
http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the 
GC-content of that string. Rosalind allows for a default error of 0.001 in all 
decimal answers unless otherwise stated; please see the note on absolute error below.
"""

import common
from collections import Counter

sample_data = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

sample_output = """Rosalind_0808
60.919540
"""


class Dna():

    def __init__(self, ID, dna_str=None):
        self.ID = ID
        self.dna_str = dna_str if dna_str else ""
        self.gc = 0.0

    def get_gc(self):
        c = Counter(self.dna_str)
        self.gc = 100.0 * float(c['G'] + c['C']) / float(len(self.dna_str))

    def __repr__(self):
        return "%s %s\n%s" % (self.ID, str(self.gc), self.dna_str)


def gc(inp):
    dnas = []
    current_dna = None
    for line in inp.splitlines():
        print line
        if line.startswith(">"):
            if current_dna:
                current_dna.get_gc()
                dnas.append(current_dna)
            current_dna = Dna(ID=line.replace(">", "").strip())
        else:
            # dna stretches over multiple lines
            current_dna.dna_str += line.strip()
    dnas.append(current_dna)

    # from pprint import pprint
    # pprint(dnas)

    max_dna = dnas[0]
    for d in dnas:
        if d.gc > max_dna.gc:
            max_dna = d
    print ""
    print "DNA with largest GC content:"
    print max_dna.ID
    print max_dna.gc

    return "%s\n%s" %(max_dna.ID, str(max_dna.gc))


common.test(gc, sample_data, sample_output)

common.runit(gc)
