def crearFacebook():
    print("<< Cuenta de Facebook >>")
    nombre = input("Nombre del usuario:\n> ")
    edad = int(input("Edad del usuario:\n> "))
    ciudad = input("Ciudad del usuario:\n> ")
    pais = input("Pais del usuario:\n> ")
    correo = input("Correo del usuario:\n> ")
    cadena = (f"----Cuenta de Facebook creada----\n"
              f"Nombre del usuario: {nombre}\nNombre del usuario: {edad}\nCiudad del usuario: {ciudad}\n"
              f"Pais del usuario: {pais}\nCorreo del usuario: {correo}\n")
    return cadena


def crearTwitter():
    print("<< Cuenta de Twitter >>")
    nombre = input("Nombre del usuario:\n> ")
    nombresCompletos = input("Nombres Completos del usuario:\n> ")
    apellidos = input("Apellido Completos del usuario:\n> ")
    edad = int(input("Edad del usuario:\n> "))
    ciudad = input("Ciudad del usuario:\n> ")
    pais = input("Pais del usuario:\n> ")
    idioma = input("Idioma del usuario:\n> ")
    correo = input("Correo electronico del usuario:\n> ")
    print(f"----Cuenta de Twitter creada----\n"
          f"Nombre del usuario: {nombre}\nNombres Completos del usuario: {nombresCompletos}\nApellidos "
          f"Completos del usuario: {apellidos}\nEdad del usuario: {edad}\n"
          f"Ciudad del usuario: {ciudad}\nPais del usuario: {pais}\nIdioma del usuario: {idioma}\n"
          f"Correo del usuario: {correo}\n")


def crearWhatsapp():
    print("<< Cuenta de Whatsapp >>")
    nombre = input("Nombre del usuario:\n> ")
    numero = int(input("Telefono del usuario:\n> "))
    edad = int(input("Edad del usuario:\n> "))
    ciudad = input("Ciudad del usuario:\n> ")
    pais = input("Pais del usuario:\n> ")
    cadena = (f"----Cuenta de Whatsapp creada----\n"
              f"Nombre del usuario: {nombre}\nTelefono del usuario: {numero}\n"
              f"Edad del usuario: {edad}\nCiudad del usuario: {ciudad}\nPais del usuario: {pais}\n")
    return cadena


def crearTelegram():
    print("<< Cuenta de Telegram >>")
    nombre = input("Nombre del usuario:\n> ")
    numero = int(input("Telefono del usuario:\n> "))
    ciudad = input("Ciudad del usuario:\n> ")
    pais = input("Pais del usuario:\n> ")
    area_interes = input("Area de interés del usuario:\n> ")
    print(f"----Cuenta de Telegram creada----\n"
          f"Nombre del usuario: {nombre}\nTelefono del usuario: {numero}\n"
          f"Ciudad del usuario: {ciudad}\nPais del usuario: {pais}\nArea de interés del usuario: {area_interes}\n")


def crearSignal():
    print("<< Cuenta de Signal >>")
    nombre = input("Nombre del usuario:\n> ")
    numero = int(input("Telefono del usuario:\n> "))
    ciudad = input("Ciudad del usuario:\n> ")
    pais = input("Pais del usuario:\n> ")
    hobby = input("Hobby principal del usuario:\n> ")
    cadena = (f"----Cuenta de Signal creada----\n"
              f"Nombre del usuario: {nombre}\nTelefono del usuario: {numero}\n"
              f"Ciudad del usuario: {ciudad}\nPais del usuario: {pais}\nHobby principal del usuario: {hobby}\n")
    return cadena


def crearInstagram():
    print("<< Cuenta de Instagram >>")
    nombre = input("Nombre del usuario:\n> ")
    ciudad = input("Ciudad del usuario:\n> ")
    edad = int(input("Edad del usuario:\n> "))
    correo = input("Correo del usuario:\n> ")
    print(f"----Cuenta de Instagram creada----\n"
          f"Nombre del usuario: {nombre}\nCiudad del usuario: {ciudad}\nEdad del usuario: {edad}\n"
          f"Correo del usuario: {correo}\n")


def crearFlickr():
    print("<< Cuenta de Flickr >>")
    nombre = input("Nombre del usuario:\n> ")
    correo = input("Correo del usuario:\n> ")
    cadena = (f"----Cuenta de Flickr creada----\n"
              f"Nombre del usuario {nombre}\nCorreo del usuario: {correo}\n")
    return cadena


def obtenerMensaje(cuentasCreadas):
    mensaje = ""
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if (cuentasCreadas >= 1) and (cuentasCreadas <= 5):
        mensaje = mensajeFinal[0]
    else:
        if (cuentasCreadas >= 6) and (cuentasCreadas <= 15):
            mensaje = mensajeFinal[1]
        else:
            if cuentasCreadas >= 16:
                mensaje = mensajeFinal[2]
    return mensaje


if __name__ == "__main__":
    bandera = True
    contador = 0
    while bandera:
        opcion = int(input("Ingrese 1 si desea crear una cuenta de Facebook\n"
                           + "Ingrese 2 si desea crear una cuenta de twitter\n"
                           + "Ingrese 3 si desea crear una cuenta de Whatsapp\n"
                           + "Ingrese 6 si desea crear una cuenta de Telegram\n"
                           + "Ingrese 5 si desea crear una cuenta de Instagram\n"
                           + "Ingrese 6 si desea crear una cuenta de Flickr\n"
                           + "Ingrese 7 si desea crear una cuenta de twitter\n>"))
        contador = contador + 1
        if opcion == 1:
            cadenaFinal = crearFacebook()
            print(cadenaFinal)
        elif opcion == 2:
            crearTwitter()
        elif opcion == 3:
            cadenaFinal = crearWhatsapp()
            print(cadenaFinal)
        elif opcion == 4:
            crearTelegram()
        elif opcion == 5:
            cadenaFinal = crearSignal()
            print(cadenaFinal)
        elif opcion == 6:
            crearInstagram()
        elif opcion == 7:
            cadenaFinal = crearFlickr()
            print(cadenaFinal)
        else:
            print("No es una opcion a seleccionar")
        salida = input("Ingrese (si) en caso que desee salir del ciclo\n> ")
        if salida == "si":
            bandera = False
    print(obtenerMensaje(contador))
