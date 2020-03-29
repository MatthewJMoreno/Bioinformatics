def find_kd_motifs(file_name):
    with open(file_name, 'r') as sequence_data:
        k, d = [int(x) for x in sequence_data.readline().split(' ')]
        print(k)
        print(type(k))


if __name__ == '__main__':
    find_kd_motifs('MotifEnumerationExample1.txt')
