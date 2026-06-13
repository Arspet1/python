import pandas as pd

data = {
    'town': [
        'Tokyo',
        'Delhi',
        'Shanghai',
        'Dhaka',
        'Sao Paulo',
        'Cairo',
        'Mexico City',
        'Beijing',
        'Mumbai',
        'Osaka'
    ],

    'population': [
        37400068,
        29399141,
        26317104,
        21810000,
        21846507,
        20484965,
        21671908,
        20035455,
        20185064,
        19222665
    ],

    'square': [
        2194,
        1484,
        6341,
        306,
        1521,
        3085,
        1485,
        16411,
        603,
        225
    ],

    'country': [
        'Japan',
        'India',
        'China',
        'Bangladesh',
        'Brazil',
        'Egypt',
        'Mexico',
        'China',
        'India',
        'Japan'
    ]
}

towns = pd.DataFrame(data)

print("\nПочатковий DataFrame:")
print(towns)

# 2.2 Густота населення
towns['density'] = towns['population'] / towns['square']

print("\nDataFrame з густиною населення:")
print(towns)

# 2.3 Міста та країни
print("\nМіста та країни:")
print(towns[['town', 'country']])

# 2.4 Перші 5 міст
print("\nПерші 5 міст:")
print(towns.head())

# 2.5 Зміна індексів
towns = towns.set_index('town')

print("\nDataFrame з новими індексами:")
print(towns)

# 2.6 Дані по одному місту
print("\nДані про Tokyo:")
print(towns.loc['Tokyo'])

# 2.7 Населення більше 12000000
print("\nМіста з населенням > 12000000:")
print(towns[towns['population'] > 12000000])

# 2.8 Площа більше 5000 км²
print("\nМіста з площею > 5000 км²:")
print(towns[towns['square'] > 5000])

# 2.9 Всі міста КНР
print("\nМіста КНР:")
print(towns[towns['country'] == 'China'])