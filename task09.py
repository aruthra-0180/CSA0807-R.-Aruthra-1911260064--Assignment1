def rate_per_litre(fat, snf):
    rate = 30 + round((fat - 3.5) * 10) * 0.40
    rate = rate + round((snf - 8.5) * 10) * 0.30
    return round(rate, 2)


def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


# Test 1: Normal values
print("Test 1:", payout(10, 3.5, 8.5))

# Test 2: Higher fat and SNF
print("Test 2:", payout(8.5, 4.2, 8.7))

# Test 3: Lower fat and SNF
print("Test 3:", payout(12, 3.1, 8.3))

# Test 4: Zero litres
print("Test 4:", payout(0, 3.5, 8.5))

# Test 5: Invalid litres
litres = -5

if litres < 0:
    print("Test 5: Invalid litres")
else:
    print("Test 5:", payout(litres, 3.5, 8.5))