import random

# rng = list(range(1, 100, 5))
# # range 1 to 100 and increment by 5
# print(rng)
#
# rng.append(1_000)
# # Adds 1000 to the end of the list of elements
# print(rng)
#
#
# rng.append([2, 3, 4])
# print(rng)
#
#
# rng.extend([2, 3, 4])
# print(rng)
# # extend takes iterable then add to the elements and scatters the number
#
# # extend is the same thing with +=
# rng += [2, 3, 4]
#
# rng.insert(0, 99)
# print(rng)
# # insert 99 in position zero. its can work for any point of the list
#
# idk = rng.index(71)
# print(idk)
# print(rng)
#
# rng.clear()
# print(rng)
#
# popped = rng.pop()
# print(popped)
# print(rng)
# # removes index from the last. But if you pass an argument of the index you want to remove
#
#
# rng.remove(41)
# print(rng)
#
#
# rng = list(range(1, 100, 5))
# print(rng)
# # To shuffle
# random.shuffle(rng)
#
# #
# print(rng)
# print(random.choice(rng))
#
# random.seed(45)
# # makes calculation which uses a number you are inputting
# rng = list(range(1, 100, 5))
# print(rng)
#
# random.shuffle(rng)
# print(rng)
#
# rng.reverse()
# print(rng)
# # reverses the list
#
# rng.sort(reverse=True)
# print(rng)
# # it prints from back in descending order from highest to lowest.

fruits = ["apple", "mango", "water melon", "cherry", "banana", "cucumber", "pineapple"]
# fruits.sort()
# print(fruits)


fruits.sort(key=len)
print(fruits)

fruits.sort(key=len, reverse=True)
print(fruits)


