#from Decorators.examples_for_real_world_application.timer_decorator import timer


# Without the generator

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")  # file.read().split() loads everything into memory at once
    return result


# using the generator
def csv_reader_gen(file_name):
    for row in open(file_name, "r"):
        yield row


#@timer
def funct():
    csv_gen = csv_reader_gen("Car_sales.csv")
    row_count = 0
    for _ in csv_gen:
        row_count += 1
    print(f"Row count: {row_count}")


funct()
