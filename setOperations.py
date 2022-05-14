# Set Operations of functions

def search(s, val):  # set[1,2,3,4,5], val = 3
    for x in s:  # 1;2;3
        if val == x:  # 3==1;3==2;3==3
            return True  # found
    return False  # not found


def union(s1, s2):  # [1,2,3,4,5] union [1,3,5,7,9] = [1,2,3,4,5,7,9]
    data = s1.copy()  # all elements of s1 into data

    # find the elements of s2 that are not in s1
    for x in s2:  # 1,3,5,7,9
        if not search(s1, x):
            data.append(x)  # as x is not found in s1

    return data


def intersect(s1, s2):  # [1,2,3,4,5] intersect [1,3,5,7,9] = [1,2,3]
    data = []

    # find the elements of s1 that also exist in s2
    for x in s1:  # 1,2,3,4,5
        if search(s2, x):
            data.append(x)

    return data


def minus(s1, s2):  # [1,2,3,4,5] minus [1,3,5,7,9] = [2,4]
    data = []

    # find the elements of s1 that are not found in s2
    for x in s1:  # 1,2,3,4,5
        if not search(s2, x):
            data.append(x)

    return data


def main():
    s1 = [1, 2, 3, 4, 5]
    s2 = [1, 3, 5, 7, 9]

    print('Set1: ', s1)
    print('Set2: ', s2)

    result = union(s1, s2)
    print('Union: ', result)

    result = intersect(s1, s2)
    print('Intersect: ', result)

    result = minus(s1, s2)
    print('Minus: ', result)

    result = symmetric(s1, s2)
    print('Symmetric Difference: ', result)

# to do : find the symmetric difference between 2 sets
def symmetric(s1, s2):
    data = []
    # find the elements of s1 that are not found in s2
    for x in s1:  # 1,2,3,4,5
        if not search(s2, x):
            data.append(x)
    # find the elements of s2 that are not found in s1
    for x in s2:  # 1,2,3,4,5
        if not search(s1, x):
            data.append(x)
    return data
main()