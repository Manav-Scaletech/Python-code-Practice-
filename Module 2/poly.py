#simple polymorphism` example in Python

# 1. method `overriding` example
class Animal:

    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


class Lion(Animal):

    def sound(self):
        print("Roar")


d = Dog()
c = Cat()
l = Lion()


d.sound()
c.sound()
l.sound()