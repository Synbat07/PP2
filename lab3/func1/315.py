def permute(s, answer=""):
    if not s:
        print(answer)
        return
    for i in range(len(s)):
        permute(s[:i] + s[i+1:], answer + s[i])

s = input("Enter a string: ")
permute(s)
