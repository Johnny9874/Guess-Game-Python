import random

 

ComputerChoice = random.randint(1,100)

 

attempts = 1

 

print("Be carefull, you only have 7 attempts in total !")

guess = int(input("Enter your guess: "))

 

while(guess != ComputerChoice):

  if guess > ComputerChoice:

    print("Too high, try again")

  else:

    print("Too low, try again")

 

  attempts += 1

 

  guess = int(input("Enter your guess: "))

 

  if attempts == 7:

    print("Game over ! U reach the limit ammount of attempts !")

    break

 

  if guess == ComputerChoice:

    print(f"U won in {attempts} attempts !")

 

play_again = "yes"

 

input("Do you want to play again ? (yes/no)")

 

while play_again.lower() == "yes":

  ComputerChoice = random.randint(1,100)

 

  attempts = 1

 

  guess = int(input("Enter your guess: "))

 

  while(guess != ComputerChoice):

    if guess > ComputerChoice:

      print("Too high, try again")

    else:

      print("Too low, try again")

 

    attempts += 1

 

    guess = int(input("Enter your guess: "))

 

    if attempts == 7:

      print("Game over ! U reach the limit ammount of attempts !")

      break

 

    if guess == ComputerChoice:

      print(f"U won in {attempts} attempts !")

  input("Do you want to play again ? (yes/no)")