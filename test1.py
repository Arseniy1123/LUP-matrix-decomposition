import numpy as np
from lup import lup_decomposition


A = np.array([[7.0, 2.0, 5.0],
              [1.0, 3.0, 3.0],
              [65.0, 21.0, 6.0]])
n = A.shape[0]
m = A.shape[1]
if n != m:
    print("Error: A non-square matrix is introduced. Please enter a square matrix!")
else:
    L, U, P = lup_decomposition(A)
    # Округление можно задать в параметре decimals. Сейчас оно составляет 3 знака после запятой
    print("L:\n", np.around(L, decimals=3))
    print("U:\n:", np.around(U, decimals=3))
    print("P:\n", P)
    # Проверка работы алгоритма: если произведения LU и PA получаются одинаковые, значит, функция работает верно
    if np.linalg.det(A) != 0.0 and A.shape[0] == A.shape[1]:
        k = L.dot(U)
        q = P.dot(A)
        print(q)
        print(k)
