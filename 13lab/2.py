def sunny():
    print("Рекомендуємо кросівки")

def rain():
    print("Рекомендуємо гумові черевики")

def snow():
    print("Рекомендуємо черевики")

weather = input("Погода (сонячно/дощ/сніг): ")

if weather == "сонячно":
    sunny()
elif weather == "дощ":
    rain()
elif weather == "сніг":
    snow()
else:
    print("Невідома погода")