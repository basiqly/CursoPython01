from random import randint
#Jogo da adivinhação

print('-----------------------------Iniciando o Jogo de Adivinhação-------------------------------')
aleatorio = randint(0,100)
chute = 0
chances = 10
while chute != aleatorio :
    chute = input('Chute um numero entre 1 a 100: ')
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == aleatorio:
            print('-----------------------')
            print('Congratulations winner!! The number was {} and you still had {} chances'.format(aleatorio,chances))
            print('-----------------------')
            break
        else :
            print('---------------')
            if chute > aleatorio :
                print('Voçê errou, Dica: É um numero menor')
            else:
                 print('Voçê errou, Dica: É um numero maior')
            print("Voçê ainda tem {} chances.".format(chances))
            print('-------')
        if chances == 0 :
             print('-------')
             print("GAME OVER!")
             print("Suas chances acabaram, voçê perdeu!")
             print('-------')
             break
print("---------GAME END----------")
