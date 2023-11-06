import random
while True:
  player=str(input("enter the choice of rock, paper and scissors:"))
  computer=random.choice(["rock","paper","scissors"])
  if player==computer:
    print("tie")
  elif player=="rock":
    if computer=="paper":
      print(f"you loss {computer} covers {player}")
    else:
      print(f"you win {player} smashed {computer}")
  elif player=="paper":
    if computer=="scissors":
      print(f"you loss {computer} cut {player}")
    else:
      print(f"you win {player} coveded {computer}")
  elif player=="scissors":
    if computer=="rock":
      print(f"you loss {computer} smashed {player}")
    else:
      print(f"you win {player} cut {computer}")
  else:
    print("check the spelling ")
