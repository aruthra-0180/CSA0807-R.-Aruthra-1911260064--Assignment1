def calculate_total(payments):
    total = 0

    for payment in payments:
        total = total + payment

    return total


payments = [300.00, 283.90, 333.60]

print("Payment 1:", payments[0])
print("Payment 2:", payments[1])
print("Payment 3:", payments[2])

total = calculate_total(payments)

print("Total payment:", round(total, 2))