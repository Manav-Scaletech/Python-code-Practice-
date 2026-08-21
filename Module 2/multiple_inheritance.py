#for the multiple inheritance


class animal:
    def nothing(self,):
        print("this is an animal class. ")

class dog:
    def nothing(self):
        print("this is a dog class. ")

class puppy(animal , dog  ):
    def nothing(self):
        super().nothing() # method overriding and using the super keyword to call the parent class method.
        print("this is a puppy class. ")    

p = puppy()
p.nothing()
