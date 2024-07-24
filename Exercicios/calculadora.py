print("\n ======================= CALCULADORA ======================")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("\n Selecione um númera para realizar uma operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\n ====> ")

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

if escolha == '1':
    print("\n")
    print(numero1, "+", numero2, "=", add(numero1,numero2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(numero1, "-", numero2, "=", subtract(numero1,numero2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(numero1, "*", numero2, "=", multiply(numero1,numero2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(numero1, "/", numero2, "=", divide(numero1,numero2))
    print("\n")

else:
    print("\n Opção Inválida!")