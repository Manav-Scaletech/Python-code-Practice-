#for loop example 

a = [10,20,30,40]

for i in range(1,5):
    print(i)    




x = 1
while x <= 5:
    print(x)
    x += 1 #this should be there otherwise it will be infinite loop ,redefine the value inside the while loop 



for i in range(5):

    if i == 2:
        continue # it will skip the current iteration and move to the next one

    print(i)