def findMinSkew(sequence):
    skew = []
    tick = 0

    for i in range(len(sequence)):
        if sequence[i] == 'C':
            tick += -1
            skew.append(tick)
        elif sequence[i] == 'G':
            tick += 1
            skew.append(tick)
        else:
            skew.append(tick)

    #print(skew)

    #minSkew = min(skew)
    maxSkew = max(skew)

    #return skew

    return [i+1 for i,x in enumerate(skew) if x == maxSkew]

# with open('Escherichia Coli Genome.txt') as fp:
#     data = findMinSkew(fp.readline())
#     print(data)
#
#
#     import matplotlib.pyplot as plt
#
#     plt.plot(data)
#     plt.xlabel('Index')
#     plt.ylabel('Skew')
#     plt.show()


print(findMinSkew('GCATACACTTCCCAGTAGGTACTG'))