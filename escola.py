#Trabalhando com IF e testes
tipoEscola = input("Tipo do Colegio: /n [1] - Publico \n [2] - Particular")
freqAluno = input("Qual a frequência do aluno?")
nomeAluno = input("Qual o nome do aluno: ")
mediaAluno = int(input(" Qual a media do aluno: "))

#mediaEscola = input("Media de corte da Escola") 
mediaEscola = 7
freqAluno= int(freqAluno)



'''
!= Diferente
==Igual
<= Menor ou Igual
>= Maior ou Igual
> Maior
< Menor
'''
if tipoEscola == "2":
    print("-----Coleégio Particular-----")
    if mediaAluno >= mediaEscola and freqAluno >= 70 :
        print("Aprovado")
    else:
        print('Reprovado')
        
if tipoEscola == "1" :
    print("-----Coleégio Particular-----")
    if mediaAluno >= mediaEscola or freqAluno >= 60 :
        print("Aprovado")
    else :
        print("Reprovado")
    