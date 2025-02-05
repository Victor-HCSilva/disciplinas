class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

if __name__ == '__main__':
    calc = Calculadora()
    print(calc.soma(1, 2))
    print(calc.subtracao(1, 2))
    print(calc.multiplicacao(1, 2))
    print(calc.divisao(1, 2))