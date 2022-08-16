def who_likes(arr):
    if len(arr) <= 0:
        print("no one likes this")
    elif len(arr) > 3:
        print(f"{arr[0]}, {arr[1]} and {len(arr)-2} like this")
    elif len(arr) > 2:
        print(f"{arr[0]}, {arr[1]} and {arr[-1]} like this")
    elif len(arr) == 1:
        print(f"{arr[0]} likes this")
    elif len(arr) > 1:
        print(f"{arr[0]} and {arr[1]} like this")


who_likes([])
who_likes(["Peter"])
who_likes(["Jacob", "Alex"])
who_likes(["Jacob", "Alex", "Mark"])
who_likes(["Mustafa", "Sezen", "Elif", "adfasdfasdfaf"])
