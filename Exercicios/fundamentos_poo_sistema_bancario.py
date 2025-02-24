class ContaBancaria:
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    def sacar(self, valor):
        if self.saldo >= abs(valor):  # Verifica se há saldo suficiente
            self.saldo -= abs(valor)
            self.operacoes.append(f"{valor}")
        else:
            self.operacoes.append(f"Saque não permitido")

    def extrato(self):
        # Exibe as operações no formato solicitado
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")

# Leitura do nome do titular e transações
nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

# Processa cada transação
for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

# Exibe o extrato
conta.extrato()
