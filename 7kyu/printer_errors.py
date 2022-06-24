# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
def printer_errors(stri):
    c = 0
    z = 0
    for s in list(stri):
        z += 1
        if s in list(map(chr, range(ord('a'), ord('m')+1))):
            continue
        else:
            c += 1
    print(f"{c}/{z}")


printer_errors("aaabbbbhaijjjm")
printer_errors("aaaaxbbbbyyhwawiwjjjww")
