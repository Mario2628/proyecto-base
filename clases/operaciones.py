class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2: "))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def sumar(self):
        self.resultado = f"La suma de {self.num1} + {self.num2} es igual a {self.num1 + self.num2}"
    
    def restar(self):
        self.resultado = f"La resta de {self.num1} - {self.num2} es igual a {self.num1 - self.num2}"
    
    def multiplicar(self):
        self.resultado = f"La multiplicación de {self.num1} * {self.num2} es igual a {self.num1 * self.num2}"
    
    def dividir(self):
        if self.num2 != 0:
            self.resultado = f"La división de {self.num1} / {self.num2} es igual a {self.num1 / self.num2}"
        else:
            self.resultado = "No se puede dividir entre cero"
    
    def modulo(self):
        if self.num2 != 0:
            self.resultado = f"El módulo de {self.num1} % {self.num2} es igual a {self.num1 % self.num2}"
        else:
            self.resultado = "No se puede calcular el módulo con divisor cero"
    
    def mostrarResultado(self):
        print(self.resultado)


