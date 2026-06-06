def frame(text, symbol):
    border = symbol * (len(text) + 2)

    print(border)
    print(symbol + text + symbol)
    print(border)

frame("Текст в рамці", "*")