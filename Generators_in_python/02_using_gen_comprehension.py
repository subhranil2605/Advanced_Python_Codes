csv_reader = lambda file_name: (row for row in open(file_name))

csv_gen = csv_reader("Car_sales.csv")

for i in csv_gen:
    print(i)
