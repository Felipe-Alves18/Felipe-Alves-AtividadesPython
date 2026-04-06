#Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: ")) 
if num1 == num2:
    print("Os números são iguais.")
else:
    diferenca = abs(num1 - num2)
    print("Os números são diferentes. A diferença entre eles é:", diferenca)
    