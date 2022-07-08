# lst = [i**2 for i in range(1, 11)]
# print(lst)
# if no condition
#
# lst = [i**2 for i in range(1, 11) if i % 2 == 0]
# print(lst)
# # if there is condition
#
# lst = ["even" if 3 % 2 == 0 else "odd"]
# print(lst)

# print(lst)
# it prints out even and double it, then leave odd number in it raw num


# lst = [int(input(f"Enter student {i }'s score: ")) for i in range(1, 6)]
# print(lst)
#
# lst = sum([int(input(f"Enter student {i }'s score: ")) for i in range(1, 6)])
# print(lst)

lst = [int(input(f"Enter student {i}'s score: ")) for i in range(1, 6)]
print(lst)
print("Total Scores = ", sum(lst))
print("Max = ", max(lst))
print("Min = ", min(lst))
print("Average = ", sum(lst) / len(lst))


# prime number

# primes = [i for i in range(1, 101) if is_prime(i)]
# print(primes)


def cube(num: int) -> int:
    return num ** 3


cubes = [cube(i) for i in range(1, 11)]
print(cubes)
