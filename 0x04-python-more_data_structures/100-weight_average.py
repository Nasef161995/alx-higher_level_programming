def weight_average(my_list=[]):
    sum = 0
    num = 0
    for i, j in my_list:
        sum = sum + (i*j)
        num = num + j
    result = sum / num
    return result
