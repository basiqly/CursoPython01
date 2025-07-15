#Entendendo funções em Python

def minhaFuncao() :
    print("Olá Mundo")

minhaFuncao()
minhaFuncao()
minhaFuncao()
minhaFuncao()

alunos =["Jesreel", "Eloara", "Emily", "Alice", "Andressa", "Davi"]
cursos = ['Python','PHP','SQL']

#Trabalhando com variaveis de função
def minhaFuncaoMelhorada(animal, primaveras):
    print('Voce gosta de ', animal, 'e ele tem' , primaveras , 'anos')

petCliente = input('Qual seu animal preferido? ')
idadePet = input("Qual a idade do seu" + petCliente)
minhaFuncaoMelhorada(petCliente, idadePet)
minhaFuncaoMelhorada('iguana' , '4')


anoNacimento = int(input("Em que ano voce nasceu? "))
anoAtual = int(input("Em que ano estamos? "))
idade = anoAtual - anoNacimento
print("Voce tem:" , idade)
