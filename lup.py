import numpy as np


def lup_decomposition(A):
    # Проверка определителя матрицы A на равенство нулю
    if np.linalg.det(A) == 0.0:
        print("Error: A singular matrix is introduced. Please, enter a non-singular matrix!")
        return 0, 0, 0
    else:
        n = A.shape[0]
        # Создание начальных матриц P и L с единичной диагональю
        P = np.eye(n)
        L = np.eye(n)
        # Создание матрицы U как копии матрицы A
        U = A.copy()
        for i in range(n):
            # Нахождение максимального элемента в i-ом столбце
            max_idx = np.argmax(np.abs(U[i:, i])) + i
            # Если максимальный элемент не находится на диагонали, нужно поменять местами строки
            if max_idx != i:
                U[[i, max_idx]] = U[[max_idx, i]]
                P[[i, max_idx]] = P[[max_idx, i]]
                if i > 0:
                    L[[i, max_idx], :i] = L[[max_idx, i], :i]
            # Вычисление множителя
            for j in range(i+1, n):
                L[j, i] = U[j, i] / U[i, i]
                U[j, i:] -= L[j, i] * U[i, i:]
        return L, U, P
