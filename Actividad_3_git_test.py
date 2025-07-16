key = True
counter = 0
use = True
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
                    temp_ops = int(input("\n"+"-"*5+"Conversor de temperaturas"+"-"*5+"\n1. Celsius a Farenheit\n2. Farenheit a Celsius\nOpción a elegir:"))
                    if temp_ops == 1:
                        while True:
                            try:
                                c_temp = int(input("Ingrese la temperatura en Celsius: "))
                                break
                            except:
                                print("Valor inválido. Ingresar solo números\n")
                        f_end_temp = (c_temp*1.8)+32
                        print(f"La temperatura en Farenheit es de {f_end_temp}°\n")

                    elif temp_ops == 2:
                        while True:
                            try:
                                f_temp = int(input("Ingrese la temperatura en Farenheit: "))
                                break
                            except:
                                print("Valor inválido, ingresar solo números\n")
                        c_end_temp = (f_temp - 32)/1.8
                        print(f"La temperatura en Celsius es de {c_end_temp}°\n")


                case "2":
                    pass
                case "3":
                    use = True
                    beam = False
    else:
        print("\nUsuario no reconocido.")
        if counter < 4:
            print("Vuelva a intentarlo.")

    if counter == 4:
        print("\n\nAcceso rechazado, vuelva más tarde")
        key = False
print("Gracias por usar el programa.")