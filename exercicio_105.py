# fazer função notas() que recebe notas de alunos
#o dicionário precisa ter:
# A Quantidade de notas
# A maior nota
# a menor nota
# a média da turma
# a situação


aluno = {}
lista = []
def notas(*nota, sit=False):
    aluno['tnotas'] = len(nota)
    aluno['maior'] = max(nota)
    aluno['menor'] = min(nota)
    aluno['media'] = sum(nota) / len(nota)
    if sit:
        if aluno['media'] > 6:
            aluno['situação'] = 'Aprovado'
        else:
            aluno['situação'] = "Reprovado"


notas(3, 4, 9, 9, 9, sit=True)
print(aluno)



