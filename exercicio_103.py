# função que receba o nome e numero de gols de um jogador
# mostrar a ficha mesmo que algum dado nao tenha sido informado

def ficha(nome='Nome não informado', gols=0):
    if gols == 1:
        print(f'O nome do jogador é {nome} e ele fez {gols} gol.')
    else:
        print(f'O nome do jogador é {nome} e o total de gols feitos é: {gols}.')


nome = str(input('Qual o nome do jogador? '))
if nome == '':
    nome = 'desconhecido'
gols = str(input('Quantos gols ele fez? '))
if gols.isnumeric():
    ficha(nome, gols)
else:
    gols = 0
    ficha(nome, gols)