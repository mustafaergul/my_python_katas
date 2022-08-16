def jaden_case(string):
    new = []
    for s in string.split(' '):
        new.append(s.capitalize())
    print(' '.join(new))


jaden_case("How can mirrors be real if our eyes aren't real")
