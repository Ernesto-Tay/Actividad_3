key = True
counter = 0
use = False
while key:
    if use:
        key = False
    counter +=1
    user = input("Coloque su username: ")
    password = input("Coloque su contraseña: ")
    if user == "nosoyadmin" and password == "4563":
        key = False
        beam = True
        while beam:
            print("\n\n-------------Menu--------------\n1. Calcular temperatura\n2. Calcular el área de un triángulo\n3. Salir")
            ops_man = input("Opción: ")
            match ops_man:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    use = True
                    beam = False
    elif counter == 4:
        print("\n\nAcceso rechazado, vuelva más tarde")
        key = False
print("Gracias por usar el programa.")