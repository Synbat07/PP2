data = ["Hello\n", "World\n", "Python\n"]

with open("ex2.txt", "w") as file:
    file.writelines(data)
