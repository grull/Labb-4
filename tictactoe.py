# -*- coding: utf-8 -*-
import tictactoe_functions
import random

# skapar ett spelplan med storleken size
# och tecknet sign
def createGamePlan(size, sign):
  gPlan = []
  row = [sign]*size
  for i in range(size):
    gPlan.append(row[:])
  return gPlan

# Skriver ut spelplanet gamePlan 
# utrustad med rad- och kolumnnumrering
def showGamePlan(gamePlan):
  i = 0
  numbers=list(range(0,len(gamePlan)))
  rowNr = [" "]+numbers
  for row in [numbers]+gamePlan:
    print(rowNr[i],end = " ")
    i += 1
    for cell in row:
      print(cell,end = " ")
    print()


# uppdaterar rutan i rad row och
#  kolumn col med tecknet sign
def updateGamePlan(row,col,gamePlan,sign):
  gamePlan[row][col] = sign
  return True

# Returnerar True om det finns en ledig ruta
# i spelplanet gamePlan och False annars
def anyVacantBoxes(gamePlan,EMPTY):
  for i in range(0,SIZE)
    if EMPTY in gamePlan[i]:
      return True
  return False

# Frågar användaren efter rad och kolumn, funktionen
# upprepar fråga tills de angiven rad och kolumn
# är giltiga. 
# Giltiga rad och kolumn har följande krav:
# 1. de är tal
# 2. de är inte negativa tal
# 3. de är inte rad och kolumn för en cell som redan är upptagen
# 4. de är inte större än spleplanens storlek
def humanSelectABox(sign):
  print("\n---Din tur ("+sign+")---")
  row = int(input("Ange raden:"))
  col = int(input("Ange columnen:"))
  return row,col


# Funktionen anropar andra funktioner
# så att: 
# 1. spelare/datorn ska välja en ruta
# 2. spelplanet uppdateras
# 4. kontrolleras om det finns vinnare eller spelplnet är full 
#    och i båda fallen spelet ska avslutas med ett meddelande
def play2win(gamePlan, sign, message,WINROW,EMPTY,HUMAN):
  if sign == HUMAN:
    row,col = humanSelectABox(sign)
  else:
    row,col = tictactoe_functions.computerSelectABox(gamePlan,sign,EMPTY)

  updateGamePlan(row,col,gamePlan,sign)
  if not anyVacantBoxes(gamePlan,EMPTY):
    print("No winner!")
    return True
  if(tictactoe_functions.lookForWinner(gamePlan,row,col,WINROW)):
    print(message)
    return True
  return False





#huvudprogrammet
if __name__ == "__main__":
  #konstanter
  WINROW = 3
  SIZE = 3

  playersInfo = (("X","\n****** You won! ******\n"), ("O", "\n****** Computer won! ******\n"))
  playerIndx = random.choice([0,1])
  gamePlan = createGamePlan(SIZE, "-")
  showGamePlan(gamePlan)
  gameFinished = False
  while not gameFinished:
    gameFinished = play2win(gamePlan, playersInfo[playerIndx][0], playersInfo[playerIndx][1],3,"-","X")
    showGamePlan(gamePlan)

    if playerIndx == 0:
      playerIndx = 1
    else:
      playerIndx = 0
