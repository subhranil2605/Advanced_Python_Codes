# Python Decorators 


def func(fun):
    def wrapper():
        print("Starting")
        fun()
        print("End")
    return wrapper


def f():
    print("hello!")


# we did not call the function so, it will show the memory address of the function returned by the func()
#print(func(f))

# now calling the function
#func(f)()


# creating a variable and store the func
f = func(f)

f()

# Now we'll use the decorators

@func
def f2():
    print("Hello world")


f2()


'''
So, for using the decorator, we dont need to create a new variable to store the wrapper, it automatically
does this for us
'''
