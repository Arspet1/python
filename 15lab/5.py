#Напишіть функцію, яка за допомогою zip() об'єднує два списки (імена та оцінки) у словник.
#    Вхід: ['Anna', 'Ivan'], [10, 8]. Вихід: {'Anna': 10, 'Ivan': 8}
def create_dict(names, grades):
    return dict(zip(names, grades))


print(create_dict(['Anna', 'Ivan'], [10, 8]))