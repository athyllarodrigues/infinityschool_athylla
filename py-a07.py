##a) Código para a função que calcula a média aritmética das notas:

def calcular_media(notas):
    if not notas:
        return None 
    soma = sum(notas)
    media = soma / len(notas)
    return media

##b) Código para o loop while que pede ao usuário que insira as notas dos alunos:

notas_alunos = []
continuar = True

while continuar:
    nota = float(input("Digite a nota do aluno (ou digite um valor negativo para encerrar): "))
    
    if nota < 0:
        continuar = False
    else:
        notas_alunos.append(nota)

##c) Código para o loop for que imprime a média de cada aluno:

for i, notas_aluno in enumerate(notas_alunos, start=1):
    media_aluno = calcular_media(notas_aluno)
    if media_aluno is not None:
        print(f"Média do Aluno {i}: {media_aluno:.2f}")
    else:
        print(f"Não há notas registradas para o Aluno {i}.")
