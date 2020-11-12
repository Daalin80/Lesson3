import random
kol = 0
number = random.randint(1, 10)
while kol < 3:
    print("Try to guess a number from 1 to 10: ")
    guess = int(input())
    kol += 1
    if guess < number:
        print("More")
    if guess > number:
        print("Less")
    if guess == number:
        print("YOU WON JACKPOT!")
        break
if guess != number:
    print("YOU LOSE EVERYTHING!")
