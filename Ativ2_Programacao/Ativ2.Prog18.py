#Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro
num = int(input("Digite um número: "))
if num > 0 and num % 2 == 0:
    print("Par positivo")
elif num < 0 and num % 2 == 0:
    print("Par negativo")
elif num > 0 and num % 2 != 0:
    print("Ímpar positivo")
elif num < 0 and num % 2 != 0:
    print("Ímpar negativo")
else:
    print("Neutro")
    