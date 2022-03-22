# https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python
def rental_car_cost(d):
    if 0 < d < 4:
        return print(d*40)
    elif 4 <= d < 7:
        return print(d*40 - 20)
    else:
        return print(d*40 - 50)


rental_car_cost(1)
rental_car_cost(4)

rental_car_cost(7)
rental_car_cost(8)
