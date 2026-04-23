"""
Desenvolva um sistema que receba do usuário 
seu nome, data de nascimento, peso e altura.
Formate a saída para aparecer na tela do usuario:
Olá(nome_informado), seja bem vindo ao sistema Python,
Aqui estão as suas informações:
    Data de nascimento:
    Altura:
    Peso:
"""

nome = str(input("Digite seu nome:"))
dataNasc = str(input("Digite sua data de nascimento:"))
# a função input é naturalmente string portanto não precisa declarar como str(input())
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

print("Olá,",nome,"seja bem vindo ao sistema Python,aqui estão as suas informações:")
print("Você nasceu no dia: ",dataNasc)
print("Você tem,",altura,"m de altura")
print("Seu peso é: ",peso)

print(type(nome))
#mesmo sem o str, o input sai como string

