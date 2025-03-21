import os
import datetime
import json
import math
import re

arr = [1, 5, 66, 9, 10]

open with ("t.txt", "w") as file:
    json.dump(arr, file)
    
s = "sakajdefawjdk "
#a j d e

n = re.findall("ajde", s)

print(re.match(" ", ))

currentdate = datetime.now()
print(currentdate - timedelta(month=2))

def sgr(n):
    yield from (x**2 for x in range(2, n+1, 2))
    
    
    
#10-9-66-5-1
 
 
