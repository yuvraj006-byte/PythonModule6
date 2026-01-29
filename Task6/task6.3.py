def gal_lit():
   if american_gas > 0:
       lit = american_gas * 3.78541
       print(lit)
   return

while True:
    american_gas = int(input("Enter the American Gasoline Amount in gallons: "))
    if american_gas < 0:
        print("Gas can Not be in Negative!")
        break
    else:
        lit = american_gas * 3.78541
        print(lit)
gal_lit()

