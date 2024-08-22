#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
# Crie um programa onde João informe: Cor, Modelo, Ano e Valor da bicicleta vendida.
# Uma bicicleta pode: Buzinar, parar e correr. Adicione esses comportamentos

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("plim..plim..plim")
    def parar(self):
        print("parando bicicleta")
        print("bicicleta parada")
    def correr(self):
        print("bicicleta correndo...")

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

#Outra forma de retornar os valores
#   def __str__(self):
#   return f" Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

b1 = Bicicleta("Verde", "caloi", 2002, 400)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2= Bicicleta("Amarela", "BX", "2019", "700")
b2.correr()
print(b2)
