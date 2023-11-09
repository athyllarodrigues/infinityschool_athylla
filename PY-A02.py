
lista1 = input("Digite a primeira lista separada por espaços: ").split()
lista2 = input("Digite a segunda lista separada por espaços: ").split()
lista1 = [int(elemento) for elemento in lista1]
lista2 = [int(elemento) for elemento in lista2]
elementos_em_comum = set(lista1) & set(lista2)
soma_elementos = sum(elementos_em_comum)
resultado = (list(elementos_em_comum), soma_elementos)
print(f"Elementos em comum: {resultado[0]}")
print(f"Soma dos elementos em comum: {resultado[1]}")
