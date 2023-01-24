import random


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


user_choice_str = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:")
computers_choice = random.randint(0,2)

choice_list = [rock,paper,scissors]

win_matrix=[
    ['draw','win','lose'],
    ['lose','draw','win'],
    ['win','lose','draw']
    ]

if user_choice_str not in ('0','1','2'):
    print("You typed an invalid number, you lose! ")
else:
    user_choice = int(user_choice_str)
    print(f"{choice_list[user_choice]}\n")

    print(f"Computer chose: \n {choice_list[computers_choice]}")

    if win_matrix[computers_choice][user_choice] == "draw":
        print("It is a draw.")
    else:
        print(f"You {win_matrix[computers_choice][user_choice]}")
