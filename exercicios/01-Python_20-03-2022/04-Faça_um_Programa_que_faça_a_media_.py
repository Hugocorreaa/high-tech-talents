# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print( "="*10, "Média dos bimestres", "="*10)

nota1 = float(input("Qual a primeira nota: "))
nota2 = float(input("Qual a segunda nota: "))
nota3 = float(input("Qual a terceira nota: "))
nota4 = float(input("Qual a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"\n --> A média das notas foi {media}")