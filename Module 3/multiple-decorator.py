def a(func):
    def inner(*args, **kwargs):
        print("a before ")
        func(*args, **kwargs)
        print("a after ")
    return inner


def b(func):
    def inner(*args, **kwargs):
        print("b before ")
        func(*args, **kwargs)
        print("b after ")
    return inner

@b
@a

def hi():
    print("hello")
    print("outside of the decorator : ")    

hi()


