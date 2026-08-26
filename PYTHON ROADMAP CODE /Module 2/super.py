#using the super keyword usage : 

class a :
    def sound(self):
        print("this is a sound of a animal. ")

class b(a):
    def sound(self): 
        super().sound() # method overriding and using the super keyword to call the parent class method.
        print("this is a sound of a dog. ")

b = b()
b.sound()