#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new = [i for i in matrix]
print(matrix)
print(new)

for i in range(3):
    for j in range(3):
        new[i][j] = new[i][j]**2

print(new)
print(matrix)
print('=======================')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element)
new = [[i**2 for i in x] for x in matrix]
print(new)
print(matrix)
print('=======================')
my_list = [1, 2, 3, 1, 4, 2, 5]
result = 0
for num in my_list:
    trial = my_list.count(num)
    if trial > 1:
        i = 0
        result = result + num
        while i != trial:
                my_list[my_list.index(num)] = 0
                i+=1
print(my_list)
print(result)
