                   #txt
## Abrindo o arquivo para escrita e adicionando conteúdo
#with open("meu_arquivo.txt", "w") as arquivo:
#    arquivo.write("Olá, Mundo!\n")
#    arquivo.write("Aprendemos Python\n")
#
## Abrindo o arquivo para leitura e exibindo o conteúdo
#with open("meu_arquivo.txt", "r") as arquivo:
#    texto = arquivo.read()
#    print(texto)
#
#________________________________________________________________________________
#import csv
#
#with open ("produto.csv","w", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["Nome","Preço"])
#    writer.writerow(["Livro","20"])
#
#with open("produto.csv","r") as arquivo:
#    texto = arquivo.read()
#    print(texto)

#_______________________________________________________________

#import json
#
#dicionario = {
#    "Nome": "Joao",
#    "Idade": "22",
#    "Profissao": "Engenheiro"
#}
#
#object_json = json.dumps(dicionario, indent=4)
#
#with open ("Dados.json", "w") as file:
#    file.write(object_json )
#    
#with open("Dados.json","r") as arquivo:
#    texto = arquivo.read()
#    print(texto)
#___________________________________________________________
#import pandas as pd
#
## Criando os dados para a planilha
#dados = {
#    'Produto': ['celular'],
#    'Quantidade': [10]
#}
#
## Criando um DataFrame com os dados
#df = pd.DataFrame(dados)
#
## Salvando o DataFrame em um arquivo Excel
#df.to_excel("vendas.xlsx", index=False)
#
#print("Arquivo 'vendas.xlsx' criado com sucesso.")
#
## Carregar o arquivo Excel
#df = pd.read_excel("vendas.xlsx")
#
## Exibir o conteúdo do arquivo
#print(df)
#_______________________________________________________________




         # EXERCICIO
#_______________________________________________________________

#1) Enunciado: Crie um arquivo de texto chamado "aula.txt" e escreva nele as 
# frases "Python é legal!" e "Aprendendo manipulação de arquivos".
# Abrindo o arquivo para escrita e adicionando conteúdo
#with open("meu_arquivo.txt", "w") as arquivo:
#    arquivo.write("Python é legal!\n")
#    
#
## Abrindo o arquivo para leitura e exibindo o conteúdo
#with open("meu_arquivo.txt", "r") as arquivo:
#    texto = arquivo.read()
#    print(texto)



#Crie um arquivo CSV com o nome "alunos.csv" e insira as informações de dois 
# alunos: João, 20 anos, e Maria, 22 anos.
#import csv
#
#with open ("alunos.csv","w", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["João","Maria"])
#    writer.writerow(["20 anos","22 anos"])
#
#with open("alunos.csv","r") as arquivo:
#    texto = arquivo.read()
#    print(texto)



#5) Crie um arquivo JSON chamado "info.json" 
#e insira informações de dois animais: um gato chamado Felix e um cachorro chamado Rex.
#import json
#
#dicionario = {
#    "Gato": "Felix",
#    "cachorro": "Rex",
#    
#}
#
#object_json = json.dumps(dicionario, indent=4)
#
#with open ("Dados.json", "w") as file:
#    file.write(object_json )
#    
#with open("Dados.json","r") as arquivo:
#    texto = arquivo.read()
#    print(texto)


#Crie um arquivo XML chamado "elementos.xml" 
# e insira informações de dois elementos químicos: Hidrogênio e Oxigênio.

#import xml.etree.ElementTree as ET
#
## Criando o elemento raiz "elementos"
#elementos = ET.Element("elementos")
#
## Criando e adicionando o elemento "hidrogenio"
#hidrogenio = ET.SubElement(elementos, "elemento")
#hidrogenio.set("nome", "Hidrogênio")
#hidrogenio.set("simbolo", "H")
#hidrogenio.set("numero_atomico", "1")
#
## Criando e adicionando o elemento "oxigenio"
#oxigenio = ET.SubElement(elementos, "elemento")
#oxigenio.set("nome", "Oxigênio")
#oxigenio.set("simbolo", "O")
#oxigenio.set("numero_atomico", "8")
#
## Criando a árvore XML
#tree = ET.ElementTree(elementos)
#
## Salvando o arquivo XML
#with open("elementos.xml", "wb") as xml_file:
#    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
#
#print("Arquivo 'elementos.xml' criado com sucesso.")
#
## Carregando o arquivo XML para leitura
#tree = ET.parse('elementos.xml')
#root = tree.getroot()
#
## Iterando sobre os elementos e imprimindo suas informações
#for elemento in root.findall('elemento'):
#    nome = elemento.get('nome')
#    simbolo = elemento.get('simbolo')
#    numero_atomico = elemento.get('numero_atomico')
#    
#    print(f"Elemento: {nome}")
#    print(f"  Símbolo: {simbolo}")
#    print(f"  Número Atômico: {numero_atomico}\n")
#




#______________________________________
#Utilizando a biblioteca Pandas, crie uma planilha do Excel
#chamada "notas.xlsx" e insira as notas de dois alunos nas disciplinas de Matemática e Português.
#import pandas as pd
#
## Criando os dados para as duas disciplinas
#dados = {
#    'Matematica': [10, 10],  
#    'Portugues': [10, 10]    
#}
#
#
#df = pd.DataFrame(dados, index=['Maria', 'João'])
#
#
#df.to_excel("notas.xlsx", index=True)
#
#print("Arquivo 'notas.xlsx' criado com sucesso.")
#
#
#df = pd.read_excel("notas.xlsx")
#
#print(df)
#

#Dado um conjunto de dados referente aos pedidos de compras de um e-commerce, armazenado em uma lista de 
#dicionários no Python, sua tarefa é gerar um arquivo .xls a partir desses dados. Utilize a biblioteca pandas 
#para realizar essa operação.
#import pandas as pd
#
#
#historico_pedidos = [
#    {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},
#    {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},
#    {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},
#    {'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}
#]
#
#df = pd.DataFrame(historico_pedidos)
#
#df.to_excel("arquivo.xlsx", index=False)
#
#print("Arquivo criado com sucesso.")
#
#df = pd.read_excel("arquivo.xlsx")
#
#print(df)

#Dado um arquivo .xls contendo dados referentes aos pedidos de compras de um e-commerce (arquivo gerado no desafio 1), sua tarefa é ler esse arquivo e converter 
#seu conteúdo em um novo arquivo no formato .csv. Utilize a biblioteca pandas.

#import pandas as pd
#
#df = pd.read_excel("arquivo.xlsx")
#
#df.to_csv("arquivo.csv", index=False)
#
#print("Arquivo 'arquivo.csv' criado com sucesso.")

# Dado um arquivo .csv que contém dados referentes aos pedidos de compras de um e-commerce (arquivo gerado no desafio 2), 
# sua tarefa é ler esse arquivo e converter seu conteúdo em um novo arquivo no formato .json. Utilize a biblioteca pandas para realizar essa operação.
#import pandas as pd
#
## Lendo o arquivo .csv
#df = pd.read_csv("arquivo.csv")
#
## Salvando o DataFrame em um arquivo .json
#df.to_json("arquivo.json", orient="records", indent=4)
#
#print("Arquivo 'arquivo.json' criado com sucesso.")
#
#
#

def descriptografar_cifra_cesar(texto, deslocamento):
    texto_descriptografado = ""
    for caractere in texto:
        # Verifica se o caractere é uma letra maiúscula
        if 'A' <= caractere <= 'Z':
            texto_descriptografado += chr((ord(caractere) - ord('A') - deslocamento) % 26 + ord('A'))
        # Verifica se o caractere é uma letra minúscula
        elif 'a' <= caractere <= 'z':
            texto_descriptografado += chr((ord(caractere) - ord('a') - deslocamento) % 26 + ord('a'))
        else:
            # Mantém caracteres não alfabéticos inalterados
            texto_descriptografado += caractere
    return texto_descriptografado

# Pedindo a palavra ou frase criptografada para o usuário
mensagem_criptografada = input("Digite a mensagem criptografada: ")

# Definindo o deslocamento
deslocamento = 3

# Descriptografando a mensagem
mensagem_original = descriptografar_cifra_cesar(mensagem_criptografada, deslocamento)

# Exibindo o texto descriptografado
print("Mensagem original:")
print(mensagem_original)
