import main
from math import sqrt

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def clean_num(reduced_num):
    culprit = '.0'
    reduced_num_str = str(reduced_num)
    if reduced_num_str.endswith(culprit):
        reduced_num_clean = reduced_num_str[:-(len(culprit))]
        reduced_num = int(reduced_num_clean)
    return reduced_num

def clean_den(reduced_den):
    culprit = '.0'
    reduced_den_str = str(reduced_den)
    if reduced_den_str.endswith(culprit):
        reduced_den_clean = reduced_den_str[:-(len(culprit))]
        reduced_den = int(reduced_den_clean)
    return reduced_den

def drop_one_denom(reduced_num):
    print(str(reduced_num))

def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if common_divisor == 1:
        reduced_num = clean_num(reduced_num)
        reduced_den - clean_den(reduced_den)

        if reduced_den == 1.0:
            drop_one_denom(reduced_num)
        else:
            print(str(reduced_num)+"/"+str(reduced_den))
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                print(str(-reduced_num)+"/"+str(-reduced_den))
            else:
                print("Debug divisor other than")

                print(str(reduced_num)+"/"+str(reduced_den))
        else:

            reduced_num = clean_num(reduced_num)
            reduced_den = clean_den(reduced_den)
            
            if reduced_den == -1:
                drop_one_denom(reduced_num)
            else:
                print(str(reduced_num)+"/"+str(-reduced_den))

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

def solve_linear_func(func_name, m, x, b):
    mx = (int(m)*int(x))
    y = int(mx) + int(b)
    print(func_name+"("+str(x)+")= "+str(y))

def find_domain_range_equation(equation):
    if 'x' or 'X' in equation:
        print('Infinite domain and range')

def find_domain_range_ordered(xs, ys):
    sd = ", "
    sr = ", "
    xsu = []
    ysu = []
    for i in xs:
        if i not in xsu:
            xsu.append(i)
    for i in ys:
        if i not in ysu:
            ysu.append(i)
    sd = sd.join(xsu)
    domainstr = "Domain: "+sd
    print(domainstr)
    sr = sr.join(ysu)
    rangestr = "Range: "+sr
    print(rangestr)
    exit()

def get_ordered_pair(ordered_pair_num, xs, ys):
    x = 0
    y = 0
    while (x is not None and y is not None):
        x = input("x for point #"+str(ordered_pair_num)+"(sbm): ")
        if (x == ""):
            print("Got empty, quitting...")
            main.page1()
        elif (x != ""):
            if (RepresentsFloat(x)):
                print("Loading...")
            elif (x == "sbm"):
                if ((xs == []) or (ys == [])):
                    print("Submission can't be empty")
                    get_ordered_pair(ordered_pair_num, xs, ys)
                find_domain_range_ordered(xs, ys)
            elif (any(c.isalpha() for c in x)):
                print("Must be a number!")
                get_ordered_pair(ordered_pair_num, xs, ys)
        y = input("y for point #"+str(ordered_pair_num)+": ")
        if (y == ""):
            print("y cannot be empty")
            get_ordered_pair(ordered_pair_num, xs, ys)
        elif (y != ""):
            if (RepresentsFloat(y)):
                print("loading...")
                ordered_pair_num += 1
            elif (any(c.isalpha() for c in x)):
                print("Must be a number!")
                get_ordered_pair(ordered_pair_num, xs, ys)
        xs += x
        ys += y