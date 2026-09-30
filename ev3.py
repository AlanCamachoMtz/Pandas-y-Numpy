def sumar():
    Num1=float(input("Ingresa primer numero: "))
    Num2=float(input("Ingresa segundo numero: "))
    R = Num1 + Num2
    print(f"El Resultado es {R}.")
    return R

def restar():
    Num1=float(input("Ingresa primer numero: "))
    Num2=float(input("Ingresa segundo numero: "))
    R = Num1 - Num2
    print(f"El Resultado es {R}.")
    return R

def multiplicar():
    Num1=float(input("Ingresa primer numero: "))
    Num2=float(input("Ingresa segundo numero: "))
    R = Num1 * Num2
    print(f"El Resultado es {R}.")
    return R

def dividir():
    Num1=float(input("Ingresa primer numero: "))
    Num2=float(input("Ingresa segundo numero: "))
    R = Num1 / Num2
    print(f"El Resultado es {R}.")
    return R

def menu():
    while True:
        print("Ingresa una opcion: ")
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        print("4- Division")
        print("5- Salir")
        op = int(input())
 
        if op == 1:
            sumar()
        elif op == 2:
            restar()
        elif op == 3:
            multiplicar()
        elif op == 4:
            dividir()
        elif op == 5:
            break

menu()