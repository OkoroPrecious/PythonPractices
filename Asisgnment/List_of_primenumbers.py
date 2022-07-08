# # rng = list(range(1, 100, 5))
# # range 1 to 100 and increment by 5
# numbers = list(range(1, 100))
def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# prime num

def is_prime(num: int) -> bool:
    max_divisor = (num // 2) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True
