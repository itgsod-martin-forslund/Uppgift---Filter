def filter(array, value):
    result = []

    for i in array:
        if i == value:
            result.append(i)

    return result

print filter([1, 2, 3 ,3, 5], 3)


def exclude(array, value):
    for i in array[:]:
        if i == value:
            array.remove(i)

    return array

print exclude([5, 7, 7, 2], 7)


def unique(array):
    lol = []

    for i in array:
        if i not in lol:
            lol.append(i)

    return lol

print unique([5, 7, 7, 2])

