def lup_decomposition(A):
    n = A.nrows()
    U = A
    P = identity_matrix(n)
    L = identity_matrix(QQ, n)
    
    for i in range(n):
        p = 0
        ind = -1
        for row in range(i, n):
            if abs(A[row, i]) > p:
                p = abs(A[row, i])
                ind = row
                
        if p == 0:
            print('Матрица вырождена')
            return 0
        
        P[[i, ind]] = P[[ind, i]]
        U[[i, ind]] = U[[ind, i]]
        for j in range(i+1, n):
            U[j, i] /= U[i, i]
            for k in range(i+1, n):
                U[j, k] -= U[j, i] * U[i, k]
    
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i, j] = A[i, j]
                U[i, j] = 0
            else:
                U[i, j] = A[i, j]
                if i == j:
                    L[i, j] = 1
                else:
                    L[i, j] = 0
    
    return L, U, P


A = matrix(QQ, [[2.0, 0.0, 2.0, 0.6], [3.0, 3.0, 4.0, -2.0], [5.0, 5.0, 4.0, 2.0], [-1.0, -2.0, 3.4, -1.0]])
A1 = copy(A)
n = A1.nrows()
m = A1.ncols()
if n != m:
    print("Error: A non-square matrix is introduced. Please enter a square matrix!")
else:
    L, U, P = lup_decomposition(A1)
    print("L:")
    print(L)
    print()
    print("U:")
    print(U)
    print()
    print("P:")
    print(P)
    print()
    if A.det() != 0.0 and A.nrows() == A.ncols():
        k = L * U 
        q = P * A
        print('P * A:')
        print(q)
        print()
        print('L * U:')
        print(k)
        print()
