def hammingDist(p,q):
    distance = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

    return distance


# with open('HammingDistanceExample.txt') as fp:
#     p, q = fp.readline(), fp.readline()
#     print(hammingDist(p,q))

print(hammingDist('CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA', 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'))
