#Exercicio: Idade
#Perguntar anos de nasc e ano atual, retonar idade e perguntar se deseja novo teste

executar = True
while executar :
    anoNacimento = int(input("Em que ano voce nasceu? "))
    anoAtual = int(input("Em que ano estamos? "))
    idade = anoAtual - anoNacimento
    print("Voce tem:" , idade , 'anos')
    pergunta = input("\n Deseja tentar novamente? \n [1]yes \n [2]no \n")
    if pergunta == "2":
        executar = False
print("----------------------------Segundo Exercicio Usando Funções--------------------------------")

def calcular_idade():
    anoNsc = int(input("Em que ano voce nasceu? "))
    anoAtl = int(input("Em que ano estamos? "))
    idade = anoAtl - anoNsc

    print("Voce tem " + str(idade) + " anos. " )

def perguntar_novamente() :
    opcao = input("Deseja testar novamente? Yes or No ")
    if opcao in "Yes" :
        iniciarprograma()
    else :
      print('Encerrando programa! Até mais ❤️')

def iniciarprograma() :
    calcular_idade()
    perguntar_novamente()

#Chamada incial
iniciarprograma()

