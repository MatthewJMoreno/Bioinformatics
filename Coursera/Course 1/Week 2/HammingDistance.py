def hammingDist(p,q):
    """
    :param p:A genetic sequence
    :param q:A genetic sequence
    :return: Number of nucleotides p differs from q.
        Example:
            p = ACT
            q = GCC
            hammingDist(p,q) = 2
    """
    distance = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

    return distance
