import random, time

def singleplayer():
  jackpots=0
  twos=0
  nones=0
  end=False
  JackpotMoney=500
  TwoMatchMoney=35
  NoneMatchMoney=5
  print("Roll A Number\n\n")
  money=200
  play=input("Do you want to play you can win money(Not Real): ")
  print("\n\n")
  if play=='yes' or play=='Yes' or play=='y' or play=='Y':
    while end==False:
      print("You have "+str(money)+" dollars left\n\n")
      spin=int(input("How many spins would you like to do. It costs 10 dollars for one spin. Or type -1 to auto spin: "))
      print("\n\n")
      if money >= 10*spin and spin !=-1:
        for loop in range(spin):
          money-=20
          x=random.randint(1,7)
          y=random.randint(1,7)
          z=random.randint(1,7)
          print(str(x)+" "+str(y)+" "+str(z))
          if x==y and y==z: #spin=same equal prize
            print("JACKPOT")
            print("All matched")
            print("+"+str(JackpotMoney)+"$\n\n")
            money+=JackpotMoney
            jackpots+=1
            time.sleep(3)
          elif x==y or y==z or x==z:
            print("Two matched")
            print("+"+str(TwoMatchMoney)+"$\n\n")
            money+=TwoMatchMoney
            twos+=1
          else:
            print("None matched")
            print("+"+str(NoneMatchMoney)+"$\n\n")
            money+=NoneMatchMoney
            nones+=1
          time.sleep(1)
      if money < 20:
        if money >= 0:
          print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        elif money < 0:
          iou=0-money
          money+=iou
        print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        time.sleep(5)
        quit()
      elif spin==-1:
        while money >=10:
          money-=20
          x=random.randint(1,7)
          y=random.randint(1,7)
          z=random.randint(1,7)
          print(str(x)+" "+str(y)+" "+str(z))
          if x==y and y==z: #spin=same equal prize
            print("JACKPOT")
            print("All matched")
            print("+"+str(JackpotMoney)+"$\n\n")
            money+=JackpotMoney
            jackpots+=1
            time.sleep(3)
          elif x==y or y==z or x==z:
            print("Two matched")
            print("+"+str(TwoMatchMoney)+"$\n\n")
            money+=TwoMatchMoney
            twos+=1
          else:
            print("None matched")
            print("+"+str(NoneMatchMoney)+"$\n\n")
            money+=NoneMatchMoney
            nones+=1
          time.sleep(1)
      if money < 20:
        if money >= 0:
          print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        elif money < 0:
          iou=0-money
          money+=iou
        print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        time.sleep(5)
        quit()
  if play=='no' or play=='No':
    quit()
    
def multiplayer():
  end=False
  jackpots=0
  twos=0
  nones=0
  JackpotMoney=500
  TwoMatchMoney=35
  NoneMatchMoney=5
  while end==False:
      money=200
      print("P1 You have "+str(money)+" dollars left\n\n")
      spin=int(input("How many spins would you like to do. It costs 10 dollars for one spin. Or type -1 to auto spin: "))
      print("\n\n")
      if money >= 10*spin and spin !=-1:
        for loop in range(spin):
          money-=20
          x=random.randint(1,7)
          y=random.randint(1,7)
          z=random.randint(1,7)
          print(str(x)+" "+str(y)+" "+str(z))
          if x==y and y==z: #spin=same equal prize
            print("JACKPOT")
            print("All matched")
            print("+"+str(JackpotMoney)+"$\n\n")
            money+=JackpotMoney
            jackpots+=1
            time.sleep(3)
          elif x==y or y==z or x==z:
            print("Two matched")
            print("+"+str(TwoMatchMoney)+"$\n\n")
            money+=TwoMatchMoney
            twos+=1
          else:
            print("None matched")
            print("+"+str(NoneMatchMoney)+"$\n\n")
            money+=NoneMatchMoney
            nones+=1
          time.sleep(0.75)
        if money < 20:
          print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
          time.sleep(5)
          quit()
      elif spin==-1:
        while money >=10:
          money-=20
          x=random.randint(1,7)
          y=random.randint(1,7)
          z=random.randint(1,7)
          print(str(x)+" "+str(y)+" "+str(z))
          if x==y and y==z: #spin=same equal prize
            print("JACKPOT")
            print("All matched")
            print("+"+str(JackpotMoney)+"$\n\n")
            money+=JackpotMoney
            jackpots+=1
            time.sleep(3)
          elif x==y or y==z or x==z:
            print("Two matched")
            print("+"+str(TwoMatchMoney)+"$\n\n")
            money+=TwoMatchMoney
            twos+=1
          else:
            print("None matched")
            print("+"+str(NoneMatchMoney)+"$\n\n")
            money+=NoneMatchMoney
            nones+=1
          time.sleep(0.75)
      if money < 20:
        if money >= 0:
          print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        elif money < 0:
          iou=0-money
          money+=iou
        print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        p1money=money
        end=True
        quit()
  jackpots=0
  twos=0
  nones=0
  while end==False:
      money=200
      print("P1 You have "+str(money)+" dollars left\n\n")
      spin=int(input("How many spins would you like to do. It costs 10 dollars for one spin. Or type -1 to auto spin: "))
      print("\n\n")
      if money >= 10*spin and spin !=-1:
        for loop in range(spin):
          money-=20
          x=random.randint(1,7)
          y=random.randint(1,7)
          z=random.randint(1,7)
          print(str(x)+" "+str(y)+" "+str(z))
          if x==y and y==z: #spin=same equal prize
            print("JACKPOT")
            print("All matched")
            print("+"+str(JackpotMoney)+"$\n\n")
            money+=JackpotMoney
            jackpots+=1
            time.sleep(3)
          elif x==y or y==z or x==z:
            print("Two matched")
            print("+"+str(TwoMatchMoney)+"$\n\n")
            money+=TwoMatchMoney
            twos+=1
          else:
            print("None matched")
            print("+"+str(NoneMatchMoney)+"$\n\n")
            money+=NoneMatchMoney
            nones+=1
          time.sleep(0.75)
        if money < 20:
          if money >= 0:
            print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
          elif money < 0:
            iou=0-money
            money+=iou
          print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
          time.sleep(5)
          quit()
      elif spin==-1:
        while money >=10:
          money-=20
          x=random.randint(1,7)
          y=random.randint(1,7)
          z=random.randint(1,7)
          print(str(x)+" "+str(y)+" "+str(z))
          if x==y and y==z: #spin=same equal prize
            print("JACKPOT")
            print("All matched")
            print("+"+str(JackpotMoney)+"$\n\n")
            money+=JackpotMoney
            jackpots+=1
            time.sleep(3)
          elif x==y or y==z or x==z:
            print("Two matched")
            print("+"+str(TwoMatchMoney)+"$\n\n")
            money+=TwoMatchMoney
            twos+=1
          else:
            print("None matched")
            print("+"+str(NoneMatchMoney)+"$\n\n")
            money+=NoneMatchMoney
            nones+=1
          time.sleep(0.75)
      if money < 20:
        if money >= 0:
          print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        elif money < 0:
          iou=0-money
          money+=iou
        print("You won a profit of "+str(money-100)+" dollars. You got "+str(jackpots)+" jackpots and "+str(twos)+" two matches and "+str(nones)+" Non matching number groups\n\n")
        p2money=money
        end='score'
      quit()
  if end=='score':
    if p1money > p2money:
      print("P1 wins")
    elif p1money < p2money:
      print("P2 wins")
    elif p1money == p2money:
      print("Tie")
  print("P1 got "+str(p1money)+" dollars")
  print("And")
  print("P2 got "+str(p2money)+" dolars")
  

game=int(input("How many people are playing 1 or 2: "))
if game==1:
  singleplayer()
if game==2:
  multiplayer()
