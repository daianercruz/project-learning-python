contatos = {
    "daiane@gmail.com": {"nome": "Daiane", "telefone": "3422-3333"},
    "byanka@gmail.com": {"nome": "Byanka", "telefone": "4324-3333"},
    "antonio@gmail.com": {"nome": "Antonio", "telefone": "6565-3333"},
    "betania@gmail.com": {"nome": "Betania", "telefone": "2313-3333"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)