def conta_vogais(texto):

    #TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = set('aeiouAEIOU')
    
    #TODO: Inicialize um contador para contar as vogais:
    contador = 0 
  
    for char in texto:
        if char in vogais: 
         contador += 1

        #TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:

    return contador
# Solicitamos ao usuário que insira uma string
texto = input("Entre com sua palavra:")

# Chamamos a função conta_vogais e exibimos o resultado

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
