def mumbling(string):
    print('-'.join([((idx+1)*i).title() for idx, i in enumerate(string)]))


mumbling("abcd")
