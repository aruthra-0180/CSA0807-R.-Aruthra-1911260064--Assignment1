from milkrate import rate_per_litre, payout

print("Case 1")
print("Rate:", rate_per_litre(3.5, 8.5))
print("Payment:", payout(10, 3.5, 8.5))

print("Case 2")
print("Rate:", rate_per_litre(4.2, 8.7))
print("Payment:", payout(8.5, 4.2, 8.7))

print("Case 3")
print("Rate:", rate_per_litre(3.1, 8.3))
print("Payment:", payout(12, 3.1, 8.3))