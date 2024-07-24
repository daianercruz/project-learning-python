class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

        def latir(self):
            print("Auauau")

        def dormir(self):
            self.acordado = False
            print("zZzZzZz...")

cao_1 = Cachorro("Antonio", "Preto/branco", False)
cao_2 = Cachorro("Molly", "Preto/Amarelo")

cao_1.latir()
cao_2.dormir()
print(cao_2.acordado)