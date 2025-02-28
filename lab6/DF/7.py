with open("example.txt", "r") as src, open("ex2.txt", "w") as dst:
    dst.write(src.read())
