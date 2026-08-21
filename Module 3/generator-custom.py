def count_up_to(maximum):
    """A custom generator that counts from 1 to the maximum."""
    count = 1
    while count <= maximum:
        yield count  # The function pauses here and sends 'count' out
        count += 1   # Resumes here on the next request


# Using the custom generator
counter = count_up_to(5)

print(next(counter))  # Outputs: 1
print(next(counter))  # Outputs: 2
print(next(counter))
print(next(counter))
print(next(counter))  # Outputs: 3
print(next(counter))
print(next(counter))
# Calling next(counter) again would raise a StopIteration exception
