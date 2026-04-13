def calculate_profit(amount, percent, period):
    if amount == 0 or percent == 0 or period == 0:
        return 0

    start = amount 

    for i in range(period):
        amount = amount + amount * (percent / 100)

    profit = amount - start
    return round(profit, 2)

print(calculate_profit(1000, 10, 3))