import math

def main():
    diameter1 = int(input("Enter the diameter: "))
    diameter2 = int(input("Enter the diameter: "))
    radius1 = diameter1 / 2
    radius2 = diameter2 / 2
    area1 = math.pi * radius1** 2
    area2 = math.pi * radius2 ** 2
    price1 = int(input("Enter the first price: "))
    price2 = int(input("Enter the second price: "))

    unit_price1 = (area1 / price1)
    unit_price2 = (area2 / price2)

    if unit_price1 > unit_price2:
        print("The price of first pizza is better value for money!")
    elif unit_price1 < unit_price2:
        print("The price of second pizza is better value for money!")
    else:
        print("Both pizza cost the same!")
    return

main()