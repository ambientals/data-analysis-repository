"""Code that transforms metres input to miles and inches. This code has educational purposes, no copyright infringement is intended."""

def meters_to_miles(metres):
    miles = metres * 0.000621371
    print(f"{metres} metres equals {miles} miles")
    
    inches = metres * 39.3701
    print(f"{metres} metres equals {inches} inches")

meters_to_miles(40)