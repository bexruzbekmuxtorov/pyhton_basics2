info = {}
for i in range(3):
    key = input(f"{i+1}-kalitni kiriting: ")
    value = int(input(f"{i+1}-qiymatni kiriting (raqam): "))
    info[key] = value
total = sum(info.values())
print("\nQiymatlar yig'indisi:", total)