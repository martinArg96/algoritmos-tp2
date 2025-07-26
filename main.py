#Archivo original: TP 1 - GRUPO 22

import getpass
user = "admin"
password = "admin"
loginCount = 0
login1 = False
opt = 1

# Variables para las novedades.
newsCode1 = "1"
newsText1 = "Una novedad importante: Aerolínea XYZ lanza una nueva ruta internacional"
newsPublicationDate1 = "10/05/2025"
newsExpirationDate1 = "10/06/2025"

newsCode2 = "2"
newsText2 = "Nueva aerolínea asociada: SkyWings comienza a operar en Argentina"
newsPublicationDate2 = "12/05/2025"
newsExpirationDate2 = "12/07/2025"

newsCode3 = "3"
newsText3 = "Mantenimiento programado para el sistema de reservas el día 20/05"
newsPublicationDate3 = "15/05/2025"
newsExpirationDate3 = "21/05/2025"

# Función para mostrar el menú principal.
def menu():
    print("\n●  Menú del Administrador")
    print("   1. Gestión de Aerolíneas")
    print("   2. Aprobar/Denegar Promociones")
    print("   3. Gestión de Novedades")
    print("   4. Reportes")
    print("   5. Salir")

# Función para mostrar el submenú1 con validación de la opción.   
def subMenu1():    
    opt1= ""
    while (opt1 != "d"):
        print("\n- Gestión de Aerolíneas")
        print("  a. Crear Aerolínea")
        print("  b. Modificar Aerolínea")
        print("  c. Eliminar Aerolínea")
        print("  d. Volver")
        
        opt1 = (input("\n* Ingrese una opción: "))
        while(opt1 != "a" and opt1 != "b" and opt1 != "c" and opt1 != "d"):
            opt1 = (input("Opción inválida. Por favor ingrese una nuevamente: "))
            
        if (opt1=="b" or opt1=="c"):
            construction()
        elif (opt1=="a"):
            createAirline()

# Función para mostrar el submenú3 con validación de la opción.                         
def subMenu3():    
    opt3 = ""
    while (opt3 != "e"):
        print("\n- Gestión de Novedades")
        print("  a. Crear Novedad")
        print("  b. Modificar Novedad")
        print("  c. Eliminar Novedad")
        print("  d. Ver Novedades")
        print("  e. Volver")
        
        opt3 = (input("\n*** Ingrese una opción: "))
        while(opt3 != "a" and opt3 != "b" and opt3 != "c" and opt3 != "d" and opt3 != "e"):
            opt3 = (input("Opción inválida. Por favor ingrese una nuevamente: "))
            
        if (opt3 == "a" or opt3 == "c"):
            construction()
        elif (opt3 == "b"):
            modifyNews()
        elif (opt3 == "d"): 
            showNews()

# Función para mostrar el submenú4 con validación de la opción.   
def subMenu4():
    opt4 = ""     
    while (opt4 != "d"):
        print("\n- Reportes")
        print("  a. Reporte de Ventas")
        print("  b. Reporte de Vuelos")
        print("  c. Reporte de Usuarios")
        print("  d. Volver")
        
        opt4 = (input("\n**** Ingrese una opción: "))
        while(opt4 != "a" and opt4 != "b" and opt4 != "c" and opt4 != "d"):
                opt4 = (input("Opción inválida. Por favor ingrese una nuevamente: "))
                
        if (opt4 == "a" or opt4 == "b" or opt4 == "c"):
            construction()

# Función para mostrar en las opciones que no tienen funcionalidad todavía.         
def construction():
    print("\n* EN CONSTRUCCIÓN...")

# Función para crear aerolíneas con las validaciones correspondientes.
def createAirline():
    name = 1
    ARG = 0
    BRA = 0
    CHI = 0
    
    while (name != "no"):
        name = input("\nIngrese el nombre de una nueva aerolínea, en caso de querer salir ingrese la palabra 'no': ")
        if (name != "no"):
            iata = input("\nIngrese código IATA (máx. 3 caracteres): ")
            # Se asegura la longitud límite del código IATA.
            while (len(iata)>3):
                iata = input("Código inválido. Ingrese código IATA (máx. 3 caracteres): ")
            
            # Variable momentaneamente inutilizada pero necesaria para esta etapa.    
            descriptionAirline = input("\nIngrese descripción de la aerolínea: ")
            
            code = input("\nIngrese el código de país (ARG, BRA O CHI): ")
            # Se asegura que se ingresen solamente los códigos aceptados.
            while (code != "ARG" and code != "BRA" and code != "CHI"):
                code = input("\nCódigo incorrecto. Ingrese el código de país (ARG, BRA O CHI): ")
                
            # Se cuenta la cantidad de aerolíneas por país.
            if (code =="ARG" or code =="BRA" or code =="CHI"):
                match code:
                    case "ARG":    
                        ARG +=1
                    case "BRA":    
                        BRA +=1
                    case "CHI":    
                        CHI +=1
                        
    # Se define cual tiene mayor y menor cantidad de aerolíneas. Se tienen en cuenta si hay 2 iguales o si son las 3 iguales.
    if (ARG>BRA and ARG>CHI):
        print ("\nEl país con mayor cantidad de aerolíneas cargadas es Argentina con ", ARG, " aerolíneas.")
        if (BRA>CHI):
            print ("El país con menor cantidad de aerolíneas cargadas es Chile con ", CHI, " aerolíneas.")
        elif (BRA<CHI):
            print ("El país con menor cantidad de aerolíneas cargadas es Brasil con ", BRA, " aerolíneas.")
        else:
            print ("Los paises con menor cantidad de aerolíneas cargadas son Brasil con ", BRA, " aerolíneas y Chile con ", CHI, " aerolíneas.")
    elif (BRA>ARG and BRA>CHI):
        print ("\nEl país con mayor cantidad de aerolíneas cargadas es Brasil con ", BRA, " aerolíneas.")
        if (ARG>CHI):
            print ("El país con menor cantidad de aerolíneas cargadas es Chile con ", CHI, " aerolíneas.")
        elif (ARG<CHI):
            print ("El país con menor cantidad de aerolíneas cargadas es Argentina con ", ARG, " aerolíneas.")
        else:
            print ("Los paises con menor cantidad de aerolíneas cargadas son Argentina con ", ARG, " aerolíneas y Chile con ", CHI, " aerolíneas.")            
    elif (CHI>ARG and CHI>BRA):
        print ("\nEl país con mayor cantidad de aerolíneas cargadas es Chile con ", CHI, " aerolíneas.")
        if (ARG>BRA):
            print ("El país con menor cantidad de aerolíneas cargadas es Brasil con ", BRA, " aerolíneas")
        elif (ARG<BRA):        
            print ("El país con menor cantidad de aerolíneas cargadas es Argentina con ", ARG, " aerolíneas.")
        else:
            print ("Los paises con menor cantidad de aerolíneas cargadas son Argentina con ", ARG, " aerolíneas y Brasil con ", BRA, " aerolíneas.")
    elif (ARG==BRA):
        if (ARG>CHI):
            print ("\nLos paises con mayor cantidad de aerolíneas cargadas son Argentina con ", ARG, " aerolíneas y Brasil con ", BRA, " aerolíneas.")
            print ("El país con menor cantidad de aerolíneas cargadas es Chile con ", CHI, " aerolíneas.")
            """ elif (ARG<CHI):
            print ("\nEl país con mayor cantidad de aerolíneas cargadas es Chile con ", CHI, " aerolíneas.")
            print ("Los paises con menor cantidad de aerolíneas cargadas son Argentina con ", ARG, " aerolíneas y Brasil con ", BRA, " aerolíneas.") """
        elif (ARG==CHI):
            print ("Todos los países tienen ", ARG, " aerolíneas cargadas.")
    elif (ARG==CHI):
        if (ARG>BRA):
            print ("\nLos paises con mayor cantidad de aerolíneas cargadas son Argentina con ", ARG, " aerolíneas y Chile con ", CHI, " aerolíneas.")
            print ("El país con menor cantidad de aerolíneas cargadas es Chile con ", CHI, " aerolíneas.")
            """ else:
            print ("\nEl país con mayor cantidad de aerolíneas cargadas es Brasil con ", BRA, " aerolíneas.")
            print ("Los paises con menor cantidad de aerolíneas cargadas son Argentina con ", ARG, " aerolíneas y Chile con ", CHI, " aerolíneas.") """
    elif (BRA==CHI):
        if (BRA>ARG):
            print ("\nLos paises con mayor cantidad de aerolíneas cargadas son Brasil con ", BRA, " aerolíneas y Chile con ", CHI, " aerolíneas.")
            print ("El país con menor cantidad de aerolíneas cargadas es Argentina con ", ARG, " aerolíneas.")
            """ else:
            print ("\nEl país con mayor cantidad de aerolíneas cargadas es Argentina con ", ARG, " aerolíneas.")
            print ("Los paises con menor cantidad de aerolíneas cargadas son Brasil con ", BRA, " aerolíneas y Chile con ", CHI, " aerolíneas.") """


# Función para mostrar las novedades
def showNews():
    print("\nNOVEDADES:")
    print("------------------------------------------")
    
    # Mostrar novedad 1
    print("Código:", newsCode1)
    print("Texto:", newsText1)
    print("Fecha publicación:", newsPublicationDate1)
    print("Fecha expiración:", newsExpirationDate1)
    print("------------------------------------------")
    
    # Mostrar novedad 2
    print("Código:", newsCode2)
    print("Texto:", newsText2)
    print("Fecha publicación:", newsPublicationDate2)
    print("Fecha expiración:", newsExpirationDate2)
    print("------------------------------------------")
    
    # Mostrar novedad 3
    print("Código:", newsCode3)
    print("Texto:", newsText3)
    print("Fecha publicación:", newsPublicationDate3)
    print("Fecha expiración:", newsExpirationDate3)
    print("------------------------------------------")      

# Función para modificar una novedad
def modifyNews():
    global newsText1, newsPublicationDate1, newsExpirationDate1
    global newsText2, newsPublicationDate2, newsExpirationDate2
    global newsText3, newsPublicationDate3, newsExpirationDate3
    newsCode = "99"
    
    showNews()
    
    while (newsCode != "0"):        
        newsCode = input("\nIngrese el código de la novedad que desea modificar o '0' para volver: ")
           
        if newsCode == newsCode1:
            print("\nIngrese el código de la novedad que desea modificar:", newsCode1)
            
            newText = input("Ingrese el nuevo texto o ingrese '0' para mantener el actual: ")
            if newText != "0":
                newsText1 = newText
            
            newPublicationDate = input("Ingrese la nueva fecha de publicación o ingrese '0' para mantener el actual: ")
            if newPublicationDate != "0":
                newsPublicationDate1 = newPublicationDate
            
            newExpirationDate = input("Ingrese la nueva fecha de expiración o ingrese '0' para mantener el actual: ")
            if newExpirationDate != "0":
                newsExpirationDate1 = newExpirationDate
            
        elif newsCode == newsCode2:
            print("\nIngrese el código de la novedad que desea modificar: ", newsCode2)
            
            newText = input("Ingrese el nuevo texto o ingrese '0' para mantener el actual: ")
            if newText != "0":
                newsText2 = newText
            
            newPublicationDate = input("Ingrese la nueva fecha de publicación o ingrese '0' para mantener el actual: ")
            if newPublicationDate != "0":
                newsPublicationDate2 = newPublicationDate
            
            newExpirationDate = input("Ingrese la nueva fecha de expiración o ingrese '0' para mantener el actual: ")
            if newExpirationDate != "0":
                newsExpirationDate2 = newExpirationDate
            
        elif newsCode == newsCode3:
            print("\nIngrese el código de la novedad que desea modificar: ", newsCode3)
            
            newText = input("Ingrese el nuevo texto o ingrese '0' para mantener el actual: ")
            if newText != "0":
                newsText3 = newText
            
            newPublicationDate = input("Ingrese la nueva fecha de publicación o ingrese '0' para mantener el actual: ")
            if newPublicationDate != "0":
                newsPublicationDate3 = newPublicationDate
            
            newExpirationDate = input("Ingrese la nueva fecha de expiración o ingrese '0' para mantener el actual: ")
            if newExpirationDate != "0":
                newsExpirationDate3 = newExpirationDate
            
        else:
            print("\nNo se encontró ninguna novedad con ese código.")
                
        print("\n¡Novedad modificada con éxito!")

# Función para iniciar sesión.        
def login():
    global loginCount
    global login1
    
    while (loginCount<3):
        user1 = input("\nIngrese su usuario: ")
        password1 = getpass.getpass("\nIngrese su contraseña: ")
            
        if (user == user1 and password == password1):
            loginCount = 99
        else: 
            loginCount += 1
            print("\nUsuario y/o contraseña inválido. Reintente nuevamente.")
        
    if (loginCount == 3):
        print("\nHa fallado 3 intentos. El programa se cerrara.")
    else:
        print("\n   ¡Ingreso exitoso!")
        login1 = True

#Programa principal
login()
if (login1):  
    while (opt!="5"):
        menu()
        opt = (input("\nIngrese una opción: "))
        # Validación de la opción.
        while(opt != "1" and opt != "2" and opt != "3" and opt != "4" and opt != "5"):
            opt = (input("Opción inválida. Por favor ingrese una nuevamente: "))
        # Redireccionamiento.
        match opt:
            case "1":    
                subMenu1()
            case "2":
                construction()
            case "3":
                subMenu3()
            case "4":
                subMenu4()
print("\nPrograma finalizado.")
print(" ")