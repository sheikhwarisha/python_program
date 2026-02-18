print("=== 3x3 Matrix Even-Odd Counter ===")

even_count = 0
odd_count = 0
zero_count = 0

for i in range(3):
    for j in range(3):
        num = int(input(f"Enter value for position [{i}][{j}] : "))
        
        if num % 2 == 0 and num != 0:
            even_count += 1
        elif num % 2 != 0:
            odd_count += 1
        else:
            zero_count += 1

print("\nEven numbers:", even_count)
print("Odd numbers:", odd_count)
print("Zero numbers:", zero_count)
