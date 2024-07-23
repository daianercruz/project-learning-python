carros = ["ferrari", "polo", "civic"]

for carro in carros:
    print(carro)

    for indice, carro in enumerate(carros):
        print(f"{indice}: {carro}")