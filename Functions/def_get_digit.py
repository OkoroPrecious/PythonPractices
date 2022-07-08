def get_digit(number, position):
    return number // (10 ** position) % 10


digit = get_digit(5768, 2)
print(digit)
