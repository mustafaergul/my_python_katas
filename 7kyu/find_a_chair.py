def meeting(rooms, need):
    la = [s for s in [t[1] - len(t[0]) for t in rooms] if s >= 0]
    if sum(la) == need:
        print(la)
    elif sum(la) > need:
        print("Game On")
    else:
        print("Not enough!")


meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4)
meeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3],
        ["XXX", 1]], 5)
meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0)
meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8)


# -2 0 1 2 2 -2
