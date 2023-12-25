import numpy as np
def divided_differences(a, matrix, k):#迭代求k阶差商
    fx = np.zeros(2 * len(matrix) - k)
    if k == 1:
        for i in range(len(matrix)):
            fx[2 * i]  = matrix[i, 2]
        for i in range(1, len(matrix)):
            fx[2 * i - 1] = (a[2 * i, 1] - a[2 * i - 1, 1]) / (a[2 * i, 0] - a[2 * i - 1, 0])
        return fx
    else:
        temp = divided_differences(a, matrix, k - 1)
        for i in range(2 * len(matrix) - k):
            fx[i] = (temp[i + 1] - temp[i]) / (a[i + k, 0] - a[i, 0])
        return fx
def Hermite_polynomial(matrix, x):
    a = np.zeros([2 * len(matrix), 2])
    for i in range(len(matrix)):
        a[2 * i, 0] = matrix[i, 0]
        a[2 * i + 1, 0] = matrix[i, 0]
        a[2 * i, 1] = matrix[i, 1]
        a[2 * i + 1, 1] = matrix[i, 1]
    Hx = matrix[0, 1]
    for i in range(1,2 * len(matrix) - 1):
        fx = divided_differences(a, matrix, i)
        temp = 1
        for j in range(i):
            temp *= (x - a[j, 0])
        Hx += fx[0] * temp
    return Hx
def main():
    matrix = np.array([[1.3, 0.6200860, -0.5220232], [1.6, 0.4554022, -0.5698959], [1.9, 0.2818186, -0.5811571]])
    print(Hermite_polynomial(matrix, 1.5))
main()