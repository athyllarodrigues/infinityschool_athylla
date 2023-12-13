class Carro:
    def __init__(self, modelo, cor, ano, velocidade=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro {self.modelo} acelerou e agora está a {self.velocidade} km/h.")

    def frear(self, decremento):
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
            print(f"O carro {self.modelo} freou e agora está a {self.velocidade} km/h.")
        else:
            print("O carro já está parado.")

    def obter_informacoes(self):
        return f"Carro {self.modelo} - Ano {self.ano} - Cor {self.cor} - Velocidade {self.velocidade} km/h"


# Exemplo de uso da classe
carro1 = Carro(modelo="Fusca", cor="Azul", ano=1980)
print(carro1.obter_informacoes())

carro1.acelerar(30)
carro1.frear(10)

print(carro1.obter_informacoes())
