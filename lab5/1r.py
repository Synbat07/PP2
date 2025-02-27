import re

def match_a_with_b(s):
    return bool(re.fullmatch(r"^a[b]*$", s))

print(match_a_with_b("a"))   # True
print(match_a_with_b("ab"))  # True
print(match_a_with_b("abc")) # False

