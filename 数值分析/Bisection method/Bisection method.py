def function(array, x):
    sum = 0
    for i in range(len(array)):
        sum += array[i] * x ** i
    return sum

def main(array, a, b):
    while True:
        if b - a <= 10 ** (-4):
            print((b + a) / 2)
            break
        if function(array, a) * function(array, (b + a) / 2) < 0:
            b = (b + a) / 2
        else:
            a = (b + a) / 2

main([-10, 0, 4, 1], 1,2)
