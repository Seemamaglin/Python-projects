# -*- coding: utf-8 -*-
"""RockPaperScissors-Project1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IdEfnJ7QKpxHj3eu7-R_M44uVIoM0eIQ
"""

import random
user_choice=int(input("Enter the choice: 0 for Rock, 1 for Paper, 2 for Scissors."))
computer_choice=random.randint(0,2)
print("Computer choice:",computer_choice)
if computer_choice==user_choice:
    print("Draw")
elif user_choice==0 and computer_choice==1:
    print("You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif user_choice==1 and computer_choice==0:
    print("You win")
elif user_choice==1 and computer_choice==2:
    print("You lose")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif user_choice==2 and computer_choice==1:
    print("You win")
else:
    print("Enter valid input")