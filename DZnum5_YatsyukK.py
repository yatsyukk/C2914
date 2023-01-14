import inspect
import sys

import colorama

def first_function():
    pass

class Human:
    pass

clrm=colorama
first_f=first_function()
nick=Human

print(colorama.__name__)
print(clrm.__name__)
print(first_function.__name__)
print(first_f.__ne__)
print(Human.__name__)
print(nick.__name__)
print(__name__)
print(type(2))
print(type(2.9))
print(type(2==2))
print(type("tbhk<3"))
print(type(list))

set={}
for method in dir(set):
    print(method)

print(inspect.ismodule(colorama))
print(inspect.isfunction(first_f))
print(inspect.isclass(Human))
print(inspect.getmodule(list))

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

for _ in dir(__builtins__):
    print(_)