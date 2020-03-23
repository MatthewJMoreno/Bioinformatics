def computeKmerPermutations(actg, kmerPrefix, actgLen, kmerSize, ans):
    if (kmerSize == 0):
        ans.append(kmerPrefix)
        return

    for i in range(actgLen):
        newkmerPrefix = kmerPrefix + actg[i]
        computeKmerPermutations(actg, newkmerPrefix, actgLen, kmerSize - 1, ans)

ans = []
kmerSize = 3
computeKmerPermutations(['A','C','T','G'], '', 4, kmerSize, ans)
print('{}'.format(ans))
