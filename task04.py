litres = 10
fat = 4.2
snf = 8.7

base_rate = 30.00
fat_step = 0.40
snf_step = 0.30

fat_steps = int((fat - 3.5) * 10)
snf_steps = int((snf - 8.5) * 10)

rate = base_rate + fat_steps * fat_step + snf_steps * snf_step
amount = litres * rate

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", round(rate, 2))
print("Total amount:", round(amount, 2))

print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("-7 // 2 =", -7 // 2)

print("int(3.9) =", int(3.9))
print("round(3.9) =", round(3.9))

print("5 < 6 < 7 =", 5 < 6 < 7)