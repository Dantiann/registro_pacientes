# Muestra un menú con las opciones disponibles para el aplicativo.
def menu(): 

    # Imprime un banner decorativo
    print("  ")
    print("***************************************")
    print("*¡Aplicativo de registro de pacientes!*")
    print("***************************************")
    print(" ")

    # Muestra las opciones del menú
    print("Digita el número de acuerdo a tu consulta:")
    print(" 1. Agregar paciente\n", "2. Mostrar pacientes\n", "3. Mostrar paciente(s) por grupo sanguíneo y Rh\n", "4. Mostrar la compatibilidad sanguínea\n", "5. Salir")
    print(" ")


# Función para agregar un nuevo paciente al diccionario
def agregar_paciente(diccionario):

    # Solicita el nombre del paciente
    nombre = input("Ingresa el nombre del paciente: ").title()

    # Valida que el nombre solo contenga letras
    while not nombre.replace(" ", "").isalpha():
        print('"Por favor, ingresa solo letras para tu nombre."')
        nombre = input("Ingresa el nombre del paciente: ").title()

    # Solicita la edad del paciente
    while True:
        try: 
            edad = int(input("Ingresa la edad del paciente: "))
            break 
        except ValueError:
            print('"Por favor, ingresa solo números para la edad"')

    # Solicita la ciudad del paciente
    ciudad = input("Ingresa la ciudad del paciente: ").title()

    # Solicita el número de teléfono del paciente
    telefono = input("Ingresa el número telefónico: ")
    while not telefono.isdigit():
        print('"Por favor, ingresa solo números para tu telefóno"') 
        telefono = input("Ingresa el número telefónico: ")

    # Solicita el grupo sanguíneo y Rh del paciente
    aboRh = input("Ingresa el grupo sanguíneo y Rh del paciente: ").upper()
    while aboRh not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-','O+','O-']:
        print('"Grupo sanguíneo y Rh no existentes. Intenta de nuevo"')
        aboRh = input("Ingresa el grupo sanguíneo y Rh del paciente: ").title()

    # Agrega el paciente al diccionario
    diccionario[nombre] = {"edad": edad, "ciudad": ciudad, "telefono": telefono,"aboRh": aboRh}


# Función para mostrar la información de todos los pacientes
def mostrar_paciente(diccionario):

    # Contador para enumerar los pacientes
    contador = 1

    # Recorre el diccionario e imprime la información de cada paciente
    for nombre, informacion in diccionario.items():
        print(f"{contador}.")
        print("Nombre:", nombre)
        print("Edad:", informacion["edad"])
        print("Ciudad:", informacion["ciudad"])
        print("Teléfono:", informacion["telefono"])
        print("Grupo sanguíneo y Rh:", informacion["aboRh"])
        print("")
        contador += 1


# Función para filtrar pacientes por tipo de sangre
def filtrar_por_tipo_sangre(diccionario, tipo_sangre):

    # Convierte el tipo de sangre a minúsculas
    tipo_sangre = tipo_sangre.lower()

    # Diccionario para almacenar los pacientes que coincidan con el tipo de sangre
    pacientes_tipo_sangre = {}

    # Recorre el diccionario e imprime la información de cada paciente
    for nombre, info in diccionario.items():
        # Compara el tipo de sangre del paciente con el tipo de sangre especificado
        if info['aboRh'].lower() == tipo_sangre:
            # Agrega el paciente al diccionario de pacientes con el tipo de sangre especificado
            pacientes_tipo_sangre[nombre] = info

    # Retorna el diccionario con los pacientes filtrados
    return pacientes_tipo_sangre


# Función para mostrar la tabla de compatibilidad sanguínea
def mostrar_compatibilidad():
    # Imprime encabezado de la tabla

    print("TIPO DE SANGRE", "  | ", " PUEDE RECIBIR DE")
    print("--------------", "     ----------------")
    print("     A+", "O+, O-, A+, A-", sep=" " * 14)
    print("     A-", "O-, A-", sep=" " * 14)
    print("     B+", "O+, O-, B+, B-", sep=" " * 14)
    print("     B-", "O-, B-", sep=" " * 14)
    print("     AB+", "TODOS", sep=" " * 13)
    print("     AB-", "AB-, O-, A-, B-", sep=" " * 13)
    print("     O+", "O+, O-", sep=" " * 14)
    print("     O-", "O-", sep=" " * 14)

    
def main():
    # Diccionario para almacenar información de los pacientes.
    # Cada clave es el nombre del paciente y el valor es otro diccionario con detalles del paciente.
    paciente = {
        'Carlos Patiño Diaz': {'edad': 42, 'ciudad': 'Bogotá', 'telefono': 3124083232, 'aboRh': 'A+'},
        'Diana Patiño Ortiz': {'edad': 39, 'ciudad': 'Cali', 'telefono': 3124082121, 'aboRh': 'A-'},
        'Lorena Castillo': {'edad': 19, 'ciudad': 'Bucaramanga', 'telefono': 3004083232,'aboRh': 'B+'},
        'Andrea Ayala Rico': {'edad': 48, 'ciudad': 'Bucaramanga', 'telefono': 3122213232, 'aboRh': 'B-'},
        'Teodolindo Bustamante': {'edad': 12 , 'ciudad': 'Curitiba', 'telefono': 3114003232,'aboRh': 'AB+'},
        'Francisca Tarduz': {'edad': 32 , 'ciudad': 'Quibdo', 'telefono': 3004083232, 'aboRh': 'AB-'},
        'Hector Castillo': {'edad': 20, 'ciudad': 'Caqueza', 'telefono': 3124081515,'aboRh': 'O+'},
        'Lola Sanchez': {'edad': 50, 'ciudad': 'Marquetalia', 'telefono': 3114033232, 'aboRh': 'O-'},
        'Catalina Chavez': {'edad': 35, 'ciudad': 'Zipaquira', 'telefono': 3123212112,'aboRh': 'O+'},
        'Jairo Ruiz': {'edad': 15, 'ciudad': 'Sopo', 'telefono': 3099993211, 'aboRh': 'O+'}
    }

    # Bucle infinito para mostrar el menú y permitir al usuario realizar acciones.
    while True:
        # Llama a la función menu() para mostrar las opciones al usuario.
        menu()

        # Solicita al usuario que ingrese una opción.
        opcion = input("Opción N°: ")

        # Comprueba la opción ingresada y ejecuta la acción correspondiente.
        if opcion == "1":
            print("Datos del paciente\n")
            # Llama a la función agregar_paciente() para agregar un nuevo paciente.
            agregar_paciente(paciente)
        elif opcion == "2":
            print("Lista de pacientes:\n")
            # Llama a la función mostrar_paciente() para mostrar la lista de pacientes.
            mostrar_paciente(paciente)
        elif opcion == "3":
            # Solicita al usuario que ingrese un tipo de sangre para filtrar.
            tipo_sangre = input("Ingresa el grupo sanguíneo y Rh a filtrar: ")
            # Llama a la función filtrar_por_tipo_sangre() para obtener una lista de pacientes que coincidan con el tipo de sangre ingresado.
            pacientes_tipo_sangre = filtrar_por_tipo_sangre(paciente, tipo_sangre)
            print("\nPacientes con tipo de sangre", tipo_sangre + ":\n")
            # Muestra la lista de pacientes filtrados o un mensaje si no se encontraron pacientes.
            if pacientes_tipo_sangre:
                mostrar_paciente(pacientes_tipo_sangre)
            else:
                print("--------------------------------------------------------")
                print("| ¡No se encontraron pacientes con ese tipo de sangre! |")
                print("--------------------------------------------------------")
        elif opcion == "4":
            print("Compatibilidad Sanguínea:\n")
            # Llama a la función mostrar_compatibilidad() para mostrar información sobre compatibilidad sanguínea.
            mostrar_compatibilidad()
            
        elif opcion == "5":
            # Opción para salir del programa.
            print(" --------------------------------------------")
            print("|  Has salido del aplicativo. ¡Hasta pronto! |")
            print(" --------------------------------------------")
            break
        else:
            # Mensaje de error para opciones no válidas.
            print(" -------------------------------------------------")
            print(" |", "¡Opción no válida! Intenta de nuevo por favor","|")
            print(" -------------------------------------------------")

# Llama a la función main() si este script se ejecuta como el programa principal.
if __name__ == "__main__":
    main()