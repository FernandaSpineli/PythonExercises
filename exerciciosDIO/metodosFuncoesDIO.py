from re import A


class Calculadora:
    def __init__(self) -> None:
      pass     

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b
        
    def multiplicacao(self, a, b):
        return a * b
        
    def divisao(self, a, b):
         return a / b
    
"""  def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b
        
    def multiplicacao(self):
        return self.a * self.b
        
    def divisao(self):
         return self.a / self.b  """

# calculadora = Calculadora(10, 2)
calculadora = Calculadora()

print(calculadora.soma(10, 2))
print(calculadora.subtracao(7, 4))
print(calculadora.multiplicacao(3, 6))
print(calculadora.divisao(50, 5))
