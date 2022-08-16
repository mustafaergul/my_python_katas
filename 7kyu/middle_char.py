def get_middle(s):
    print(s[int(len(s)/2)]) if len(s) % 2 != 0 else print(s[int(len(s)/2-1):int(len(s)/2+1)])


get_middle("test")
get_middle("testing")
get_middle("middle")
