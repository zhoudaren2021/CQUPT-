import numpy as np
from sympy import symbols
def divided_differences(matrix, k):#迭代求k阶差商
    fx = np.zeros(len(matrix) - k)
    if k == 0:
        fx = matrix[:, 1]
        return fx
    else:
        temp = divided_differences(matrix, k - 1)
        for i in range(len(matrix) - k):
            fx[i] = (temp[i + 1] - temp[i]) / (matrix[i + k][0] - matrix[i][0])
        return fx
def newton_interpolation(matrix):
    x = symbols('x')
    Px = matrix[0, 1]
    for i in range(1,len(matrix)):
        fx = divided_differences(matrix, i)
        temp = 1
        for j in range(len(matrix[0]) - 1):
            temp *= (x - matrix[j, 0])
        Px += fx[0] *  temp
    return Px
def main():
    matrix = np.array([[1.0, 0.7651977], [1.3, 0.6200860], [1.6, 0.4554022], [1.9, 0.2818186], [2.2, 0.1103623]])
    print(newton_interpolation(matrix))
main()