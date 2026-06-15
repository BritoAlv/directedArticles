from math import gcd, pi


def experiment(m : int, upper_bound : int):
    from random import randint
    goods = 0
    for i in range(m):
        a, b = randint(1, upper_bound), randint(1, upper_bound)
        if gcd(a, b) == 1:
            goods += 1
    
    print(goods / m, 6 / (pi ** 2) )