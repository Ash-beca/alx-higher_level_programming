#!/usr/bin/python3
def weight_average(my_list=[]):
    points = 0
    total = 0
    if my_list:
        numbers_in_tuples = ()
        for numbers_in_tuples in my_list:
            points += (numbers_in_tuples[0] * numbers_in_tuples[1])
            total += numbers_in_tuples[1]
        return points / total
    return 0