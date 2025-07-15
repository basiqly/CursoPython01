#Trabalhando com Loopings

palavra = "garrafinha" 
contador = 0
print("Palavra Escolhida: " , palavra)
for letra in palavra :
    print(contador, " " , letra)
    contador = contador + 1
print('------------')
cidades = ['São Paulo', 'Santa Fé do Sul', 'Londres', 'Três Lagoas', 'Manchester', 'Bristol'] 
for cidade in cidades :
    print(cidade) 
print('-------------')
print(cidades[2])

print("--------------While---------------")

botaoExecutar = True
contador = 0
while botaoExecutar :
    contador = contador + 1
    if contador >= 10 :
      botaoExecutar = False
print("fim da lista:")
print('-----------------------')

shoppingList = ['shirt', 'trousers', 'shoes', 'jacket', 'cardigan', 'skirt']
contador = 1
for List in shoppingList :
    print(contador, "-", List)
    contador = contador + 1
