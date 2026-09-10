#duck typing example in Python

from functools import reduce


class Duck:

    def quack(self):
        print("Quack!")

class Person:

    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(duck_like):
    duck_like.quack()

    
duck = Duck()
person = Person()   
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm pretending to be a duck!
