

def get_damages(H):
    '''
    Input: H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    D = [1 for _ in H]
    H_tup = [(H[i], i) for i in range (len(H))]
    def merge_sort(A, a = 0, b = None):
        if b is None: b = len(A)
        if 1 < b - a:
            c = (a+b+1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            L, R = A[a:c], A[c:b]
            merge (L, R, A, len(L), len(R), a, b)
    
    def merge(L, R, A, i, j, a, b):
        if a < b:
            if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
                A[b-1] = L[i-1]
                D = D[L[i-1][1]] + j
                i = i - 1
            else:
                A[b-1] = R[j-1]
                j = j - 1
            merge(L, R, A, i, j, a, b-1)
    merge_sort(H_tup)
    i = 0
    while (i < len(H_tup)):
        j = H_tup[i][1]
        D[j] = D[j] + i
        i = i + 1

    return D


H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
print(get_damages(H))
