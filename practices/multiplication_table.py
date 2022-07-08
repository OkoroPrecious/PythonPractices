# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for number in numbers:
#     for i in numbers:
#         product = number * i
#         print("{:<5} x {:<5d} = {:>5d}".format(number, i, product))
#         print()
#
for i in range(1, 13):
    for j in range(1, 13):
        print("{:<4} x {:<4} = {:>4}".format(i, j, i * j), end="    ")
    print()

# import itertools
#
# for i, j in itertools.product(range(1, 13), range(1, 13)):
#     print("{} x {} = {}".format(i, j, i * j))
# print()
