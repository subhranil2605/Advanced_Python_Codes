# List and Dictionaries

numbers: list = [2, 34, 56, 3, 2, 5]

description: dict = {
    "length": len(numbers),
    "sum": sum(numbers),
    "mean": sum(numbers) / len(numbers)
}

print(description)
# sum and len are calculated twice


# using walrus operator
description: dict = {
    "length": (num_len := len(numbers)),
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_len
}

print(description)
