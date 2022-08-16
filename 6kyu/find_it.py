def find_it(seq):
    print([s for s in seq if not seq.count(s) % 2 == 0][0])


find_it([7])
find_it([0])
find_it([1, 1, 2])
find_it([0, 1, 0, 1, 0])
