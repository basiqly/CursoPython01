#Importar o modulo unittest que nos permite escrever teste automatizados
import unittest

#importar as funções de teste
from test_unitario import somar, subtrair, multiplicar, dividir

#criar a classe que contem os teste unitarios para as funções de operação
class TesteOperacoes(unittest.TestCase):
    #testar a função de soma
    def testar_soma(self):
        #verificar se a soma de 2 e 3 é igual a 5
        self.assertEqual(somar(2,3),5)
        #verificar se a soma de -1 e 1 é igual a 0
        self.assertEqual(somar(-1,1),0)
         #verificar se a soma de -2 e -3 é igual a -5
        self.assertEqual(somar(-2,-3),-5)

    def testar_divisao(self):
        self.assertEqual(dividir(6,2), 3)
        self.assertEqual(dividir(-6,3), -2)
        self.assertEqual(dividir(-6,2), -3)
        with self.assertRaises(ValueError):
            dividir(1, 0) 
            #vai dar erro quando realizar o teste, pois não é possivel dividir por 0

    def testar_multiplicacao(self):
        self.assertEqual(multiplicar(5,2), 10)
        self.assertEqual(multiplicar(-5,10), -25)
        self.assertEqual(multiplicar(-5,-3), 15)
       
           

    def testar_subtracao(self):
        self.assertEqual(subtrair(-9,2), -11)
        self.assertEqual(subtrair(-9,-5), -14)
        self.assertEqual(subtrair(-7,-2), -9)
       
           



#permite que os testes sejam executados quando rodamos o arquivo diretamente
if __name__ == '__main__':
    unittest.main() #executa todos os teste definidos na classe
    