#This file finds the most frequent k-mers of a specified length

def findkmers(lengths):
    with open("Vibrio Cholerae Ori.txt") as fp:
        from FrequentWords import kmerFinder
        sequence = fp.readline()

        for kmer_len in lengths:
            kmerFreq = kmerFinder(kmer_len, sequence)
            maximum = max(kmerFreq.values())

            print("The most frequent kmers of length {} are: ".format(kmer_len))
            print([x for x in kmerFreq.keys() if kmerFreq[x] == maximum])
            print("These kmers appear {} times\n".format(maximum))


findkmers([9])