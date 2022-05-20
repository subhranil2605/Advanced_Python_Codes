def filter_to_positive_number(numbers: list) -> list:
    return list(filter(lambda x: x >= 0, numbers))


# data with negative and positive
data = [90, -9, 5, 3, 12, 1]

# filtered data
positive_data = filter_to_positive_number(data)

print(positive_data)
