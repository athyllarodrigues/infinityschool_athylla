# infinityschool_athylla
LP-A01
numero_inteiro = int(input("Digite um número inteiro: "))
print("Você digitou o número inteiro:", numero_inteiro)

numero_flutuante = float(input("Digite um número decimal: "))
print("Você digitou o número decimal:", numero_flutuante)

string = input("Digite uma mensagem: ")
print("Você digitou a mensagem:", string)

escolha = input("Digite 'True' ou 'False': ")
valor_booleano = escolha.lower() == 'true'
print("Você escolheu:", valor_booleano)

valores = input("Digite alguns valores separados por espaço: ")

tupla = tuple(valores.split())
print("Você digitou a tupla:", tupla)

nulo = None
print("Variável nula:", nulo)
