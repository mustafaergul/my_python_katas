# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
def greet(name):
    names = name.split()
    for n in names.items():
        print(n) if n.istitle() else "No"


greet("Hello, Ryan how are you doing today?")
