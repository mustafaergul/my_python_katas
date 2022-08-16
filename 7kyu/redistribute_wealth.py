def redistribute_wealth(arr):
    le = len(arr)
    sa = sum(arr)
    print([(sa/le) for x in range(le)])


redistribute_wealth([5, 10, 6])
redistribute_wealth([0, 10])
redistribute_wealth([3, 2, 2])
