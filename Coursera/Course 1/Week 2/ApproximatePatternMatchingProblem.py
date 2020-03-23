def findApproxPattern(pattern, sequence, d):
    from HammingDistance import hammingDist
    indicies = []

    for i in range(len(sequence) - len(pattern) + 1):
        p = pattern
        q = sequence[i:i+len(pattern)]

        if hammingDist(p,q) <= d:
            indicies.append(i)

    return indicies


# with open('ApproximatePatternMatchCountExample.txt') as fp:
#     pattern = fp.readline().strip('\n')
#     sequnce = fp.readline().strip('\n')
#
#     d = int(fp.readline())
#
#     print(len(findApproxPattern(pattern, sequnce, d)))

print(*findApproxPattern('CCC', 'CATGCCATTCGCATTGTCCCAGTGA', 2))