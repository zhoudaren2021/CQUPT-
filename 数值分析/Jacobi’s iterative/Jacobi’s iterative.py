import numpy as np

def convert_arrays(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != j and j != len(matrix[0]) - 1:
                matrix[i][j] = matrix[i][j] / (- matrix[i][i])
            elif j == len(matrix[0]) - 1:
                matrix[i][j] = matrix[i][j] / matrix[i][i]
                matrix[i][i] = 0
def multiply_matrices(matrix1, matrix2):
    temp = np.zeros((len(matrix2), 1))
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0]) - 1):
            temp[i] += matrix1[j] * matrix2[i][j]
    for i in range(len(matrix2)):
        matrix1[i] = temp[i] + matrix2[i][len(matrix2[0]) - 1]

def main():
    my_matrix = np.array([[10, -1, 2, 0, 6], [-1, 11, -1, 3, 25], [2, -1, 10, -1, -11], [0, 3, -1, 8, 15]], dtype = float)
    convert_arrays(my_matrix)
    x = np.zeros((15, len(my_matrix)))
    i = 0
    while True:
        if i == 0:
            multiply_matrices(x[i], my_matrix)
        else:
            x[i] = x[i - 1]
            multiply_matrices(x[i], my_matrix)
            if (max(np.abs(x[i] - x[i - 1]))) / (np.sqrt(np.sum(x[i]**2))) <= 10**(-3):
                break
        i = i + 1
    print(x[i])
    #print(max(np.abs(x[i] - x[i - 1])))
    #print(max(np.abs(x[i])))
    #print(np.sqrt(np.sum(x[i]**2)))

main()
