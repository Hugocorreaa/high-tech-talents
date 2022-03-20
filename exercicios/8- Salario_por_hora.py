# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print( "="*10, "Cálculo do salário por hora", "="*10)

valorPorHora = int(input("Quando você ganha por hora: R$"))
horasTrabalhadas = int(input("Quantas horas você trabalha no mês: "))

salario = valorPorHora * horasTrabalhadas

print(f"\n --> Seu salário será R${salario}")