def calculate_payment(litres, fat, snf, month):
    base_rate = 30.00
    fat_step = 0.40
    snf_step = 0.30

    if month in [4, 5, 6]:
        base_rate = 32.00
        fat_step = 0.45

    fat_steps = round((fat - 3.5) * 10)
    snf_steps = round((snf - 8.5) * 10)

    rate = base_rate + fat_steps * fat_step + snf_steps * snf_step
    rate = round(rate, 2)

    amount = litres * rate

    if litres > 500:
        amount = amount + litres * 0.50

    return rate, round(amount, 2)


# Test 1: Normal season
rate, amount = calculate_payment(100, 4.2, 8.7, 2)
print("Normal season")
print("Rate:", rate)
print("Payment:", amount)

# Test 2: Seasonal rate (April)
rate, amount = calculate_payment(100, 4.2, 8.7, 4)
print("Seasonal rate")
print("Rate:", rate)
print("Payment:", amount)

# Test 3: Bonus for more than 500 litres
rate, amount = calculate_payment(600, 4.2, 8.7, 4)
print("Bonus payment")
print("Rate:", rate)
print("Payment:", amount)