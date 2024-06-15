
while True:
    print()
    print("///Elige Primero los Numeros para las Operaciones///")
    print("----------------------------------------------------")
    print()
    num1 = int(input("1er Numero: ")) 
    num2 = int(input("2do Numero: "))
     

    print()
    print("""Seleccione la operacion que desea
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- Dividir
            5- Salir 
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("La suma es", num1 + num2)
        
    elif valor == 2:
        print("La resta es", num1 - num2)
        
    elif valor == 3:
        print("La multiplicacion es", num1 * num2)
        
    elif valor == 4:
        print("La division es", num1 / num2)
        
    elif valor ==5:
        print("Saliendo del programa")
        break
    else:
        print("Opcion incorrecta, por favor intente de nuevo.")
