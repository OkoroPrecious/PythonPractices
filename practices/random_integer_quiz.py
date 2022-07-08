import random

correct_guess = random.randint(0, 100)
count = 0

while count < 5:
    guess = int(input("Guess a number: "))
    if guess < correct_guess:
        print("Too low, try again")
    elif guess > correct_guess:
        print("Too high, try again")
    else:
        print("Awesome, You are correct")
        break
        
    count += 1
              
else:
    print("You tried, exceeded your number of chanced")

    print("The correct number is ", correct_guess)
