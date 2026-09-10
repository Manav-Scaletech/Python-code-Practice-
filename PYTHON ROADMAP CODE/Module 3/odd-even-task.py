from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

def separate_even_odd(acc, item):
    key, value = item

    if value % 2 == 0:
        acc["even"].append(value)
    else:
        acc["odd"].append(value)

    return acc

result = reduce(
    separate_even_odd,
    enumerate(numbers),
    {"even": [], "odd": []}
)

print(result)