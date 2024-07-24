def contar_caracteres(string):
    # TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}


# TODO: Itere através de cada caractere na string string.
    for caractere in string:
        if caractere in contador: contador[caractere] += 1
        else: contador[caractere] = 1
    # TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)