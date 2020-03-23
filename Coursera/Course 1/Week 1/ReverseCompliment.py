def revComp(sequence):
    compliment = ''
    for i in range(len(sequence)):
        if sequence[i:i+1] == 'A':
            compliment = compliment + 'T'
        elif sequence[i:i+1] == 'T':
            compliment = compliment + 'A'
        elif sequence[i:i+1] == 'G':
            compliment = compliment + 'C'
        else:
            compliment = compliment + 'G'

    return compliment[::-1]



print(revComp('TTGTGTC'))