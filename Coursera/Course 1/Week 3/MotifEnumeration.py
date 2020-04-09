def kd_motifs(file_name):
    genome_sequence = []
    with open(file_name, 'r') as sequence_data:
        k, d = [int(x) for x in sequence_data.readline().split(' ')]
        genome_sequence = sequence_data.readlines()

    return find_motifs(k, d, genome_sequence)

# TODO Looking over the solution, ATT and ATA should be part of the solution. The way my current code works it to
#  make ATT the representative of ATA. It looks like I need to add not only the current kmer but its d-mismatch
#  counterparts to kmer_appearences
def find_motifs(k, d, sequences):
    """
    Given several sequences, scan through each storing each kmer and all of its d-mismatches. If the original kmer or
    any of its d-mismatches appear in all sequences, that kmer is said to be a (k,d)-motif.
    Example: Given k = 3 and d = 1 and the following sequences
        ACTA
        ACCG
        CCTC
    ACT is a (3,1)-motif. Since it appears in the first sequences. ACC (which is 1 nucleotide away from ACT) is in the
    2nd sequence. and CCT (which is also 1 nucleotide away from ACT) appears in the third

    :param k:
    :param d:
    :param sequences:
    :return:
    """
    from HammingDistance import hammingDist
    kmer_appearances = {}

    sequence_index = 0
    for sequence in sequences:
        for i in range(len(sequence) - k):
            current_kmer = sequence[i:i+k]

            kmer_has_representative = False
            for kmer in kmer_appearances:
                if hammingDist(kmer, current_kmer) <= d:
                    kmer_has_representative = True
                    if sequence_index not in kmer_appearances[kmer]:
                        kmer_appearances[kmer].append(sequence_index)
                    break

            if not kmer_has_representative:
                kmer_appearances[current_kmer] = [sequence_index]
        sequence_index = sequence_index + 1

    kd_motif = []
    for kmer in kmer_appearances:
        if len(kmer_appearances[kmer]) == len(sequences):
            kd_motif.append(kmer)

    return kd_motif


if __name__ == '__main__':
    motifs = kd_motifs('MotifEnumerationExample1.txt')
    print(motifs)
