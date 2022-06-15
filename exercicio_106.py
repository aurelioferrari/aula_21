# Criar um mini-sistema interactive help
# terminar o programa quando o usuário digitar fim

def inthelp():
    while True:
        nome = str(input('\033[1:31mDigite um comando:\033[m ')).strip().lower()
        while nome.isnumeric():
            nome = str(input('Digite um comando válido: ')).strip().lower()
        if nome in "FIMfim":
            break
        else:
            help(nome)

inthelp()