'exercicio 1'

valor = input("Insira um numero entre 0 e 10: ")
while not valor.isnumeric():
    valor = input("Insira um numero entre 0 e 10: ")

valor = int(valor)

while valor < 0 or valor > 10:
    valor = int(input("Insira um numero entre 0 e 10: "))