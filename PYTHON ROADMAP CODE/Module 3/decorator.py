def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper


@my_decorator
def greet():
    print("Hello, Manav!")


greet()