def xo(s):
    return True if [i.lower() for i in s].count("x") == [i.lower() for i in s].count("o") else False


xo("xo")
xo("ooxx")
xo("xooxx")
xo("ooxX")
xo("zzoo")
