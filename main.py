#Archivo original: TP 1 - GRUPO 22
import getpass
import random

import os

'''
Type
flight = [
    [flightCode, airline, origin, destination, date, time, price, seats],

Var
flights : flight

'''
MAXFLIGHTS = 20
MAXAIRLINES = 5 #cambio a 5 maximo por consigna



# Inicializar el array vacío - MODIFICADO: Agregado estado del vuelo
flights = [[""]*6 for i in range(MAXFLIGHTS)]  # 6 columnas: aerolínea, origen, destino, fecha, hora, estado
flightPrices = [0.0] * MAXFLIGHTS

#ejemplo:
# flights[0] = ["LAT", "Buenos Aires", "Santiago", "01/06/2025", "10:00", "A"] y flightPrices[0] = 150.00

# ARREGLO DE AEROLINES PRECARGADO
# airlines = [name, iata, descriptionAirline, code]
airlines = [
    ["Aerolínea Argentina", "AAA", "Descripción de Aerolínea Argentina", "ARG"],
    ["Latam", "LAT", "Descripción de Latam", "CHI"],
    ["Gol", "GOL", "Descripción de Gol", "BRA"],
    ["Aerolínea Austral", "AUS", "Descripción de Aerolínea Austral", "ARG"],
    ["Sky Airline", "SKY", "Descripción de Sky Airline", "CHI"]
]

user = ""
password = ""
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
    print("   5. Gestión de Vuelos")
    print("   0. Salir")

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

#Funcion para mostrar el submenu de gestión de vuelos (Para usuario tipo SEO)
def subMenu5():
    opt5 = ""
    while (opt5 != "d"):
        print("\n- Gestión de Vuelos")
        print("  a. Crear Vuelo")
        print("  b. Modificar Vuelo")
        print("  c. Eliminar Vuelo")
        print("  e. buscar Vuelo") #requerimiento 2 hay q sacarlo de aca!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("  d. Volver")

        opt5 = (input("\n**** Ingrese una opción: "))
        while(opt5 != "a" and opt5 != "b" and opt5 != "c" and opt5 != "d" and opt5 != "e"):
            opt5 = (input("Opción inválida. Por favor ingrese una nuevamente: "))

        match opt5:
            case "a":
                createFlight(airlines, flights, flightPrices,seatMatrix)
                showFlights(flights, flightPrices)
                listAirlinesFlights()
            case "b":
                modifyFlight()
            case "c":
                deleteFlight()
            case "e":
                flightSearch()
            case "d":
                print("\nVolviendo al menú principal...")

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

# Funcion para crear VUELOS - MODIFICADA: Incluye estado del vuelo
def createFlight(airlines, flights, flightPrices, seatMatrix):
    print("\n CREANDO VUELOS")

    flightIndex = 0
    #ver cuántos vuelos hay creados
    for i in range(MAXFLIGHTS):
        if flights[i][0] != "":
            flightIndex += 1

    airlineCode = input(" \n  Ingrese el Código de aerolínea (máx. 3 caracteres) o 'salir' para volver: ")
    while airlineCode != "salir":
        while(flightIndex<MAXFLIGHTS):
            # Validación del código de aerolínea.
            while (len(airlineCode) > 3):
                airlineCode = input("  Código inválido. Ingrese el código de aerolínea (máx. 3 caracteres): ")
            # Se busca la aerolínea ingresada.
            while(searchAirline(airlineCode,airlines) == False):
                airlineCode = input("  Aerolínea no encontrada. Ingrese el código de aerolínea (máx. 3 caracteres): ")

            flights[flightIndex][0] = airlineCode  # Asignar el código de aerolínea al vuelo
            flights[flightIndex][1] = input(" \n  Ingrese origen del vuelo: ")
            flights[flightIndex][2] = input(" \n  Ingrese destino del vuelo: ")
            flights[flightIndex][3] = input(" \n  Ingrese fecha del vuelo (DD/MM/AAAA): ")
            flights[flightIndex][4] = input(" \n  Ingrese hora del vuelo (HH:MM): ")
            flights[flightIndex][5] = "A"  # Asignar estado activo por defecto

            flightPrices[flightIndex] = float(input(" \n  Precio del vuelo: "))
            # Asignar asientos al vuelo
            assignSeatsToFlight(seatMatrix, flightIndex)

            print("\n  Vuelo CREADO exitosamente.")

            airlineCode = input(" \n  Ingrese el código de aerolínea (máx. 3 caracteres) o 'salir' para volver: ")
            if airlineCode == "salir":
                flightIndex= 9999
            else:
                flightIndex += 1

# MODIFICADA: Incluye estado del vuelo
def showFlights(flights, flightPrices):
    print("\n  Vuelos disponibles:")
    print("  ------------------------------------------")
    print("  Aerolínea | Origen       | Destino      | Fecha       | Hora     | Precio   | Estado")
    for i in range(MAXFLIGHTS):
        if flights[i][0] != "":
            estado_texto = "ACTIVO" if flights[i][5] == "A" else "BAJA"
            print(f"   {flights[i][0]}     {flights[i][1]}  {flights[i][2]}  {flights[i][3]} {flights[i][4]}  ${flightPrices[i]:.2f}  {estado_texto}")

# MODIFICADA: Validar que el vuelo esté activo antes de modificar
def modifyFlight():
    global flights, flightPrices, airlines
    
    print("\n MODIFICAR VUELO")
    
    # Mostrar vuelos disponibles primero
    showFlightsWithIndex(flights, flightPrices)
    
    if not hasFlights():
        print("\n  No hay vuelos disponibles para modificar.")
        return
    
    flightCode = input("\n  Ingrese el código de vuelo (índice) a modificar o 'salir' para volver: ")
    
    while flightCode != "salir":
        try:
            flightIndex = int(flightCode)
            if flightIndex >= 0 and flightIndex < MAXFLIGHTS and flights[flightIndex][0] != "":
                
                # Verificar si el vuelo está dado de baja
                if flights[flightIndex][5] == "B":
                    print(f"\n  El vuelo {flightIndex} está dado de baja.")
                    activar = input("  ¿Desea activarlo para poder modificarlo? (s/n): ")
                    if activar.lower() == "s":
                        flights[flightIndex][5] = "A"
                        print("  ¡Vuelo activado exitosamente!")
                    else:
                        print("  No se puede modificar un vuelo dado de baja.")
                        break
                
                print(f"\n  Vuelo encontrado: {flights[flightIndex][0]} - {flights[flightIndex][1]} a {flights[flightIndex][2]}")
                print("  ¿Qué desea modificar?")
                print("    1. Aerolínea")
                print("    2. Origen")
                print("    3. Destino") 
                print("    4. Fecha")
                print("    5. Hora")
                print("    6. Precio")
                print("    7. Modificar todo")
                print("    0. Cancelar")
            
                option = input("\n  Ingrese su opción: ")
                while option not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
                    option = input("  Opción inválida. Ingrese una opción válida: ")
            
                match option:
                    case "1":
                        newAirlineCode = input("  Ingrese el nuevo código de aerolínea (máx. 3 caracteres): ")
                        while len(newAirlineCode) > 3:
                            newAirlineCode = input("  Código inválido. Ingrese el código de aerolínea (máx. 3 caracteres): ")
                        while not searchAirline(newAirlineCode, airlines):
                            newAirlineCode = input("  Aerolínea no encontrada. Ingrese el código de aerolínea (máx. 3 caracteres): ")
                        flights[flightIndex][0] = newAirlineCode
                        print("  ¡Aerolínea modificada exitosamente!")
                    
                    case "2":
                        flights[flightIndex][1] = input("  Ingrese el nuevo origen del vuelo: ")
                        print("  ¡Origen modificado exitosamente!")
                    
                    case "3":
                        flights[flightIndex][2] = input("  Ingrese el nuevo destino del vuelo: ")
                        print("  ¡Destino modificado exitosamente!")
                    
                    case "4":
                        flights[flightIndex][3] = input("  Ingrese la nueva fecha del vuelo (DD/MM/AAAA): ")
                        print("  ¡Fecha modificada exitosamente!")
                    
                    case "5":
                        flights[flightIndex][4] = input("  Ingrese la nueva hora del vuelo (HH:MM): ")
                        print("  ¡Hora modificada exitosamente!")
                    
                    case "6":
                        flightPrices[flightIndex] = float(input("  Ingrese el nuevo precio del vuelo: "))
                        print("  ¡Precio modificado exitosamente!")
                    
                    case "7":
                        # Modificar todos los campos
                        newAirlineCode = input("  Ingrese el nuevo código de aerolínea (máx. 3 caracteres): ")
                        while len(newAirlineCode) > 3:
                            newAirlineCode = input("  Código inválido. Ingrese el código de aerolínea (máx. 3 caracteres): ")
                        while not searchAirline(newAirlineCode, airlines):
                            newAirlineCode = input("  Aerolínea no encontrada. Ingrese el código de aerolínea (máx. 3 caracteres): ")
                    
                        flights[flightIndex][0] = newAirlineCode
                        flights[flightIndex][1] = input("  Ingrese el nuevo origen del vuelo: ")
                        flights[flightIndex][2] = input("  Ingrese el nuevo destino del vuelo: ")
                        flights[flightIndex][3] = input("  Ingrese la nueva fecha del vuelo (DD/MM/AAAA): ")
                        flights[flightIndex][4] = input("  Ingrese la nueva hora del vuelo (HH:MM): ")
                        flightPrices[flightIndex] = float(input("  Ingrese el nuevo precio del vuelo: "))
                        print("  ¡Vuelo modificado exitosamente!")
                    
                    case "0":
                        print("  Modificación cancelada.")
            
                # Mostrar vuelos actualizados
                showFlightsWithIndex(flights, flightPrices)
                break
            else:
                print("  Vuelo no encontrado o índice inválido.")
            
        except ValueError:
            print("  Código inválido. Ingrese un número válido.")
        except:
            print("  Error al procesar el código de vuelo.")
            
        flightCode = input("\n  Ingrese el código de vuelo (índice) a modificar o 'salir' para volver: ")

# MODIFICADA: Incluye estado del vuelo
def showFlightsWithIndex(flights, flightPrices):
    """Muestra los vuelos con su índice como código"""
    print("\n  Vuelos disponibles:")
    print("  ------------------------------------------")
    print("  Código | Aerolínea | Origen    | Destino   | Fecha      | Hora  | Precio   | Estado")
    for i in range(MAXFLIGHTS):
        if flights[i][0] != "":
            estado_texto = "ACTIVO" if flights[i][5] == "A" else "BAJA"
            print(f"   {i}      {flights[i][0]}     {flights[i][1]}  {flights[i][2]}  {flights[i][3]} {flights[i][4]}  ${flightPrices[i]:.2f}  {estado_texto}")

# NUEVA: Función para eliminar vuelo (baja lógica)
def deleteFlight():
    global flights, flightPrices
    
    print("\n ELIMINAR VUELO")
    
    # Mostrar vuelos disponibles primero
    showFlightsWithIndex(flights, flightPrices)
    
    if not hasActiveFlights():
        print("\n  No hay vuelos activos para eliminar.")
        return
    
    flightCode = input("\n  Ingrese el código de vuelo (índice) a eliminar o 'salir' para volver: ")
    
    while flightCode != "salir":
        try:
            flightIndex = int(flightCode)
            if flightIndex >= 0 and flightIndex < MAXFLIGHTS and flights[flightIndex][0] != "":
                
                # Verificar si el vuelo está activo
                if flights[flightIndex][5] == "B":
                    print(f"\n  El vuelo {flightIndex} ya está dado de baja.")
                    break
                elif flights[flightIndex][5] == "A":
                    print(f"\n  Vuelo encontrado: {flights[flightIndex][0]} - {flights[flightIndex][1]} a {flights[flightIndex][2]}")
                    print(f"  Precio: ${flightPrices[flightIndex]:.2f}")
                    
                    # Confirmación antes de eliminar
                    confirmar = input("\n  ¿Está seguro que desea eliminar este vuelo? (s/n): ")
                    if confirmar.lower() == "s":
                        flights[flightIndex][5] = "B"  # Cambiar estado a baja
                        print("  ¡Vuelo eliminado exitosamente!")
                        
                        # Mostrar vuelos actualizados
                        showFlightsWithIndex(flights, flightPrices)
                    else:
                        print("  Eliminación cancelada.")
                    break
            else:
                print("  Vuelo no encontrado o índice inválido.")
            
        except ValueError:
            print("  Código inválido. Ingrese un número válido.")
        except:
            print("  Error al procesar el código de vuelo.")
            
        flightCode = input("\n  Ingrese el código de vuelo (índice) a eliminar o 'salir' para volver: ")

def searchAirline(airlineCode, airlines):
    foundAirline = False
    for airline in range(MAXAIRLINES):
        if airlines[airline][1] == airlineCode:
            print("\n  Aerolínea encontrada:")
            foundAirline = True
    return foundAirline

def hasFlights():
    """Verifica si hay vuelos cargados en el sistema"""
    for i in range(MAXFLIGHTS):
        if flights[i][0] != "":
            return True
    return False

# NUEVA: Función para verificar si hay vuelos activos
def hasActiveFlights():
    """Verifica si hay vuelos activos en el sistema"""
    for i in range(MAXFLIGHTS):
        if flights[i][0] != "" and flights[i][5] == "A":
            return True
    return False

def initializeSeatMatrix():
    # Crear matriz vacía de 800x7 de forma clásica
    seatMatrix = [[None for j in range(7)] for i in range(800)]
    
    # Inicializar la columna del pasillo
    for row in range(800):
        seatMatrix[row][3] = "PASILLO"
    
    # Inicializar todos los asientos como None (excepto pasillo)
    for row in range(800):
        for col in range(7):
            if col != 3:  # No tocar la columna del pasillo
                seatMatrix[row][col] = None
    
    return seatMatrix

def assignSeatsToFlight(seatMatrix, flightIndex):
    # Asigna asientos aleatoriamente con estados L, O, R para un vuelo específico
    
    if flightIndex < 0 or flightIndex >= 20:
        print("Error: Índice de vuelo inválido. Debe estar entre 0 y 19")
        return
    
    startRow = flightIndex * 40
    endRow = startRow + 39
    
    states = ["L", "O", "R"]
    
    for row in range(startRow, endRow + 1):
        for col in range(7):
            if col != 3:
                randomState = random.choice(states)
                seatMatrix[row][col] = randomState
    
    print(f"Asientos asignados al vuelo {flightIndex + 1} (filas {startRow} a {endRow})")
    print("Asientos inicializados aleatoriamente: L (libre), O (ocupado), R (reservado)")


#ListarVuelosAerolineas(): REQUERIMIENTO 1
def listAirlinesFlights():
    # Arreglo auxiliar para contar vuelos por aerolínea [código, cantidad]
    airlineFlightCount = [["", 0] for i in range(MAXAIRLINES)]
    
    # Inicializar con las aerolíneas existentes
    for i in range(MAXAIRLINES):
        airlineFlightCount[i][0] = airlines[i][1]  # Código IATA de la aerolínea
        airlineFlightCount[i][1] = 0  # Inicializar contador en 0
    
    # Contar vuelos vigentes por aerolínea
    for i in range(MAXFLIGHTS):
        if flights[i][0] != "" and flights[i][5] == "A":  # Solo vuelos vigentes
            airlineCode = flights[i][0]
            
            # Buscar la aerolínea en el contador y sumar
            for j in range(MAXAIRLINES):
                if airlineFlightCount[j][0] == airlineCode:
                    airlineFlightCount[j][1] += 1
    
    # Ordenar de manera descendente por cantidad de vuelos (Falsa Burbuja)
    for i in range(MAXAIRLINES - 1):
        for j in range(MAXAIRLINES - 1 - i):
            if airlineFlightCount[j][1] < airlineFlightCount[j + 1][1]:
                aux = airlineFlightCount[j]
                airlineFlightCount[j] = airlineFlightCount[j + 1]
                airlineFlightCount[j + 1] = aux
    
    # Mostrar resultados
    print("\n  VUELOS VIGENTES POR AEROLÍNEA (ordenado descendente)")
    print("  ------------------------------------------")
    print("  Posición | Aerolínea | Cantidad de Vuelos")
    
    for i in range(MAXAIRLINES):
        print(f"     {i+1}      {airlineFlightCount[i][0]}       {airlineFlightCount[i][1]}")
    
    print(f"\n  Aerolínea con MAYOR cantidad de vuelos: {airlineFlightCount[0][0]} ({airlineFlightCount[0][1]} vuelos)")
    print(f"  Aerolínea con MENOR cantidad de vuelos: {airlineFlightCount[MAXAIRLINES-1][0]} ({airlineFlightCount[MAXAIRLINES-1][1]} vuelos)")

#buscarVuelos() REQUERIMIENTO 2
def flightSearch():
   fechaBusqueda = input("\nIngrese la fecha de salida (DD/MM/AAAA): ")
   
   vuelosEncontrados = 0
   
   print("\n" + "=" * 104)
   print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA")
   print("=" * 104)
   print("CÓDIGO  AEROLÍNEA        ORIGEN           DESTINO          FECHA        HORA     PRECIO")
   print("vuelo")
   print("-" * 104)
   
   for i in range(MAXFLIGHTS):
       if flights[i][0] != "" and flights[i][5] == "A" and flights[i][3] == fechaBusqueda:
           # Buscar nombre de la aerolínea
           nombreAerolinea = ""
           for j in range(MAXAIRLINES):
               if airlines[j][1] == flights[i][0]:
                   nombreAerolinea = airlines[j][0]
           
           print(f"{i+1:<8}{nombreAerolinea:<17}{flights[i][1]:<17}{flights[i][2]:<17}{flights[i][3]:<13}{flights[i][4]:<9}${flightPrices[i]:,.0f}")
           vuelosEncontrados += 1
   
   print("-" * 104)
   print(f"Total de vuelos: {vuelosEncontrados}")    

#Programa principal
seatMatrix = initializeSeatMatrix()  # Inicializar y GUARDAR la matriz de asientos
login()
if (login1):  
    while (opt!="0"):
        menu()
        opt = (input("\nIngrese una opción: "))
        # Validación de la opción.
        while(opt != "1" and opt != "2" and opt != "3" and opt != "4" and opt != "5" and opt != "0"):
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
            case "5":
                subMenu5()
print("\nPrograma finalizado.")
print(" ")