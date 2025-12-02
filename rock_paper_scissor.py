import random

choices = ('r','p','s')

while True:
  user_choice = input('rock, paper, or scissor (R,P,S):').lower()
  if user_choice not in choices:
    print("Invalid choice!")
  #random choice 
  computer_choice = random.choice(choices)

  print(f"you chose {user_choice}")
  print(f"computer chose {computer_choice}")

  if user_choice == computer_choice:
    print("Its tie!")
  elif(
    (user_choice =='R' and computer_choice =='S') or\
    (user_choice =='S' and computer_choice =='P') or\
    (user_choice =='P' and computer_choice =='R')):
   print("You Win")
  else:
    print("you lose")

    play_again =input( "Do u want to play again? (y/n):").lower()
    if play_again !='y':
       print("Thanks for playing!")
       break
    
