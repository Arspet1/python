#Реалізуйте функцію group_by_length(words), яка приймає список слів та групує
#  їх у словник за довжиною слова. Вхід: ['cat', 'dog', 'apple', 'bat'].
#  Вихід: {3: ['cat', 'dog', 'bat'], 5: ['apple']}
def group_by_length(words):
    result = {}

    for word in words:
        length = len(word)

        if length not in result:
            result[length] = []

        result[length].append(word)

    return result


print(group_by_length(['cat', 'dog', 'apple', 'bat']))