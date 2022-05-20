'''
Repeated function calls: makes your code slower.
'''

numbers: list = [7, 6, 1, 3, 4, 1, 5, 0, 9]


def slow(num: int) -> int:
    return num - 5


results: list = [slow(num) for num in numbers if slow(num) > 0]
print(results)

# using filter
##results = filter(lambda value: value > 0, (slow(num) for num in numbers))
##print(list(results))

# in the avobe case, we can see that the function slow() calls
# twice

# use walrus operator to call that function once
results: list = [
    value for num in numbers
    if (value := slow(num)) > 0
]

print(results)



