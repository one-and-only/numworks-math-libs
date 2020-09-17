from math import sqrt
from decimal import Decimal

def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

prgrmchoice = input("Select From One of the Programs:\n1. Simplify a Fraction (Numerical)\n2. Factor a Quadratic Function\nYour Choice: ")
if (prgrmchoice == "1"):
    numer = int(input("Enter the Numerator of the Fraction: "))
    denom = int(input("Enter the Denominator of the Fraction: "))

    def simplify_fraction(numer, denom):
        if denom == 0:
            return "Division by 0 - result undefined"

        # Remove greatest common divisor:
        common_divisor = gcd(numer, denom)
        (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
        # Note that reduced_den > 0 as documented in the gcd function.

        if common_divisor == 1:
            print(str(Decimal(numer).normalize())+"/"+str(Decimal(denom).normalize()))
        else:
            # Bunch of nonsense to make sure denominator is negative if possible
            if (reduced_den > denom):
                if (reduced_den * reduced_num < 0):
                    print(str(Decimal(-reduced_num).normalize())+"/"+str(Decimal(-reduced_den).normalize()))
                else:
                    print("Debug divisor other than")
                    print(str(Decimal(reduced_num).normalize())+"/"+str(Decimal(reduced_den).normalize()))
            else:
                print(str(reduced_num)+"/"+str(reduced_den))
    simplify_fraction(numer, denom)
elif (prgrmchoice == "2"):
    def simplify_fraction_quadratic(numer, denom):
        if denom == 0:
            return "Division by 0 - result undefined"

        # Remove greatest common divisor:
        common_divisor = gcd(numer, denom)
        (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
        # Note that reduced_den > 0 as documented in the gcd function.

        if common_divisor == 1:
            return (numer, denom)
        else:
            # Bunch of nonsense to make sure denominator is negative if possible
            if (reduced_den > denom):
                if (reduced_den * reduced_num < 0):
                    return(-reduced_num, -reduced_den)
                else:
                    return (reduced_num, reduced_den)
            else:
                return (reduced_num, reduced_den)

    def quadratic_function(a,b,c):
        if (b**2-4*a*c >= 0):
            x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
            x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
            # Added a "-" to these next 2 values because they would be moved to the other side of the equation
            mult1 = -x1 * a
            mult2 = -x2 * a
            (num1,den1) = simplify_fraction_quadratic(a,mult1)
            (num2,den2) = simplify_fraction_quadratic(a,mult2)
            if ((num1 > a) or (num2 > a)):
                # simplify fraction will make too large of num and denom to try to make a sqrt work
                print("No factorization")
            else:
                # Getting ready to make the print look nice
                if (den1 > 0):
                    sign1 = "+"
                else:
                    sign1 = ""
                if (den2 > 0):
                    sign2 = "+"
                else:
                    sign2 = ""
                print("({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
        else:
            # if the part under the sqrt is negative, you have a solution with i
            print("Solutions are imaginary")
        return
    
    a = input("What is your a? (y=ax^2+bx+c) ")
    b = input("What is your b? (y=ax^2+bx+c) ")
    c = input("What is your c? (y=ax^2+bx+c) ")

    quadratic_function(int(a),int(b),int(c))
else:
    print("You entered an invalid option.")