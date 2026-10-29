from decimal import Decimal
import time

payments = ["300.00", "283.90", "333.60"]

# Using float
start = time.perf_counter()

float_total = 0.0
for payment in payments:
    float_total += float(payment)

float_time = time.perf_counter() - start

# Using Decimal
start = time.perf_counter()

decimal_total = Decimal("0.00")
for payment in payments:
    decimal_total += Decimal(payment)

decimal_time = time.perf_counter() - start

print("Float total:", round(float_total, 2))
print("Decimal total:", decimal_total)
print("Float time:", float_time)
print("Decimal time:", decimal_time)

# Rounding each payment
rounded_total = 0
for payment in payments:
    rounded_total += round(float(payment), 2)

print("Rounded payment total:", round(rounded_total, 2))

# Rate card using dictionary
rate_card = {
    "base": 30.00,
    "fat_step": 0.40,
    "snf_step": 0.30
}

print("Base rate:", rate_card["base"])
print("Fat step:", rate_card["fat_step"])
print("SNF step:", rate_card["snf_step"])