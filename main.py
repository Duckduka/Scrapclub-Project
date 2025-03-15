#
from random import randint
# import time
bal = 500
day = 1

print ("Welcome to The fight of You and Luther!")

while(bal > 0):
  print("Day", day)
  thingu = input("Chose a Place (1,2,3)(or <<?>> if you are really risky)")
  # time.sleep(1)
  chance = randint(1,10)
  jc = randint(1,10000)
  Wierd = randint(-100000,100000)
  if (bal > 50000):
    print("You KILL the LUTHER")
    print("YOU WIN!!!!!")
    break
  if (thingu == "1"):
    if (chance >= 5):
      print("You lost 2 times your ammo.")
      bal = bal / 2
      print ("Current amount of ammo:",bal)
    elif(chance <=2):
      print ("You got a rare ammo! + 1000")
      bal = bal + 1000
      print ("Current amount of ammo:",bal)
    elif(chance == 4 or chance == 3):
      print("You lose half of your ammo")
      print ("Current amount of ammo:",bal)
      bal = bal/2

  elif(thingu == "2"):
    if (chance <= 8):
      print("You lost 400 ammo")
      bal = bal - 400
      print ("Current amount of ammo:",bal)
    elif(chance == 9):
      print ("You got a devil coin! - 2000")
      bal = bal - 2000
      print ("Current amount of ammo:",bal)
    elif(chance == 10 ):
      print("You got 5% of your ammo")
      print ("Current amount of ammo:",bal)
      bal = bal + bal * 0.05

  elif(thingu == "3"):
    if (chance == 1 or chance == 2):
      print("You got 3 times your ammo")
      bal = bal * 3
      print ("Current amount of ammo:",bal)
    elif(chance <=8):
      print ("You got a Chabba! +", jc)
      bal = bal + jc
      print ("Current amount of ammo:",bal)
    else:
      print("Luther suddenly punches you. You fall to the ground as he says: <<Good Game Snerk.>>")
      break

  elif(thingu == "?"):
    if (chance == 1 ):
      print("You got 10 ammo")
      bal = bal + 10
      print ("Current amount of ammo:",bal)
    elif(chance == 2):
      print ("You lost 10 ammo!",)
      bal = bal - 10
      print ("Current amount of ammo:",bal)
    elif (chance == 3 ):
      print("You got a 100 ammo")
      bal = bal + 100
      print ("Current amount of ammo:",bal)
    elif(chance == 4):
      print ("You lost 100 ammo!",)
      bal = bal - 100
      print ("Current amount of ammo:",bal)
    elif(chance == 5):
      print ("You got an ammo pack of 1000 ammo!",)
      bal = bal + 1000
      print ("Current amount of ammo:",bal)
    elif (chance == 6 ):
      print("You got a big ammo pack that gave you 5000 ammo!")
      bal = bal + 5000
      print ("Current amount of ammo:",bal)
    elif(chance ==  7):
      print ("You got an ammo curse, stealing and making you lose 5000 ammo!",)
      bal = bal - 5000
      print ("Current amount of ammo:",bal)
    elif(chance == 8):
      print ("You got a random amount of ammo!",)
      bal = bal + Wierd
      print ("Current amount of ammo:",bal)
    elif (chance == 9):
      print("You got alot of ammo! +10000 ammo")
      bal = bal + 10000
      print ("Current amount of ammo:",bal)
    elif(chance == 10):
      print ("You wasted a bunch of your ammo...  STUPIDDDDDDDD !",)
      bal = bal - 10000
      print ("Current amount of ammo:",bal)
  day = day + 1
  print()
  print("====================================================")
  # pa = input("Do you want to try to get ammo?(n)")
  # if (pa == "n"):
  #   break


print("You died! You survived for", day - 1, "days")
