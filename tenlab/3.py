wagon = [
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: None, 2: None, 3: None, 4: None}
]


i = 0  

for cupe in wagon:
    is_free = True

    for mesto in cupe:
        if cupe[mesto] is not None:
            is_free = False
            i += 1 
if is_free: 
    print("Вільні купе:", i)
        

