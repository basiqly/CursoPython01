#Função de soma
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
      raise ValueError("Não é possivel dividir por zero")
    return a / b