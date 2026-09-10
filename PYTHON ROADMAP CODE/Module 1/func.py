#for the function code example: 

number = [1,2,3,4,5]

print(sorted(number, reverse=True)) #for the absolute value of the number : 



#function scoped for the local , encloasing , gloabal and built in scope

x = "Global"

def outer():

    y = "Enclosing"

    def inner():

        z = "Local"

        print(z)
        print(y)
        print(x)
        print(len("abc"))

    inner()

outer()