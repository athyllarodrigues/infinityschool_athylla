pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

# a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.
idade_joao = pessoas["João"]
print("Idade de João:", idade_joao)

# b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.
pessoas["Ana"] = 31
print("Dicionário após adicionar Ana:", pessoas)

# c) Crie uma função chamada maior_idade que recebe um dicionário como argumento
#    e retorna o nome da pessoa com a maior idade.
def maior_idade(dic):
    pessoa_maior_idade = max(dic, key=dic.get)
    return pessoa_maior_idade

nome_maior_idade = maior_idade(pessoas)
print("Pessoa com maior idade:", nome_maior_idade)
