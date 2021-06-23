import random, operator

def registro():
    
    jugadores = {}

    jugador_1 = input('\nIngrese el nombre del primer jugador: ')
    jugadores.setdefault('Jugador 1',jugador_1)

    jugador_2 = input('\nIngrese el nombre del segundo jugador: ')
    jugadores.setdefault('Jugador 2',jugador_2)

    print('\n'+'¡Registro exitoso!'.center(30))
    return jugadores

def juego(jugadores):

    global registro_puntaciones

    confirmacion_registro_1 = input('\nIngrese el nombre del primer jugador para confirmar el registro: ')
    confirmacion_registro_2 = input('\nIngrese el nombre del segundo jugador para confirmar el registro: ')

    if (confirmacion_registro_1 in jugadores.values()) and (confirmacion_registro_2 in jugadores.values()):

        alfabeto = 'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z'.split()
        letra_incial = random.choice(alfabeto)

        num_jugador = 1

        palabras_ingresadas_1,palabras_ingresadas_2 = 0,0

        puntuacion_1, puntuacion_2 = 0,0

        vidas_1, vidas_2 = 3,3

        puntos = 0

        lista_palabras = []

        print('\n'+'JUGADORES'.center(30,'=')+'\n\n'+'JUGADOR 1'.center(30,'-')+ '\n\n' + (jugadores['Jugador 1'].upper()).center(30) +'\n\n'+'JUGADOR 2'.center(30,'-')+ '\n\n' + (jugadores['Jugador 2'].upper()).center(30)+'\n\n'+'='*30+'\n\n')

        print(f'Jugador 1, tu primera palabra debe de iniciar con la letra {letra_incial}\n')

        while ((vidas_1 > 0) and (vidas_2 > 0)) and ((palabras_ingresadas_1< 20) and (palabras_ingresadas_2< 20)):

            palabra = input(f'Respuesta Jugador {num_jugador}: ')

            if num_jugador == 1:
                palabras_ingresadas_1 += 1
            elif num_jugador == 2: 
                palabras_ingresadas_2 += 1
            
            if (palabra[0] != letra_incial.upper()) and (palabra[0] != letra_incial.lower()):
                print(f'Error, vuelve a ingresar la palabra recuerda que debe iniciar con la letra {letra_incial.upper()}')
                if num_jugador == 1:
                    vidas_1 -= 1
                elif num_jugador == 2:
                    vidas_2 -= 1
                continue

            letra_incial = palabra[len(palabra)-1]

            if len(palabra) > 7:
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
            
            if palabra in lista_palabras:
                puntos = 0
            
            if len(lista_palabras) == 0:
                lista_palabras.append(palabra)
            else:
                if palabra != lista_palabras[len(lista_palabras)-1]:
                    lista_palabras.append(palabra)
                else:
                    puntos = -2

            if num_jugador == 1:
                puntuacion_1 += puntos
                num_jugador = 2
            elif num_jugador == 2: 
                puntuacion_2 += puntos
                num_jugador = 1
            
        if puntuacion_1 > puntuacion_2:
            print('\n'+'EL GANADOR ES'.center(30,'=') +'\n'+(jugadores['Jugador 1'].upper()).center(30) + '\n'+'='*30)
        elif puntuacion_2 > puntuacion_1:
            print('\n'+'EL GANADOR ES'.center(30,'=') +'\n' + (jugadores['Jugador 2'].upper()).center(30) + '\n'+'='*30)
        else:
            print('\n'+'='*28+'\nLA PARTIDA TERMINÓ EN EMPATE\n'+'='*28+'\n')
    
        print('Puntuaciones:\n'+ jugadores['Jugador 1'] + ' ' + '='*10 + ' '+ str(puntuacion_1) + '\n' + jugadores['Jugador 2'] + ' ' + '='*10 + ' ' + str(puntuacion_2))

        registro_puntaciones.setdefault(jugadores['Jugador 1'],[])
        registro_puntaciones.setdefault(jugadores['Jugador 2'],[])

        registro_puntaciones[jugadores['Jugador 1']].append(puntuacion_1)
        registro_puntaciones[jugadores['Jugador 2']].append(puntuacion_2)

    else: 
        print("\n\n"+"¡ERROR!".center(30)+ "\n\nPuede que uno o más jugadores no estén registrados.Por favor regístrense antes de jugar\n\n")

def consulta():
    global registro_puntaciones
    puntuaciones_globales = {}
    
    if len(registro_puntaciones) == 0 :
        print('\n'+'¡ERROR!'.center(51))
        print('No hay puntuaciones registradas en la base de datos')
    else:
        while True:
            nombre = input("\nIngrese el nombre del jugador que desea consultrar: ")

            if nombre in registro_puntaciones.keys():
                
                print('\n'+'PARTIDAS DEL JUGADOR'.center(29,'='))
                for partida,puntuacion in enumerate(registro_puntaciones[nombre]):
                    print(f'Partida {partida+1}: obtuvo {puntuacion} puntos')
                print('='*30)
                
                for jugador,puntuaciones in registro_puntaciones.items():
                    if jugador == nombre:
                        continue
                    
                    puntuacion_global = 0
                    
                    for partida in puntuaciones:
                        puntuacion_global += partida
                    puntuaciones_globales.setdefault(jugador,puntuacion_global)
                
                puntuaciones_ordenadas = list(reversed(sorted(puntuaciones_globales.items(), key=operator.itemgetter(1))))


                puntuaciones_globales = {}

                for element in puntuaciones_ordenadas:
                    puntuaciones_globales[element[0]] = element[1]
                print('PUNTUACIONES GLOBALES'.center(29,'='))

                for jugador,puntuacion_global in puntuaciones_globales.items():
                    print(f"{jugador}---------{puntuacion_global}")
                print('='*30)
                break
            print("\n¡Eror!. Ingrese un nombre que se encuentre disponible en la base de datos.")

def menu():
    global jugadores
    print('\n'+'ELIJA UNA OPCIÓN'.center(30,'-')+'\n'+'1.Registrar Jugadores'.ljust(30,'-')+'\n'+'2.Verificar puntuaciones'.ljust(30,'-')+'\n'+'3.Jugar'.ljust(30,'-')+'\n'+'4.salir'.ljust(30,'-'))
    opcion = int(input('\n'+ 'Selección: '))

    if opcion == 1:
        jugadores = registro()
        menu()
    elif opcion == 2:
        consulta()
        menu()
    elif opcion == 3:
        juego(jugadores)
        menu()
    elif opcion == 4:
        print('\n'+'Saliendo del programa...'.center(30))
        print('\n'+'Que tenga buen dia!'.center(30))
    else:
        print('\nError! Elija una opción válida...\n')
        menu()

if __name__ == '__main__':
    registro_puntaciones = {}
    jugadores = {}
    menu()
#Colorear prints
#Documentar el funcionamiento