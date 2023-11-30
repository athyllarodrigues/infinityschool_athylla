def calcular_media(lista):
    if not lista:
        return None 

    soma = sum(lista)
    media = soma / len(lista)
    return media


numeros = [10, 15, 20, 25, 30]
media_resultado = calcular_media(numeros)

if media_resultado is not None:
    print(f"A média dos números é: {media_resultado}")
else:
    print("A lista está vazia.")
