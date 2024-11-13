#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média
notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:")
for i, nota in enumerate(notas):
    print(f"Nota {i + 1}: {nota}")

print(f"Média: {media:.2f}")