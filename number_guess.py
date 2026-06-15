import random

print("---Number Guessing Game---")
print("Guess a Number between 1 and 100 ")

#generate the random number between 1 and 100
number =random.randint(1,100)
attempts = 0

while True:
    try:
      guess = int(input("Enter your Guess:"))
      attempts +=1
    #check the guess
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print(f"Congratulations!  You Guessed it in {attempts} attempts ")
        break
