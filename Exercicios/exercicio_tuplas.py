#Desafio para entrada de números em uma tupla e retornar a soma desses números

def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input("Entre com uma sequencia de números:")

    elementos = (map(int, entrada.split()))

    resultado = soma_tupla(elementos)

    print(f"A soma dos elementos da tupla é: {resultado}")