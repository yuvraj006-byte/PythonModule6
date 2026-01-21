import math

def main():
    diameter = int(input("Enter the diameter: "))
    radius = diameter / 2
    area = math.pi * radius ** 2
    price1 = int(input("Enter the first price: "))
    price2 = int(input("Enter the second price: "))

    unit_price1 = (area / price1)
    unit_price2 = (area / price2)

    if unit_price1 > unit_price2:
        print("The price of first pizza is better value for money!")
    elif unit_price1 < unit_price2:
        print("The price of second pizza is better value for money!")
    else:
        print("Both pizza cost the same!")

main()