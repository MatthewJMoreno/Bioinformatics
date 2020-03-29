def kd_motifs(file_name):
    genome_sequence = []
    with open(file_name, 'r') as sequence_data:
        k, d = [int(x) for x in sequence_data.readline().split(' ')]
        genome_sequence = sequence_data.readlines()

    return find_motifs(k, d, genome_sequence)


def find_motifs(k, d, sequences):
    from FrequentWords import kmerFinder

    for sequence in sequences:
        print(kmerFinder(k, sequence))

    return []


if __name__ == '__main__':
    motifs = kd_motifs('MotifEnumerationExample1.txt')
