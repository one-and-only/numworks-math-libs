import libs.lib1

prgrmchoice = input("Select From One of the Programs:\n1. Simplify a Fraction (Numerical)\n2. Factor a Quadratic Function\nYour Choice: ")
if (prgrmchoice == "1"):
    numer = int(input("Enter the Numerator of the Fraction: "))
    denom = int(input("Enter the Denominator of the Fraction: "))
    libs.lib1.simplify_fraction(numer, denom)
elif (prgrmchoice == "2"):
    a = input("What is your a? (y=ax^2+bx+c) ")
    b = input("What is your b? (y=ax^2+bx+c) ")
    c = input("What is your c? (y=ax^2+bx+c) ")
    libs.lib1.quadratic_function(int(a),int(b),int(c))
else:
    print("You entered an invalid option.")