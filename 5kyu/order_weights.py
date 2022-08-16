def order_weights(lst):
    # print(sorted([sum([int(i) for i in (_)]) for _ in string.split(' ')]))
    # print(sum([int(i) for i in (_)]))

    for _ in lst.split(' '):
        lst1 = sum([int(i) for i in (_)])


order_weights("103 123 4444 99 2000")
