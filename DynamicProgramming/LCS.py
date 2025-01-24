# LCS stands for Longest Common Subsequence. What it finds is that, when two inputs strings are given
# the longest common substring among them is found, tricky part is that substring may not be continous
# For example ABCD, AED, the longest common substring is AD


def LCS(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]
    lcsString = [""] * (index+1)
    lcsString[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcsString[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return L[m][n], ''.join(lcsString)


X = "ABCDAF"
Y = "ACBCF"
lcs, lcsString = LCS(X, Y)

print("Length of Longest Common Subsequence between {} {} is {} and the string is {}".format(
    X, Y, str(lcs), lcsString))
