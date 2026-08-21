# def note(func):
#     def hello(name , city , date):
#         print("before : ")
#         age = 2
#         func(name , city , date , age )
#         print("after of it : ")
#     return hello
    
# @note
# def main(a,b,c,d):
#     print(a , b , c , d)
    
# def main("manav" , "ahemdabd " , 21  )     


def my_decorator(func):

    def wrapper(a, b, c, d):

        print("Before")

        print("Decorator got d =", d)

        f = func(a, b, c)

        print("After")
        
        return f  + d

    return wrapper


@my_decorator
def greet(a, b, c):

    return a + b + c 


print(greet(1, 2, 3, 999))             #main func with 3 argu and deco. func.  with 4 argu. 
    