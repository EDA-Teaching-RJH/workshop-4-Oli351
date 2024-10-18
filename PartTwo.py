total = 0

while total < 75:
    coin_value = int(input("value of coin: "))
    print("please add more coins")
    total += coin_value

if total >= 75:
    print("Tank you!")
    change = total - 75
    print(f"your change is", change)

