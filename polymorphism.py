#trabalhando com orientação e polymorphism

class Animal:
    def fazer_som(self) :
        
        pass
class Cachorro(Animal) :
    def fazer_som(self):
        return "Woof Woof"

class Gato(Animal) :
    def fazer_som(self):
        return "Meow"
    
#Usando o polimorfismo
def fazer_animal_falar(animal: Animal) :
        print(animal.fazer_som())

 #Criando os objetos
cachorro = Cachorro()
gato = Gato()
    

#Chamando o metodo de cada animal de forma polimorphism
fazer_animal_falar(cachorro)    
fazer_animal_falar(gato)
