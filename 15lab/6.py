#Напишіть функцію, яка зчитує дані з файлу grades.txt, у якому кожен рядок має формат:
#  Ім'я: оцінка. Поверніть словник зі студентами, чиї оцінки >= 10.
def read_grades(filename):
    result = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, grade = line.strip().split(":")
            grade = int(grade)

            if grade >= 10:
                result[name] = grade

    return result


print(read_grades("grades.txt"))