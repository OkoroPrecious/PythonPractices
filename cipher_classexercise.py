import string

user = (input("Enter a string to encode :"))
key = input("Enter a key number")
a_digit = key.isdigit()

# first ensure the string is string and int is int
while not user.isalpha():
    user = input("Enter a string to encode : ")

while not a_digit:
    key = input("Enter a key number")

key = int(key)

abc = string.ascii_lowercase

trans = abc[key:] + abc[:key]

cipher = user.translate(str.maketrans(abc, trans))
print(cipher)

decipher = cipher.translate(str.maketrans(trans, abc))
print(decipher)
