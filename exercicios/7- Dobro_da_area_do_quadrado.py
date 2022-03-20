# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print( "="*10, "Dobro da área de um quadrado", "="*10)

lado = int(input("Qual o lado do quadrado: "))

area = lado**2
dobro = area * 2

print(f"\n --> O dobro da área do quadrado é {dobro}")