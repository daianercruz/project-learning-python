contatos = {
    "daiane@gmail.com": {"nome": "Daiane", "telefone": "3422-3333"},
}

copia = contatos.copy()
copia["daiane@gmail.com"] = {"nome": "dai"}

print(contatos["daiane@gmail.com"])

print(copia["daiane@gmail.com"])