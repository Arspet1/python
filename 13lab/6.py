def getInput():
    return input("Введіть число: ")

def testInput(value):
    try:
        int(value)
        return True
    except:
        return False

def strToInt(value):
    return int(value)

def printInt(value):
    print(value)

data = getInput()
print("Введено:", data)

if testInput(data):
    print("Число корректное")
    number = strToInt(data)
    printInt(number)
else:
    print("Це не ціле число")