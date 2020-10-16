
# In basic terms, a decorator accepts a function as an argument, does something, and returns another function.
# If we call a decorated function, we are actually calling the function returned by the decorator.
def decorator_function(decorated_function):
    def wrapper():
        print('Before running...')
        decorated_function()
        print('After running...')

    return wrapper

@decorator_function
def say_hello():
    print("hello")

say_hello()