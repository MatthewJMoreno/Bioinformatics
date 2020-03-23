def patternMatch(pattern, genome):
    indicies = []
    pointer = 0

    while True:
        index = genome.find(pattern, pointer)

        if index >= 0:
            indicies.append(str(index))
            pointer = index + 1
        else:
            break

    return indicies


print(patternMatch('AA', 'AAACATAGGATCAAC'))

# with open('Thermotoga Petrophila Ori.txt') as fp:
#     genome = fp.readline()
#     pattern = 'ATGATCAAG'
#     print(' '.join(patternMatch(pattern, genome)))
