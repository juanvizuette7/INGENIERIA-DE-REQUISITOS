class Calculadora:
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multiplicacion(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "No se puede dividir por cero"

if __name__ == "__main__":
    calculadora = Calculadora()

    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))

        resultado_suma = calculadora.suma(num1, num2)
        resultado_resta = calculadora.resta(num1, num2)
        resultado_multiplicacion = calculadora.multiplicacion(num1, num2)
        resultado_division = calculadora.division(num1, num2)

        print(f"Suma: {resultado_suma}")
        print(f"Resta: {resultado_resta}")
        print(f"Multiplicación: {resultado_multiplicacion}")
        print(f"División: {resultado_division}")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
