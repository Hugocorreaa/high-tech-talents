# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print( "="*10, "Conversor de Celsius em Fahrenheit", "="*10)

tempC = int(input("Qual a temperatura em ºC: "))

tempF = tempC * 1.8 + 32

print(f"\n --> {tempC}ºC são {tempF}ºF")