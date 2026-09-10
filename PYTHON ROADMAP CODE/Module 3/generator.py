import logging

def hello():
    i = 0
    for i in range(5):
        i += 1
        yield i
    
g = hello()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
