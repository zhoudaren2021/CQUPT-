import numpy as np
import math
def Lagrange_polynomial_approximation(matrix, x):
    ak = np.ones(len(matrix))
    bk = np.ones(len(matrix))
    Lk = np.zeros(len(matrix))
    Px = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == i:
                continue
            else:
                ak[i] = ak[i] * (matrix[i][0] - matrix[j][0])
                bk[i] = bk[i] * (x - matrix[j][0])
        Lk[i] = bk[i] / ak[i]
        Px += Lk[i] *  matrix[i][1]
    return Px
def main():
    matrix = [[1, 0.1924], [1.05, 0.2414], [1.1, 0.2933], [1.15, 0.3492]]
    print("逼近值：" + Lagrange_polynomial_approximation(matrix, 1.09))
    print("误差界：" +  np.abs(Lagrange_polynomial_approximation(matrix, 1.09) - math.log10(math.tan(1.09))))
main()