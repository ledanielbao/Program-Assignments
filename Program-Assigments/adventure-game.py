# DANIEL LE 

def start():
  print("Welcome to the amusement park! Ready to have some fun?") 
  answer = input("Type (Y).")

  if answer == "Y":
    amusement_park()

  else:
    exit()

def amusement_park():
  print("You got lost in the amusement park; find the exit as soon as possible!")
  print("You come to a crossroads. To your right is a delapidated ferry ride, and to your left is a path that leads to a merry-go-round.")
  print("1). Ferry ride.")
  print("2). Merry-go-round.")
  answer = input("Which path do you choose? (1 or 2)")

  if answer == "1":
    print("You move down the path to the ferry, you find a bright shiny key on the floor. You pick it up.")
    gate()

  elif answer == "2":
    print("You fell in a pothole and died lol")
    game_over()

  else:
    game_over("Don't you know how to type something properly?")

def gate():
  print("\nYou continue moving forward and come to a gate.")
  print("You can go through the gate with the keys that you found (1), or you can move further down along on the path (2).")
  print("1). Go through the gate.")
  print("2). Go down the path.")
  answer = input("What do you do? (1 or 2)")

  if answer == "1":
    print("You go through the gate and find a janitor that takes you to the exit and you find your family waiting for you.")

  elif answer == "2":
    print("You continue down the path for all eternity, surviving off of bugs and sidewalk mulch. \nYou meet a few people along the way until you finally die of starvation.")
    game_over()

  else:
    print("Don't you know how to type something properly?")
    game_over()

def game_over():
  print("GAME OVER")
  play_again()

def play_again():
  print("Would you like to play again?")
  answer = input("(Y/N)")

  if answer == "Y":
    start()

  elif answer == "N":
    exit()