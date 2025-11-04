alunos = []

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    alunos.append((nome, nota))

maior_aluno = alunos[0]

for aluno in alunos:
    if aluno[1] > maior_aluno[1]:
        maior_aluno = aluno

print(f"\nO aluno com a maior nota é {maior_aluno[0]}, com nota {maior_aluno[1]}")