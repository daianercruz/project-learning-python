def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([100, 30, 44]))  # 174
print(retorna_antecessor_e_sucessor(30))  # (29, 31)