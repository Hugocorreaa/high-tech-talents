# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print( "="*10, "Dobro da área de um quadrado", "="*10)

lado = float(input("Qual o lado do quadrado: "))

area = lado**2
dobro = area * 2

print(f"\n --> A área do quadrado é {area} e seu dobro é {dobro}")