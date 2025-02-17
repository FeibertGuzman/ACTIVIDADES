# Suma de dos numeros con variables fijas

num=5
num0=8

suma= num + num0

print("La suma es: ",suma)

print("Suma de dos numeros ingresdos por teclado")
# Solicitar los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la suma
resultado = num1+num2

# Muestra el resultaso 
print(f"La suma de {num1} + {num2} = {resultado}")

import platform
print("Versión de Python:", platform.python_version())
