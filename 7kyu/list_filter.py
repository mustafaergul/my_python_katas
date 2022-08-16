def lst_filter(lst):
    print([n for n in lst if isinstance(n, int)])


lst_filter([1, 2, 'a', 'b'])
