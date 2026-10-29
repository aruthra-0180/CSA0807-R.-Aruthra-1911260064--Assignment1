farmer_id = input("Enter farmer ID: ")

try:
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    if litres <= 0:
        print("Invalid litres")
    elif fat < 2.0 or fat > 7.0:
        print("Invalid fat percentage")
    elif snf < 0:
        print("Invalid SNF percentage")
    else:
        rate = 30 + (fat - 3.5) * 4 + (snf - 8.5) * 3
        amount = litres * rate

        print(f"Farmer ID: {farmer_id}")
        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Total amount: Rs. {amount:.2f}")

except ValueError:
    print("Invalid input. Enter numbers only.")