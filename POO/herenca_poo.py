class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregando):
        super().__init__(cor, placa, numero_rodas)
        self.carregando = carregando

    def esta_carregado(self):
        print(f"{'Sim' if self.carregando else 'Não'} estou carregado")


moto = motocicleta("preta", "xxxx", 2)


carro = carro("branco", "xxx", 4)


caminhao= caminhao("vermelho", "xxxx", 8, True)

print(carro, moto, caminhao)