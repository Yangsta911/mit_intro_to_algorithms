

def get_damages(H):
    '''
    Input: H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    D = [1 for _ in H]
    H_tup = [(H[i], i) for i in range (len(H))]
    merge_sort(H_tup, D)
    return D

def merge_sort(A,D, a = 0, b = None):
    if b is None: b = len(A)
    if 1 < b - a:
        c = (a+b+1) // 2
        merge_sort(A, D, a, c)
        merge_sort(A,D, c, b)
        L, R = A[a:c], A[c:b]
        merge (L, R, A, len(L), len(R), a, b, D)

def merge(L, R, A, i, j, a, b, D):
    if a < b:
        if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
            D[L[i-1][1]] = D[L[i-1][1]] + j
            A[b-1] = L[i-1]
            i = i - 1
        else:
            A[b-1] = R[j-1]
            j = j - 1
        merge(L, R, A, i, j, a, b-1, D)



