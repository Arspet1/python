products = []
a = 0
while a != "":
    a = str(input())
    products.append(a)
    if a == "":
        break

with open("shopping_list.txt", "w") as f:
    f.writelines(products)
print(len(products) -1)        