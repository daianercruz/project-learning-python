class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes_formatadas(self):
        return f"Nome: {self.nome}, Idade: {self.idade} "


# Entrada do usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

# Criando uma instância da Pessoa
pessoa = Pessoa(nome, idade)

# Chamando o método para retornar as informações formatadas e imprimindo o resultado
print(pessoa.informacoes_formatadas())