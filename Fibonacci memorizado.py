from functools import lru_cache


@lru_cache(maxsize=50000)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    try:
        return fibonacci(n - 1) + fibonacci(n - 2)
    except RecursionError:
        print(f'Erro de recursão para n = {n}')
        exit(1)


print(fibonacci(500))
