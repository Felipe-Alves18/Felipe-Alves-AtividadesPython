#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado
valor = input("Digite algo: ")
print("O tipo da variável é:", type(valor))
try:
    num = float(valor)
    quadrado = num ** 2
    print("O quadrado do número é:", quadrado)
except ValueError:
    print("O valor digitado não é numérico.")
    