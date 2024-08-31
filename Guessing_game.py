import random
random_number = random.randint(1,100)
print(random_number)
tries = 0
while True:
    tries = tries + 1
    print("Hello there!!!, Welcome to my guessing game. Try to guess a number between 1-100 to win the game")
    user_guess = int(input("Guess the number: "))
    if tries > 4:
        print("You have exceeded your limit of trials! Try again next time,thank you!!")
        break
    if user_guess < random_number:
        print(" You are wrong, try a higher number")
    if user_guess > random_number:
        print(" You can do it, go lower")
    if user_guess == random_number:
        print (f"Congratulations, you won the game after {tries} tries, you are a genius !!!")
        break
    