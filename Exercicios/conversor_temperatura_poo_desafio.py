class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

# Entrada do usuário
celsius = float(input())

# Criando uma instância do conversor
conversor = ConversorTemperatura()

# Realizando a conversão e imprimindo o resultado
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(f"{fahrenheit}")