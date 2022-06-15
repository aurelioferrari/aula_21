# criar função leiaint() que faz a verificação se a entrada digitada é um número

def leiaint():
    ok = False
    while True:
        n = str(input("Digite um número: "))
        if n.isnumeric():
            print(f'Você digitou o número {n}.')
            ok = True
        else:
            print('Você digitou um número inválido.')
        if ok == True:
            break



leiaint()