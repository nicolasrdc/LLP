def fibonacci(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b 

T = int(input("Digite o número de casos de teste: "))

for _ in range(T):
    N = int(input("Digite o valor de N: "))
    print(f"Fib({N}) = {fibonacci(N)}")
