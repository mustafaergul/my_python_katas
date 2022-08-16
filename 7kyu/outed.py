def outed(meet, boss):
    print("Get Out Now!") if (sum(meet.values()) + meet[boss] / len(meet) <= 5) else print("Nice Work Champ!")

outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura')
