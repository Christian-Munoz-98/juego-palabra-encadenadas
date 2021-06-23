import random, operator

def registro():
    
    jugadores = {} #Se reinicia el registro al inicio de la funcion

    jugador_1 = input('\nIngrese el nombre del primer jugador: ')
    jugadores.setdefault('Jugador 1',jugador_1)#Se define el nombre del primer jugador en el diccionario

    jugador_2 = input('\nIngrese el nombre del segundo jugador: ')
    jugadores.setdefault('Jugador 2',jugador_2)#Se define el nombre del segundo jugador en el diccionario

    print('\n'+'¡Registro exitoso!'.center(30))
    return jugadores #regresa el diccionario con los jugadores registrados 

def juego(jugadores):

    global registro_puntaciones

    confirmacion_registro_1 = input('\nIngrese el nombre del primer jugador para confirmar el registro: ')
    confirmacion_registro_2 = input('\nIngrese el nombre del segundo jugador para confirmar el registro: ')

    if (confirmacion_registro_1 in jugadores.values()) and (confirmacion_registro_2 in jugadores.values()): #confirma la existencia de los jugadores para inicar juego

        alfabeto = 'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z'.split()#Se obtiene la lista de las letras del alfabeto
        letra_incial = random.choice(alfabeto) #Selecciona la letra con la que iniciará la partida

        num_jugador = 1 #Variable que define de que jugador es el turno

        palabras_ingresadas_1,palabras_ingresadas_2 = 0,0 #Variables que guarda las palabras ingresadas de cada jugador

        puntuacion_1, puntuacion_2 = 0,0 #Variables para guardar puntuaciones

        vidas_1, vidas_2 = 3,3 #Variable para contabilizar las oportunidades de cada jugador

        puntos = 0 #Variable para deifinir los puntos que suma cada jugador

        lista_palabras = []

        print('\n'+'JUGADORES'.center(30,'=')+'\n\n'+'JUGADOR 1'.center(30,'-')+ '\n\n' + (jugadores['Jugador 1'].upper()).center(30) +'\n\n'+'JUGADOR 2'.center(30,'-')+ '\n\n' + (jugadores['Jugador 2'].upper()).center(30)+'\n\n'+'='*30+'\n\n')

        print(f'Jugador 1, tu primera palabra debe de iniciar con la letra {letra_incial}\n')

        while ((vidas_1 > 0) and (vidas_2 > 0)) and ((palabras_ingresadas_1< 20) and (palabras_ingresadas_2< 20)): #mientras cada jugador no gaste 3 intentos e ingrese menos de 20 palabras la partida se ejecuta

            palabra = input(f'Respuesta Jugador {num_jugador}: ')

            if num_jugador == 1: #controla cual jugador es el que ha agregado una palabra
                palabras_ingresadas_1 += 1
            elif num_jugador == 2: 
                palabras_ingresadas_2 += 1
            
            if (palabra[0] != letra_incial.upper()) and (palabra[0] != letra_incial.lower()): #El ciclo se reinicia y solicita al jugador ingresar una palabra valida
                print(f'Error, vuelve a ingresar la palabra recuerda que debe iniciar con la letra {letra_incial.upper()}')
                if num_jugador == 1: #Resta una vida al jugador por equivocarse
                    vidas_1 -= 1
                elif num_jugador == 2:
                    vidas_2 -= 1
                continue

            letra_incial = palabra[len(palabra)-1] #Define la nueva letra con la que debe inicar la siuiente palabra

            if len(palabra) > 7: #Definen cuantos puntos suma el jugador segun la longitud de la palabra
                puntos = 6
            elif len(palabra) == 7:
                puntos = 5
            elif len(palabra) == 6:
                puntos = 4
            elif len(palabra) == 5:
                puntos = 3
            elif len(palabra) == 4:
                puntos = 2
            else:
                puntos = 1
            
            if palabra in lista_palabras: #Si ingresa una palabra repetida sus puntos se anulan
                puntos = 0
            
            if len(lista_palabras) == 0:
                lista_palabras.append(palabra)
            else:
                if palabra != lista_palabras[len(lista_palabras)-1]:
                    lista_palabras.append(palabra) #Regisstra las palabras ingresadas siempre y cuando no se ingrese la misma palabra consecutivamente
                else:
                    puntos = -2 #resta dos puntos al jugador por el error

            if num_jugador == 1:#Intercambia turnos y suma puntos
                puntuacion_1 += puntos
                num_jugador = 2
            elif num_jugador == 2: 
                puntuacion_2 += puntos
                num_jugador = 1
            
        if puntuacion_1 > puntuacion_2: #Imprime al ganador de la partida
            print('\n'+'EL GANADOR ES'.center(30,'=') +'\n'+(jugadores['Jugador 1'].upper()).center(30) + '\n'+'='*30)
        elif puntuacion_2 > puntuacion_1:
            print('\n'+'EL GANADOR ES'.center(30,'=') +'\n' + (jugadores['Jugador 2'].upper()).center(30) + '\n'+'='*30)
        else:
            print('\n'+'='*28+'\nLA PARTIDA TERMINÓ EN EMPATE\n'+'='*28+'\n')
    
        print('Puntuaciones:\n'+ jugadores['Jugador 1'] + ' ' + '='*10 + ' '+ str(puntuacion_1) + '\n' + jugadores['Jugador 2'] + ' ' + '='*10 + ' ' + str(puntuacion_2))

        registro_puntaciones.setdefault(jugadores['Jugador 1'],[])#Crea una lista de puntuaciones para cada jugador nuevo registrado
        registro_puntaciones.setdefault(jugadores['Jugador 2'],[])

        registro_puntaciones[jugadores['Jugador 1']].append(puntuacion_1)#Agrega la ultima puntuacion de los jugadores al registro
        registro_puntaciones[jugadores['Jugador 2']].append(puntuacion_2)

    else: 
        print("\n\n"+"¡ERROR!".center(30)+ "\n\nPuede que uno o más jugadores no estén registrados.Por favor regístrense antes de jugar\n\n")#Mensaje de error en caso de que los jugadores no esten registrados

def consulta():
    global registro_puntaciones
    puntuaciones_globales = {}#Crea un nuevo diccionaro con las puntuaciones ordenadas 
    
    if len(registro_puntaciones) == 0 :
        print('\n'+'¡ERROR!'.center(51))
        print('No hay puntuaciones registradas en la base de datos') #Error en caso de querer consultar puntuaciones sin jugadores registrados
    else:
        while True:
            nombre = input("\nIngrese el nombre del jugador que desea consultrar: ")

            if nombre in registro_puntaciones.keys():#Confirma que el jugador está registrado
                
                print('\n'+'PARTIDAS DEL JUGADOR'.center(29,'='))
                for partida,puntuacion in enumerate(registro_puntaciones[nombre]):#Imprime el historial de puntuaciones del jugador 
                    print(f'Partida {partida+1}: obtuvo {puntuacion} puntos')
                print('='*30)
                
                for jugador,puntuaciones in registro_puntaciones.items():
                    if jugador == nombre:
                        continue#Omite al jugador del que se consultó su historial
                    
                    puntuacion_global = 0
                    
                    for partida in puntuaciones:
                        puntuacion_global += partida
                    puntuaciones_globales.setdefault(jugador,puntuacion_global)#Agrega las puntuaciones globales al nuevo diccionario
                
                puntuaciones_ordenadas = list(reversed(sorted(puntuaciones_globales.items(), key=operator.itemgetter(1))))#Crea una lista las puntuaciones emparejadas con los jugadores


                puntuaciones_globales = {}

                for element in puntuaciones_ordenadas:
                    puntuaciones_globales[element[0]] = element[1]#Ordena el diccionario con las puntuaciones globales
                print('PUNTUACIONES GLOBALES'.center(29,'='))

                for jugador,puntuacion_global in puntuaciones_globales.items():
                    print(f"{jugador}---------{puntuacion_global}")#Imprime las puntuaciones globales en orden decreciente
                print('='*30)
                break
            print("\n¡Eror!. Ingrese un nombre que se encuentre disponible en la base de datos.")#mensaje de error en caso de que el jugador no esté registrado

def menu(): #Menu de opciones principal
    global jugadores
    print('\n'+'ELIJA UNA OPCIÓN'.center(30,'-')+'\n'+'1.Registrar Jugadores'.ljust(30,'-')+'\n'+'2.Verificar puntuaciones'.ljust(30,'-')+'\n'+'3.Jugar'.ljust(30,'-')+'\n'+'4.salir'.ljust(30,'-'))
    opcion = int(input('\n'+ 'Selección: '))

    if opcion == 1:
        jugadores = registro()
        menu() #Recursividad del menu
    elif opcion == 2:
        consulta()
        menu()
    elif opcion == 3:
        juego(jugadores)
        menu()
    elif opcion == 4:
        print('\n'+'Saliendo del programa...'.center(30))
        print('\n'+'Que tenga buen dia!'.center(30))#EL programa se detiene porque se rompio la recursividad
    else:
        print('\nError! Elija una opción válida...\n')
        menu()

if __name__ == '__main__': #Entry point (programa principal)
    registro_puntaciones = {}#Variables globales
    jugadores = {}
    menu()
#Colorear prints