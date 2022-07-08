import string
abc = string.ascii_lowercase
user_entry = 'love'
key = 5
# cipher = (s.translate(str.maketrans(abc, abc[key:] + abc[:key])
cipher = (user_entry.translate(str.maketrans(abc, abc[key:] + abc[:key])))
print(cipher)
