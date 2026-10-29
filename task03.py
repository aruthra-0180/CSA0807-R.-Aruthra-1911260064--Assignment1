 
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

farmer_id = "F101"
litres = 10
fat = 4.2
snf = 8.7

print("Farmer ID:", farmer_id)
print("Litres:", litres)
print("Fat:", fat)
print("SNF:", snf)

print("Base rate:", BASE_RATE)
print("Fat step value:", FAT_STEP_VALUE)
print("SNF step value:", SNF_STEP_VALUE)

print(type(litres))
print(type(fat))
print(type(farmer_id))

a = 10
b = 20

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
