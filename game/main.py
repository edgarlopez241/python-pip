import random
print('*'*10)
print('Escoja una opcion\n')

winP = 0
winC = 0
tied = 0
rounds = 1

while True:
    print('*'*10)
    print('Marcador')
    print(f'Computadora {winC}')
    print(f'Jugador {winP}')
    print(f'Empates {tied}')
    print('*'*10)
    print('Ronda n°', rounds)
    rounds += 1
    userOption = int(input("1 piedra, 2 papel o  3 tijera  \n"))
    print('*'*10)
    computerOption = random.randint(1,3)
    strOptP = ''
    if userOption ==1:
      strOptP = 'Piedra' 
    elif userOption ==2:
      strOptP = 'Papel'
    else :
      strOptP = 'Tijera'
    
    strOptC = ''
    if computerOption == 1:
      strOptC = 'Piedra' 
    elif computerOption ==2:
      strOptC = 'Papel'
    else :
      strOptC = 'Tijera'
    
    
    if userOption == computerOption:
       print(f"Empate, ambos eligieron {strOptP}")
       tied += 1
      
    elif userOption == 1 and computerOption==2:
        print(f"Perdiste, eligiste {strOptP} y la computadora eligio {strOptC}")
        winC += 1
    elif userOption == 1 and computerOption==3:
        print(f"Ganaste, eligiste {strOptP} y la computadora eligio {strOptC}")
        winP += 1
    elif userOption == 2 and computerOption==1:
        print(f"Ganaste, eligiste {strOptP} y la computadora eligio {strOptC}")
        winP += 1
    elif userOption == 2 and computerOption==3:
      print(f"Perdiste, eligiste {strOptP} y la computadora eligio {strOptC}")
      winC += 1
    elif userOption == 3 and computerOption==1:
      print(f"Perdiste, eligiste {strOptP} y la computadora eligio {strOptC}")
      winC += 1
    elif userOption == 3 and computerOption==2:
      print(f"Ganaste, eligiste {strOptP} y la computadora eligio {strOptC}")
      winP += 1
      print('*'*10)
    if winP == 3:
      print (f'El ganador es el Jugador')
      break
    if winC == 3:
      print (f'El ganador es la Computadora')
      break