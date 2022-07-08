# file = open("hello.txt", mode="w", encoding="utf-8")

with open("hello.txt", mode="w", encoding= "utf-8") as file:
    file.write("I love writing\n")
    file.write("I love reading\n")
    file.writelines(["I am prone to violence", "I am prone to violence"])


with open("hello.txt", mode="r", encoding="utf-8") as file:
    for index, line in enumerate(file.readlines()):
        print(f"line {index + 1}: {line}")


# file.close()
# It will open a file to display
