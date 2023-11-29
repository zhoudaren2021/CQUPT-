import numpy as np

def gaussian_elimination(A, b):
    # 将输入转换为浮点数类型
    A = A.astype(float)
    b = b.astype(float)

    # 合并增广矩阵
    augmented_matrix = np.column_stack((A, b))

    # 行数和列数
    rows, cols = augmented_matrix.shape

    # 消去过程
    for i in range(rows):
        # 将当前列的对角元素缩放为1
        current_row = augmented_matrix[i, :]
        augmented_matrix[i, :] = current_row / current_row[i]

        # 将其他行的当前列元素消为0
        for j in range(i + 1, rows):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # 回代过程
    x = np.zeros(rows)
    for i in range(rows - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:cols-1], x[i+1:cols-1])

    return x

# 例子
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

result = gaussian_elimination(A, b)
print("解为:", result)
