# random is a built-in Python module used to generate random values.

# import random
#
# fruits = ["Apple", "Orange", "Mango", "Banana"]
#
# print(random.choice(fruits))

# random → module

# print(random.randint(1,10))

# randint → function inside that module

# 1. Coin toss

# coin=["heads","tails"]
#
# print(random.choice(coin))

# 2. Rock paper scissors game

# human = ["rock", "paper", "scissors"]
# system = ["rock", "paper", "scissors"]
#
# while True:
#     human_choice = input("Enter rock, paper, or scissors: ").lower()
#
#     if human_choice not in human:
#         print("Invalid input")
#         break
#
#     system_choice = random.choice(system)
#
#     print("Human:", human_choice)
#     print("System:", system_choice)
#
#     if human_choice == system_choice:
#         print("It's a tie")
#
#     elif (human_choice == "rock" and system_choice == "scissors") or \
#          (human_choice == "paper" and system_choice == "rock") or \
#          (human_choice == "scissors" and system_choice == "paper"):
#         print("Human wins")
#
#     else:
#         print("System wins")

# Symbol      Purpose
#
# Backslash \         Continue code on the next line
#
# Newline \n         Print a new line

# 1. .lower() — Convert to lowercase
#
# name = "HARIGESH"
# print(name.lower())
#
# 2. .upper() — Convert to uppercase
#
# name = "harigesh"
# print(name.upper())
#
# 3. .capitalize() — Capitalize the first letter
#
# name = "harigesh"
# print(name.capitalize())

# 3. Dice GAME

# def player():
#     initial = random.randint(1, 6)
#     score = 0
#
#     for i in range(initial):
#         b = random.randint(1, 6)
#         score += b
#
#     return score
#
# player1 = player()
# player2 = player()
#
# print(player1, player2)
#
# if player1 > player2:
#     print("player 1 wins")
#
# elif player2 > player1:
#     print("player 2 wins")
#
# else:
#     print("its a draw")

# 4. RPG game

# import random
#
# enemyhp = 100
# playerhp = 100
#
# while playerhp > 0 and enemyhp > 0:
#
#     print("\nPlayer HP:", playerhp)
#     print("Enemy HP:", enemyhp)
#
#
#     player_damage = random.randint(1, 20)
#     enemyhp = enemyhp - player_damage
#
#     print("Player attacks enemy for", player_damage, "damage!")
#
#     if enemyhp <= 0:
#         print("Enemy defeated! You win!")
#         break
#
#
#     enemy_damage = random.randint(1, 20)
#     playerhp = playerhp - enemy_damage
#
#     print("Enemy attacks player for", enemy_damage, "damage!")
#
#     if playerhp <= 0:
#         print("Player defeated! Game over!")
#
# print("\nGame finished!")






