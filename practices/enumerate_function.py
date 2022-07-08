river = 'Mississippi'
target = input('Input a character to find: ')
for index, letter in enumerate(river):
    if letter == target:
        print("Letter found at index: ", index)
        break
    else:
        print('letter', target, 'not found', river)
