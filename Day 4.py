# #Exercise 1
# import random
# item=['Heads','Tails']
# coin=random.choice(item)
# print(f'{coin}')

#Exercie 2
# import random
# item=[]

# name = input('Give first name:')
# item.append(name)
# name = input('Give 2nd name:')
# item.append(name)
# name = input('Give 3rd name:')
# item.append(name)

# one_name= random.choice(item)
# print(one_name)

#Exercise 3
# row = ['1','1','1']
# row1 = ['1','1','1']
# row2 = ['1','1','1']
# grid = [row, row1, row2]
# pos_row = int(input('pick row 1-3: '))
# pos_col = int(input('Pick col 1-3: '))
# grid[pos_row -1][pos_col-1] = '0'

# print(row)
# print(row1)
# print(row2)

#Final Exercise
import random
print('What do you choose?')
attack= int(input('0=rock\n1=paper\n2=scissors\npick: '))
count = ['rock','paper','scissors']
Ai= random.choice(count)
result = ['You Win', 'You Lose', 'Its a draw a lol']

if attack == 0: 
    print('you chose: Rock')
    print(f'The AI chose: {Ai}')
elif attack == 1:
    print('you chose: Paper')
    print(f'The AI chose: {Ai}')
elif attack == 2:
    print('you chose: Scisor')
    print(f'The AI chose: {Ai}')
else:
       print('lol')
       

if attack == 0 and Ai == 'rock':
    print("Draw")
elif attack == 0 and Ai == 'paper':
    print("You lose")
elif attack == 0 and Ai == 'scissors':
    print("You won")

if attack == 1 and Ai == 'rock':
    print("You Won")
elif attack == 1 and Ai == 'paper':
    print("Draw")
elif attack == 1 and Ai == 'scissors':
    print("You lose")

if attack == 2 and Ai == 'rock':
    print("You lose")
elif attack == 2 and Ai == 'paper':
    print("You Win")
elif attack == 2 and Ai == 'scissors':
    print("Draw")

#better version
# import random

# print("What do you choose?")
# attack = int(input("0 = rock\n1 = paper\n2 = scissors\npick: "))

# choices = ["rock", "paper", "scissors"]
# ai = random.choice(choices)

# print(f"You chose: {choices[attack]}") #so nmili ng index num base sa inputed num sa aattack variabale
# print(f"The AI chose: {ai}")

# # Draw condition
# if choices[attack] == ai:
#     print("It's a draw lol")

# # Winning conditions
# elif (
#     (choices[attack] == "rock" and ai == "scissors") or
#     (choices[attack] == "paper" and ai == "rock") or
#     (choices[attack] == "scissors" and ai == "paper")
# ):
#     print("You Win")

# # Losing condition
# else:
#     print("You Lose")

