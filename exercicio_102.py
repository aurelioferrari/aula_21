# função fatorial que receba 2 parâmetros: numero e show
# o numero a calcular o fatorial e o outro para decidir se vai ou nao mostrar o processo de calculo

def fatorial(numero, show):
    soma = 1
    if show == 1:
        for i in range(numero, 0, -1):
            soma *= i
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print('1 =', end=" ")
        print(f'{soma}')
    if show == 2:
        for i in range(numero, 0, -1):
            soma *= i
        print(f'O valor do fatorial é {soma}')

numero = int(input('Digite um número para calcular o fatorial: '))
show = int(input('Digite 1 para ver o cálculo.\nDigite 2 para ver apenas o resultado.'))
while show != 1 and show != 2:
    show = int(input('Digite 1 para ver o cálculo.\nDigite 2 para ver apenas o resultado.'))
fatorial(numero, show)


