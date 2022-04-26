# multiple input iterables with map()

first = [1, 2, 3]
second = [4, 5, 6, 7]

result = list(map(pow, first, second))

print(result) # [1, 32, 729]

'''
1**4, 2**5, 3**6 and the last digit of second is ignored
'''


# another example

a = [2, 4, 6]
b = [1, 3, 5]

c = map(lambda x, y: x-y, a, b)

c = list(c)
print(c)


# another one
print(list(map(lambda x, y, z: x + y +z, [2, 4], [1, 3], [7, 8])))
