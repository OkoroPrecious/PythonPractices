user_input = int(input("Enter an integer: "))

square_number = user_input * user_input

if user_input and square_number > 100:
    print(user_input, "and", square_number, "are greater than 100")
elif user_input and square_number < 100:
    print(user_input, "and", square_number, "are less than 100")

elif user_input and square_number == 100:
    print(user_input, "and", square_number, " are equal to 100")

else:
    print(user_input, "and", square_number, "are not equal than 100")
