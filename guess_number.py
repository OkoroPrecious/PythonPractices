import random

correct_guess = random.randint(0, 100)
count = 0

while count < 5:
    guess = int(input("Guess a number: "))
    if guess < 0 or guess > 100:
        print("out of range...")
        break

    if guess < correct_guess:
        print("Too low, try again")
    elif guess > correct_guess:
        print("Too high")
    else:
        print("Awesome, You are correct")
        break

    count += 1

else:
    print("You tried, exceeded your number of chanced")
    print("The correct number is ", correct_guess)
