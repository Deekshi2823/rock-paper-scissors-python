import random 
Rock,Paper,Scissors=0,1,2
num=int(input("Enter your choice(0-Rock/1-Paper/2-Scissors):"))
ran=random.randint(0,2)
print("Computer choice:",ran)
if num==ran:
  print("Draw")
elif (num==0 and ran==2) or (num==1 and ran==0) or (num==2 and ran==1):
  print("You won")
else:
  print("Computer Won")
