#multilevel inheritance

class animal:
    def nothing(self,):
        print("this is an animal class. ")

    def note(self):
        print("first one called : ")

class dog(animal):
    def nothing(self):
        super().nothing() 
        print("this is a dog class. ")

class puppy(dog):
    def nothing(self):
        super().nothing() # method overriding and using the super keyword to call the parent class method.
        print("this is a puppy class. ")

p = puppy()

#
p.nothing()
