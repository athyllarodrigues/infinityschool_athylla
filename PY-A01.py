
num_alunos = int(input("Digite a quantidade de alunos na turma: "))

soma_idades = 0

for i in range(num_alunos):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    soma_idades += idade

media_idade = soma_idades / num_alunos

print(f"A média de idade da turma é: {media_idade}")
