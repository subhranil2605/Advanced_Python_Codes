numbers = [i for i in range(1, 11)]

squared = map(lambda x: x**2, numbers)


##print(numbers)
##print(list(squared))

# converting string values to integer
str_nums = ["1", "2", "3", "100"]

int_nums = list(map(int, str_nums))

##print(str_nums)
##print(int_nums)


# different kind of functions
words = ["Hello", "Subhranil", "Apple"]

len_words = list(map(len, words))

[print(f"{w}:{l}") for w, l in zip(words, map(len, words))]
#[print(f"{w}:{len(w)}") for w in words]


b = map(list, zip(words, len_words))
print(list(b))



