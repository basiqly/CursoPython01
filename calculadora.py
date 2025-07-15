#Calculadora Básica em Python
def intro():
    return '''
  ___    __    __    ___  __  __  __      __   ____  _____  ____ 
 / __)  /__\  (  )  / __)(  )(  )(  )    /__\ (_  _)(  _  )(  _ \
( (__  /(__)\  )(__( (__  )(__)(  )(__  /(__)\  )(   )(_)(  )   /
 \___)(__)(__)(____)\___)(______)(____)(__)(__)(__) (_____)(_)\_)
'''
def mostrar_menu() :
    return '''
[1] ou [+] para
[2] ou [-] para
[3] ou [*] para
[4] ou [/] para
[5] ou [Sair] para
(ou digite sua opção: Somar / Subtrair / Multiplicar / Sair)
'''
#função que le os valores
def ler_valores() :
    valor01 = int(input("Insira o primeiro valor: "))
    valor02 = int(input('Insira o segundo valor: '))
    return valor01 , valor02

#funçoes de calculo
def somar(a , b) :
   return a + b
def subtrair(a , b) :
   return a - b
def multiplicar(a , b) :
   return a * b
def dividir(a , b) :
   return a / b

#função para permanecer ou sair do programa
def desejacontinuar() :
    print('''
        [1] Não, desejo sair!
        [2] Sim, desejo realizar outro calculo!
 ''')
    opcao = input('Deseja realizar outra conta?')
    return opcao != "1"

#Looping Principal
print(intro())
executar = True
while executar :
    print(mostrar_menu())
    operador = input('Qual a sua opção?: ').strip().lower()

    if operador in [ '5','sair'] :
        print('Obrigado por usar a melhor calculadora')
        break
    
    v01, v02 = ler_valores()

    if operador in ['1','+','somar'] :
        resultado = somar(v01, v02)   
    elif operador in ['2','-','subtrair'] :
        resultado = subtrair(v01, v02)
    elif operador in ['3','*','multiplicar'] :
        resultado = multiplicar(v01, v02)   
    elif operador in ['4','/','dividir'] :
        resultado = dividir(v01, v02)
    else:
        print('Opção invalida. Tente Novamente.')

    print("Resultado é " + str(resultado))
    executar = desejacontinuar()
