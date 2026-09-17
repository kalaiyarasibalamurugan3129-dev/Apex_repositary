import math

print("1. Area of Circle")
print("2. Area of Square")
print("3. Area of Rectangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print("Area of Circle =", area)

elif choice == 2:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 3:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)

else:
    print("Invalid choice")