def desce(number):
    print(''.join(list(map(str, sorted([int(n) for n in str(number)], reverse=True)))))


desce(12345)
