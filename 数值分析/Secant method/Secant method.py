import numpy as np
import math

def function(array, x, func=None):
    if func is None:
        # 默认情况下，使用多项式函数
        return polynomial_function(array, x)
    else:
        # 如果提供了 func 参数，则使用指定的函数
        return func(x)

def polynomial_function(array, x):
    sum = 0
    for i in range(len(array)):
        sum += array[i] * x ** i
    return sum

def cosine_function(x):
    return x - math.cos(x)

def main(array, x0, x1, func):
    a = np.zeros((100, 1))
    a[0] = x0
    a[1] = x1
    i = 1
    while True:
        a[i + 1] = a[i] - function(array, a[i], func) * (a[i] - a[i - 1]) / (function(array, a[i], func) - function(array, a[i - 1], func))
        if abs(a[i + 1] - a[i]) <= 1e-4:
            break
        i += 1
    print(a[i])

main(None, 0, 1.5, func = cosine_function)