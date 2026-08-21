# single lever inheritance

class animal:
    def noting(self,):
        print("this is an animal class. ")  

class dog(animal):
    def nothing(self):
        print("this is a dog class. ")

d = dog()
d.nothing() # this will call the nothing method of dog class.