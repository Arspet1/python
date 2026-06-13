#Напишіть функцію save_text_to_file(text, filename), яка записує переданий текст у файл з вказаною назвою.
def save_text_to_file(text, filename):
    with open(filename, "w") as file:
        file.write(text)


save_text_to_file("hello, world", "test.txt")