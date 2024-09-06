
arquivo = open("D:\daian\Documentos\Projeto Python\project-learning-python\Manipulando Arquivos\Arquivos\Arquivos.txt", "r")
print(arquivo.read())
arquivo.close()

arquivo = open("D:\daian\Documentos\Projeto Python\project-learning-python\Manipulando Arquivos\Arquivos\Arquivos.txt", "r")
print(arquivo.readline())
arquivo.close()

arquivo = open("D:\daian\Documentos\Projeto Python\project-learning-python\Manipulando Arquivos\Arquivos\Arquivos.txt", "r")

while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()