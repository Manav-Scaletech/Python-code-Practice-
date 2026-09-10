from functools import reduce

numbers = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10
}

def separate(result, item):
    if item[1] % 2 == 0:
        result["even"].append(item[1])
    else:
        result["odd"].append(item[1])

    return result

answer = reduce(
    separate,
    numbers.items(),
    {"odd": [], "even": []}
)

print(answer)