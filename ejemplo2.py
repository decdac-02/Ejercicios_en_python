#calcular el area de un circulo

def calcular_area (radio):
    return 3.1416*(radio*radio)

print("Dime el valor del radio: ")
radio = float(input())
area = calcular_area(radio)
print(area)

def mostrar (numero):
    if numero == 0:
        return
    print(numero)
    mostrar (numero - 1)

mostrar(8)