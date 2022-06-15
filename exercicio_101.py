from datetime import date

def voto():
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    return idade

def obrigacao():
    global idade
    if idade < 16:
        print('Você não pode votar.')
    if idade >= 16 and idade < 18 or idade > 65:
        print('Voto opcional.')
    if idade >= 18 and idade < 65:
        print('Voto obrigatório.')


idade = voto()
obrigacao()





