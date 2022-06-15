def fatorial(num=1):
    res = 1
    n = num
    for i in range(1, n+1):
        res = res * i
    return res

f1 = fatorial(5)
f2 = fatorial(3)

soma = f1 + f2
print(f'A soma dos fatoriais é {soma}')