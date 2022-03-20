# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print( "="*10, "Média dos bimestres", "="*10)

nota1 = int(input("Qual a primeira nota: "))
nota2 = int(input("Qual a segunda nota: "))
nota3 = int(input("Qual a terceira nota: "))
nota4 = int(input("Qual a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"\n --> A média das notas foi {media}")