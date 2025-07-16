key = True
while key:
    for attempt in range(4):
        user = input("Coloque su username: ")
        password = input("Coloque su contraseña: ")
        if user == "nosoyadmin" and password == "4563":
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
                        beam = False
        key = False
    print("\n\nAcceso rechazado, vuelva más tarde")
    key = False
print("Gracias por usar el programa.")