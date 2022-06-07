for num in range(1, 101):
    #  if num % 15 == 0:
    #     print("Buzz Fizz")
    #
    # elif num % 3 == 0:
    #     print("Buzz")
    # elif num % 5 == 0:
    #     print("Fizz")
    #
    # else:
    #     print(num)

    if not num % 15:
        print("Buzz Fizz")

    elif not num % 3:
        print("Buzz")
    elif not num % 5:
        print("Fizz")

    else:
        print(num)