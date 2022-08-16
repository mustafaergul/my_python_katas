def solution(number):
    arr = []
    [arr.append(n) for n in range(1, number) if n % 3 == 0 or n % 5 == 0]
    print(sum(arr))


solution(10)
solution(16)
solution(15)
