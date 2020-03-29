def kmerFinder(k, sequence):
    """
    Given a kmer length k and a sequence, ACTTACT for example, scan through the sequence finding all kmers and keeping
    track of how many times each kmer appears.
    :param k:
    :param sequence:
    :return: A dictionary with unique kmers in the sequence as the key (type string) and the number of times it appears
    as its value (type int). The above sequence with k=3 will return {'ACT':2, 'CTT':1, 'TTA':1, 'TAC':1}
    """

    kmercount = {}
    for i in range(len(sequence) - k):
        if sequence[i:i+k] in kmercount:
            kmercount[sequence[i: i + k]] += 1
        else:
            kmercount[sequence[i: i + k]] = 1
    return kmercount