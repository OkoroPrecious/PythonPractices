lst = [1, 2, 3, 4]

# try:
#     s = lst[9]
#     print("I did well")
# except IndexError as e:
#     print(f"Error occurred: {e}")
#

# When in a try and any error occurs, the except block will execute
# But when no error occur, the try block executes
# You  can  catch any error by using just the except keyword
# You can catch multiple exception
# When there are multiple errors, the first one is caught first and the exception message displays

lst = [1, 2, 4]


# def raise_exception():  # customized exception
#     raise ValueError("This is just whining you with exception")
#
#
# try:
#     d = 4 + "I"
#     s = lst[9]
#     print("I did well")
#
# except IndexError as e:
#     print(f"Index out of bounds: {e}")
# except TypeError as e:
#     print(f"Error of no type: {e}")
# finally:
#     print("I am from finally")

# Browse python Built in exceptions to see all.
# finally block is always executed if or no error.
# except, else and finally runs when there is an error


def square(s: int | float) -> int | float:
    if isinstance(s, int | float):  # isinstance means type of
        return s * s
    raise ValueError("I can only square an integer or a float")

try:
    print(square([7]))
except IndexError as e:
    print(f"Error occurred: {e}")

except (TypeError, ValueError) as e:
    print(f"Error occurred: {e}")

finally:
    print("Done")




