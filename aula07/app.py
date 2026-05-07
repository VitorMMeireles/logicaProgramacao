'''
Manipulação de arquivos: percorrer os meus diretórios, encontrar o arquivo
passar o comando de abertura de arquivo, passar comando de ação.

arquivo = open("arquivo.txt" , "modo")

modos de ação:
   * -"r" : leitura de arquivo
   * -"w" : escrita(obs: sobrescreve o conteudo antigo)
   * -"a" : adiciona conteudo
    -"x" : cria um arquivo
    -"b" : arquivos binarios
    -"t" : texto
 '''

#criando e escrevendo arquivo
arquivo = open('primeiro_arquivo.txt' , 'w')
arquivo.write("Ola mundo! Meu primeiro arquivo")
arquivo.close()

#lendo arquivo
arquivo = open('primeiro_arquivo.txt' , 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica
with  open('primeiro_arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# arquivp com multiplas escritas
with open("alunos.txt" , "a") as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('Cintra\n')
    arquivo.write('Lucas\n')
    arquivo.write('Gomes\n')
    arquivo.write('Karython\n')

#lendo linha a linha 
with open("alunos.txt" , "r") as arquivo:
    for linha in arquivo:
        print(linha)

#usando lista para escrever um arquivo
frutas = ['pera', ' abacaxi ', 'manga', 'caju']

with open('frutas.txt' , 'w') as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

#converter o arquivo em lista
with open("frutas.txt" , 'r') as arquivo:
    linhas = arquivo.readlines()
    print(type(linhas))
    print(linhas)

# Saída ['pera\n', ' abacaxi \n', 'manga\n', 'caju\n']

#limpar qubra de linha 
with open("frutas.txt" ,'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# exemplo para cadstro
while True:
    nome = input("Digite seu nome: ").title()

    with open("cadastro.txt" , 'a') as arquivo:
        arquivo.write(nome +'\n')

    sair = input("Deseja sair do sistema? s/n").lower()

    if sair == 's':
        break

