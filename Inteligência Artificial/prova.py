numero_alunos=int(input("Digite o número de alunos :"))

soma_medias_turma = 0
for i in range(1,numero_alunos +1):
    print()
    print(f"Aluno {i} :")

    nome=input("Digite o nome de cada aluno :")
    nota1 =float(input("Digite a primeira nota:  "))
    nota2 =float(input("Digite a segunda nota:  "))
    nota3 =float(input("Digite a terceira nota: "))
        
    media =(nota1 + nota2 + nota3)/3
    soma_medias_turma += media

    if media >= 7 :
        indicacao = "Aprovado"
    else:
        indicacao = "Reprovado"
    
    print(f"Aluno: {nome}")
    print(f"Notas: {nota1:2f},{nota2:2f},{nota3:2f}")
    print(f"Média: {media:2f}")
    print(f"Condição:{indicacao}")

media_geral_turma = soma_medias_turma / numero_alunos
print(f"Média geral da turma:{media_geral_turma:2f}")
            

          