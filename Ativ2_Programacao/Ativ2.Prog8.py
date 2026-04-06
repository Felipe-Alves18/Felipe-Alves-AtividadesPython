#Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe "Número inválido"
num = float(input("Digite um número: "))
if num >= 0:
    raiz = num **0.5
    print("A raiz aproximada do número é:", raiz)
else:
    print("Número inválido")
    