#finds all kmers of the specified length
def kmerFinder(length, sequence):
    kmercount = {}
    for i in range(len(sequence) - length):
        if sequence[i:i+length] in kmercount:
            kmercount[sequence[i: i + length]] += 1
        else:
            kmercount[sequence[i: i + length]] = 1
    return kmercount

# with open('EX2.txt') as fp:
#     sequence = fp.readline()
#     kmers = kmerFinder(12, sequence)
#     maximum = max(kmers.values())
#     print([x for x in kmers.keys() if kmers[x] == maximum])




