import time
import sys

def factorial(n):
    response = 1

    while n > 1:
        response = response * n
        n = n - 1

    return response


def factorial_recursive(n):
    if n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    n = 200000
    sys.setrecursionlimit(n + 10)

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f"Execturion time with bucle\t{final - comienzo}")

    comienzo = time.time()
    factorial_recursive(n)
    final = time.time()
    print(f"Execution time with recusive\t{final - comienzo}")