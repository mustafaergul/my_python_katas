def isogram(string):
    if len([s for s in string.lower()]) == len(set([s for s in string.lower()])):
        print("True")
    else:
        print("False")


isogram("aba")
isogram("Dermatoglyphics")
isogram("moOse")
