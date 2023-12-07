import numpy as np

def numerical_derivative(function, array, x, h=1e-5):
    return (function(array, x + h) - function(array, x - h)) / (2 * h)

def function(array, x):
    sum = 0
    for i in range(len(array)):
        sum += array[i] * x ** i
    return sum

def main(array, p):
    a = np.zeros((100, 1))
    a[0] = p
    i = 0
    while True:
        a[i + 1] = a[i] - function(array, a[i]) / numerical_derivative(function, array, a[i])
        if abs(a[i + 1] - a[i]) <= 1e-4:
            break
        i += 1
    print(a[i])

main([-10, 0, 4, 1], 1.5)
