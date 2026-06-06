def combine_lists(list1, list2):
    result = []

    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])

    return result

a = [1, 2, 3]
b = [11, 22, 33]

print(combine_lists(a, b))