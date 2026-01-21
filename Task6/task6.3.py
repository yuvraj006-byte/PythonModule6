american_gas = int(input("Enter the American Gasoline Amount in gallons: "))

def gal_lit():
    if american_gas < 0:
        print("Gas can Not be in Negative!")
        breakpoint()
    lit = american_gas * 3.78541
    return print(lit)



gal_lit()

