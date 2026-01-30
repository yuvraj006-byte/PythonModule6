import math
def area_func_one():
    diameter1 = float(input("Enter the First diameter: "))
    radius1 = (diameter1 / 2) / 100
    area1 = math.pi * radius1 ** 2
    return area1

def area_func_two():
    diameter2 = float(input("Enter the Second diameter: "))
    radius2 = (diameter2 / 2) / 100
    area2 = math.pi * radius2 ** 2
    return area2


def price(a,b):
    return a, b
price1 = int(input("Enter the first price: "))
price2 = int(input("Enter the second price: "))

unit_price1 = price1/area_func_one()
unit_price2 = price2/area_func_two()
def main():
    price(unit_price1, unit_price2)

    if unit_price1 < unit_price2:
        print("The price of first pizza is better value for money!")
    elif unit_price1 > unit_price2:
        print("The price of second pizza is better value for money!")
    else:
        print("Both pizza cost the same!")
    return

main()