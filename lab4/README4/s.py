#SCOPE

#1) Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#2) Global Scope
#A variable created outside of a function is global and can be used by anyone:

x = 500

def myfunc():
  print(x)

myfunc()

print(x)