# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print( "="*10, "Conversor de Fahrenheit em Celsius", "="*10)

tempF = int(input("Qual a temperatura em ºF: "))

tempC = 5 * ((tempF -32)/9)

print(f"\n --> {tempF}ºF são {tempC}ºC")