def mensagem(nome):
    print("Executando nome")
    return f"Oi {nome}"

def mensagem_loga(nome):
        print('executando mensagem longa')
        return f"Oi tudo bem {nome}?"

def executar(funcao, nome):
    print("execudando o executar")
    return funcao(nome)

print(executar(mensagem, "Daiane"))
print(executar(mensagem_loga, "Daiane"))