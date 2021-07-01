#jugadores y puntajes.
import random, operator, string
#jugadores = {}
jugadores = {'CARLOS':[23,48,95,34,23],'ENRIQUE':[45,23,18,90,12],'GABRIEL':[45,56,32,45,78],'MIROS':[56,56,98,23,45],'CHRISTIAN':[56,23,34,78,15]}
Puntos = {}

# menu.
def menu():
  print("\033[1;32m"+'\nMenu Principal')
  print('\033[1;30m'+'\nElija una opción:'+"\033[0;34m"+'\n1.-Registrar Jugador\n2.-Consultar puntuaciones\n3.-Jugar\n4.-Salir')

  select = input('Selección: ')

  if select == '1':
    registro()
    menu()
  elif select == '2':
    consulta()
    menu()
  elif select == '3':
    jugar()
    menu()
  elif select == '4':
    print("\033[1;35m"+'\nGracias por jugar.\n¡Que tenga buen día!')
  else: 
    print("\033[0;31m"+'\n¡Error! Seleccione una opción válida')
    menu()

# registra jugadores
def registro():
  print("\033[1;32m"+'\n¡Bienvenido al Registro de jugadores!:D',"\033[1;30m")

  if len(jugadores) <= 1:
    print("\033[1;34m"+'\n---Recuerde que debe registrar dos jugadores para comenzar una partida---',"\033[1;30m")

  #variable para registrar un nuevo jugador. 
  jugador= input('\nIngrese el nombre del nuevo jugador: ')
  jugador= jugador.upper() 

  if jugador in jugadores:#Verifica si el jugador ingresado se encuentra ya registrado
    print("\033[3;31m"+'\nEste jugador ya se encuentra registrado. ¡Si continua se reiniciarán sus puntuaciones!'+'\033[0;34m'+'\n1.-Continuar\n2.-Cancelar registro',"\033[1;30m")
    select = input('\n¿Desea continuar?: ')
    
    if select == '1':
      jugadores[jugador]=[]
      print("\033[1;36m"+"\033[3;36m"+'\n¡Puntuación Reestablecida!')
      reg_2()
    elif select == '2':
      print("\033[0;36m"+"\033[3;36m"+"\033[1;36m"+'\nVolviendo al registro...',"\033[0;32m")
      registro()
    else:
      print("\033[1;37;41m"+'\n¡Opcion invalida!',"\033[0;36m"+"\033[3;36m"+ "\nSaliendo al menu...")
  else:
    jugadores[jugador]= []#Define una lista d epuntuaciones vacia para nuevo jugador
    print("\033[3;36m"+'\n¡Registro Existoso!')
    reg_2()

# consultar puntuaciones 
def consulta():
  print("\033[1;32m"+"\nCONSULTA DE PUNTUACIONES","\033[0;30m")
  jugador = input("\n¿A que jugador desea consultar? ")
  jugador = jugador.upper()

  if jugador in jugadores: #confirma que el jugador esta registrado.
    print("\033[1;34m"+"------\nPuntuaciones de: {}\n------".format(jugador))

    for indice,partida in enumerate(jugadores[jugador]):  #imprime las puntuaciones del jugador.
      print("\033[0;34m"+"Puntuacion de la partida {}: {} Puntos".format((indice+1),(partida)))

    if len(jugadores[jugador]) == 0: #error en caso de que el jugador no haya jugado.
      print("\033[1;36m"+"\033[3;36m"+"Este jugador no ha realizado una partida.")
    print("\033[1;34m"+"-------\nPuntuaciones globales de todos los jugadores:\n-------")

    for jugador in jugadores: #Genera un diccionario con las puntuaciones totales de los jugadores
      puntuacion_total = 0
      for partida in jugadores[jugador]:
        puntuacion_total += partida
      Puntos[jugador] = puntuacion_total
    puntuaciones_globales = dict(sorted(Puntos.items(), key=operator.itemgetter(1),reverse=True))#ordena el diccionario
    contador = 1

    for jugador in puntuaciones_globales: #Imprime la tabla de puntuaciones
      print("\033[0;34m"+"{}° lugar {} con {} puntos".format ((contador),(jugador),(puntuaciones_globales[jugador])))
      contador += 1

    print("\033[0;30m"+"\n¿Desea consutar la puntuacion de otro jugador?","\033[0;34m"+"\n1.-Si \n2.-No")
    select = input('Selección: ')

    if select == '1':
      consulta()
    elif select == '2':
      print("\033[1;30m"+'\nSaliendo al menu...')
    else: 
      print("\033[1;37;41m"+"\n¡Error!","\033[0;36m"+ "\033[3;36m"+"\nSaliendo al menu...")

  else:
    print("\033[3;31m"+"\033[1;31m"+"\n¡El jugador que desea consultar no se encuentra registrado!")
  
def jugar():

  # confirma que los jugadores estan registrados.
  if len(jugadores) < 2: 
    print("\033[1;32m"+'INICIANDO JUEGO...')
    print("\033[3;31m"+"\033[1;31m"+"\nError, debe haber al menos dos jugadores registrados para poder jugar\n","\033[0;30m")
    
  else:
    jugador_1 = input('\nIngrese el nombre del primer jugador para confirmar el registro: ')
    jugador_1 = jugador_1.upper()
    jugador_2 = input('\nIngrese el nombre del segundo jugador para confirmar el registro: ')
    jugador_2 = jugador_2.upper()

    if (jugador_1 in jugadores) and (jugador_2 in jugadores):
      print("\033[3;36m"+f'\n¡Confirmación exitosa!')
      print("\033[1;32m"+f"\nJUGADOR 1: {jugador_1}","\033[1;35m"+f"\nJUGADOR 2: {jugador_2}\n","\033[1;30m")

      letra_inicio = random.choice(string.ascii_letters)
      letra_inicio = letra_inicio.upper()

      jugador_actual = 1

      palabras_ingresadas_1,palabras_ingresadas_2 = 0,0

      puntuacion_1, puntuacion_2 = 0,0

      puntos = 0

      vidas_1, vidas_2 = 3,3

      registro_palabras = []

      error = False

      while ((vidas_1 > 0) and (vidas_2 > 0)) and ((palabras_ingresadas_1< 21) and (palabras_ingresadas_2< 20)): #Juego principal
        palabra_ingresada = input(f'\n-----Turno del jugador {jugador_actual}----- \nIngrese una palabra  que inicie con la letra {letra_inicio}--->\n')
        palabra_ingresada = palabra_ingresada.upper()

        if palabra_ingresada[0] != letra_inicio:
          print("\033[1;37;41m"+"\n¡Error!" "\033[0;31m"+"\033[1;31m"+"\033[3;31m"+f"\nRecuerda que debe iniciar con la letra --> {letra_inicio}")
          error = True
          if jugador_actual == 1:
            vidas_1 -= 1
          else:
            vidas_2 -= 1
          continue
        
        letra_inicio = palabra_ingresada[len(palabra_ingresada)-1]

        if error:
          puntos = 0
          if len(palabra_ingresada) > 7:
            puntos = 4
          elif len(palabra_ingresada) == 7:
            puntos = 3
          elif len(palabra_ingresada) == 6:
            puntos = 2
          elif len(palabra_ingresada) == 5:
            puntos = 1
          elif len(palabra_ingresada) == 4:
            puntos = 0.5
        else:
          puntos = 1
          if len(palabra_ingresada) > 7:
            puntos = 6
          elif len(palabra_ingresada) == 7:
            puntos = 5
          elif len(palabra_ingresada) == 6:
            puntos = 4
          elif len(palabra_ingresada) == 5:
            puntos = 3
          elif len(palabra_ingresada) == 4:
            puntos = 2
      
        error = False

        if palabra_ingresada in registro_palabras:
          puntos = 0
        else:
          registro_palabras.append(palabra_ingresada)
        
        print("\033[1;32m"+f"\nJugador {jugador_actual}""\033[4;30m"+f"\nSuma {puntos} Puntos\n")
        
        if jugador_actual == 1:
          palabras_ingresadas_1 += 1
          puntuacion_1 += puntos
          jugador_actual = 2
        else:
          palabras_ingresadas_2 += 1
          puntuacion_2 += puntos
          jugador_actual = 1
        
        
      if puntuacion_1 > puntuacion_2: #Define al ganador
        print("\033[1;30;47m"+f'\nEl ganador es: {jugador_1}\n')
      elif puntuacion_2 > puntuacion_1:
        print("\033[1;30;47m"+f'\nEl ganador es: {jugador_2}\n')
      else:
        print("\033[1;30;47m"+'\nLa partida terminó en empate\n')

      #impresión de puntuaciones
      print("\033[4;34m"+"\033[0;34m"+"\033[1;34m"+"------PUNTUACIONES-----")
      print("\033[0;34m"+"\033[1;34m"+"\033[1;32m"+f"\n{jugador_1}:{puntuacion_1} Puntos""\033[0;35m"+"\033[1;35m"+f"\n{jugador_2}:{puntuacion_2} Puntos")
      
      #agrega la puntuacion al historial de los jugadores
      jugadores[jugador_1].append(puntuacion_1)#agrega la puntuacion al historial de los jugadores
      jugadores[jugador_2].append(puntuacion_2)

    else:
      print("\033[1;31m"+"\033[3;31m"+"\n¡Puede que uno o más jugadores no estén registrados!.\nPor favor regístrense antes de jugar.\n")

def reg_2(): #Regresa al registro si el usuario lo deseaA
  print("\033[0;30m"+'\n¿Quieres registrar otro jugador?'+"\033[0;34m"+'\n1.-Sí\n2.-No\n')
  select = input('Selección: ')

  if select == '1':
    registro()
  elif select == '2':
    print("\033[3;36m"+"\033[1;36m"+'\nSaliendo al menu...')
  else: 
    print("\033[1;37;41m"+"\n¡Error!","\033[0;36m"+ "\033[3;36m"+"\nSaliendo al menu...")

#Programa principal
print("\033[1;35m"+"BIENVENIDO AL JUEGO DE LAS PALABRAS ENCADENADAS")
menu()