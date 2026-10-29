def rate_per_litre(fat, snf, base_rate=30.00):
    fat_steps = round((fat - 3.5) * 10)
    snf_steps = round((snf - 8.5) * 10)

    rate = base_rate + fat_steps * 0.40 + snf_steps * 0.30
    return round(rate, 2)


def payout(litres, fat, snf, base_rate=30.00):
    rate = rate_per_litre(fat, snf, base_rate)
    return round(litres * rate, 2)


# Normal payment
print("Normal season")
print("Rate:", rate_per_litre(4.2, 8.7))
print("Payment:", payout(8.5, 4.2, 8.7))

# Updated seasonal rate
print("Seasonal rate")
print("Rate:", rate_per_litre(4.2, 8.7, 32.00))
print("Payment:", payout(8.5, 4.2, 8.7, 32.00))

# Validate input
litres = -5

if litres < 0:
    print("Invalid litres")
else:
    print("Payment:", payout(litres, 4.2, 8.7))