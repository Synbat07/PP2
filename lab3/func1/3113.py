print ("Hello! What is your name?")
name = input()

print ("Well ", name, """I am thinking of a number between 1 and 20.
       Take a guess.""")

num = int(input())

import random
rn = random.randint(1, 20)
attempts = 0

for i in range(20):
    if num < rn:
        print ("Your guess is too low.")
        attempts += 1
        num = int(input("Try again: "))
    elif num > rn:
        print ("Your assumption is too high.")
        attempts += 1
        num = int(input("Try again: "))
    else:
        print ("Good job ", name, "! You guessed my number in", attempts, "guesses!")
        break