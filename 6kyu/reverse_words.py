def reverse_words(string):
    new = []
    for s in string.split(' '):
        if len(s) >= 5:
            new.append(s[::-1])
        else:
            new.append(s)
    print(' '.join(new))


reverse_words("Hey fellow warriors")
