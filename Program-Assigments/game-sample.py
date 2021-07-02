# DANIEL LE, SHAREEF ALIU, AVNOOR SINGH SIDHU


# amusement park - you will need to rename this function.
def amusement_park():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou got lost in the amusement park; find the exit as soon as possible!")
  print("You come to a crossroads. To your right is a delapidated ferry ride, and to your left is a path that leads to a merry-go-round.")
  print("1). Ferry ride.")
  print("2). Merry-go-round.")

  # get user input take input()
  answer = input("Which path do you choose? (1 or 2)")

  if answer == "1":
    # lead him to the gate()
    print("You move down the path to the ferry, you find a bright shiny key on the floor. You pick it up.")
  gate()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    print("You fell in a pothole and died lol")
    game_over()
  else:
    # game_over() with "reason"

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


# function to ask play again or not
def play_again():
  # use print statement to ask if user wants to play again
  print("Would you like to play again?")
  # get input
  answer = input("Y/N")
  # evaluate input using conditional 
  if answer == "Y":
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


def start():
  # have some introductory text printed like: ("\nYou are standing in a dark room.")
  print("Welcome to the amusement park! Ready to have some fun?") 
  # get user input using input() and save 
  answer = input("Type (Y).")

  # use a loop to manage game -- 

 # if x in input:
    # go to a function()
  if answer == "Y":
    amusement_park()
 # elif "r" in input:
    # go to another function()
  # elif:
    # go somewhere else
  # elif
    # go somewhere else
  else:
    # else go to game over function
    game_over("Don't you know how to type something properly?")


# calling start function. 
start()