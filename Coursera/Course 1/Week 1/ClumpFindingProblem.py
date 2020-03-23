# The inputs for this problem are
# 1 - The genome sequence
# 2 - K the length of the kmer
# 3 - L the sublength of genome
# 4 - t the minimum number of times the kmer must appear in the subsequence of length L

from FrequentWords import kmerFinder

def findClumps(sequence, k, l, t):
    clumps = set()
    kmers = kmerFinder(k, sequence[0:l])

    for key, value in kmers.items():
        if value >= t and key not in clumps:
            clumps.add(value)

    for i in range(1, len(sequence)-l):
        oldestKmer = sequence[i:i+k]
        newestKmer = sequence[l-k+1+i: l+1+i]

        #kmers[oldestKmer] -= 1
        if newestKmer in kmers:
            kmers[newestKmer] += 1
        else:
            kmers[newestKmer] = 1

        if kmers[newestKmer] >= t and newestKmer not in clumps:
            clumps.add(newestKmer)

    return clumps

    #oldestKmer = sequence[0:k]
    #newestKmer = sequence[l + 1: l + k + 1]



# def findClumps(sequnce, k, l, t):
#     clumps = []
#
#     for i in range(len(sequnce) - l):
#         subSeq = sequnce[i:i+l]
#         kmers = kmerFinder(k, subSeq)
#
#     return clumps
#
#

with open('Escherichia Coli Genome.txt') as fp:
    sequence = fp.readline()
    info = [int(x) for x in fp.readline().split(' ')]
    k,l,t = info

    c = findClumps(sequence, k, l, t)
    print(len(c))