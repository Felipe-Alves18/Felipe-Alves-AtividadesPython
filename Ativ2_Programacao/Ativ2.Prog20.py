#Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, mostre o valor
valor = float(input("Digite um número: "))
if 0 <= valor <= 100:
    print("O número está dentro do intervalo.")
else:
    print("O número está fora do intervalo. O valor digitado foi:", valor)  