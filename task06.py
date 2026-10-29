def rate_per_litre(fat, snf):
    base_rate = 30.00
    fat_step = 0.40
    snf_step = 0.30

    fat_steps = int((fat - 3.5) * 10)
    snf_steps = int((snf - 8.5) * 10)

    rate = base_rate + fat_steps * fat_step + snf_steps * snf_step
    return round(rate, 2)


def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    amount = litres * rate
    return round(amount, 2)


def ten_day_total(payments):
    total = 0

    for amount in payments:
        total = total + amount

    return round(total, 2)


litres = 8.5
fat = 4.2
snf = 8.7

rate = rate_per_litre(fat, snf)
amount = payout(litres, fat, snf)

payments = [amount, 300.00, 250.00]
total = ten_day_total(payments)

print("Rate per litre:", rate)
print("Payment:", amount)
print("Ten-day total:", total)