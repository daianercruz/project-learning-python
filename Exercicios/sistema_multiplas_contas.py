class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo):
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)

    def listar_contas(self):
        # Monta a saída desejada: "João: R$ 500, Maria: R$ 1000"
        contas_formatadas = [f"{conta.titular}: R$ {conta.saldo}" for conta in self.contas]
        print(", ".join(contas_formatadas))

# Criação da instância do SistemaBancario
sistema = SistemaBancario()

# Loop para ler as entradas do usuário
while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

# Listar todas as contas no formato desejado
sistema.listar_contas()
