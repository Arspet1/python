with open("input_countries.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

dictionary = {
    "Українська": ["Україна"],
    "Російська": ["Україна"],
    "Французька": ["Франція"],
    "Німецька": ["Німеччина"],
    "Іспанська": ["США"],
    "Англійська": ["США", "Німеччина", "Франція"]
}

for line in lines:
    parts = line.split(":")
    country = parts[0].strip()
    languages_str = parts[1].strip()

languages = languages_str.split()
    

lang = input("Введіть мову: ")  


if lang in dictionary:
    print(dictionary[lang])
else:
    print("Нема таких країн у словнику")