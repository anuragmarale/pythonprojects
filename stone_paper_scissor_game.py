rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_list=[rock,paper,scissors]
user_choise=int(input("0 for Rocks, 1 for paper, 2 for scissors: "))
if user_choise >= 3 or user_choise < 0:
  print("Invalid Input, you Lose")
else: 
  print(game_list[user_choise])
  comp_choise=random.randint(0,2)
  print(f"Computer's Play: {comp_choise}")
  print(game_list[comp_choise])

  if user_choise >= 3 or user_choise < 0:
    print("Invalid Input, you Lose") 
  elif user_choise == 0 and comp_choise== 2:
    print("You Win!!")
  elif comp_choise == 0 and user_choise == 2:
    print("You Lose")
  elif comp_choise > user_choise:
    print("You Lose")
  elif user_choise == comp_choise:
    print("It's a draw")
  elif user_choise > comp_choise:
    print("You Win!!")


