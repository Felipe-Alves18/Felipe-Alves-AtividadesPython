#Receba a quantidade de horas trabalhadas e o valor da hora, calcule e imprima o salário do funcionário
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))
salario = horas_trabalhadas * valor_hora
print(f"O salário do funcionário é: R${salario:.2f}")