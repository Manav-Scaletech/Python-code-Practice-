#using the class methods in the custom manager 

class one:

    def __enter__(self):
        print("you are entering the file :")
        return self

    def add(self, a, b):
        return a + b

    def __exit__(self, exc_type, exc_value, traceback):
        print("file is closed :")
        
with one() as n:
    print(n.add(10, 20))