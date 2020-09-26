import numworksLibs

def page1():
    prgrmchoice = input("Select From One of the Programs:\n1. Simplify a Fraction (Numerical)\n2. Factor a Quadratic Function\n3. Solve Y in Linear Functions\n4. Find D:{}, R:{} of Function\n\"q\" to quit\nYour Choice: ")
    if (prgrmchoice == "1"):
        numer = int(input("Enter the Numerator of the Fraction: "))
        denom = int(input("Enter the Denominator of the Fraction: "))
        answer = numworksLibs.simplify_fraction(numer, denom)
        print(answer)
        return answer
    elif (prgrmchoice == "2"):
        a = input("What is your a? (y=ax^2+bx+c) ")
        b = input("What is your b? (y=ax^2+bx+c) ")
        c = input("What is your c? (y=ax^2+bx+c) ")
        answer = numworksLibs.quadratic_function(int(a),int(b),int(c))
        print(answer)
        return answer
    elif (prgrmchoice == "3"):
        func_name = input("Function Name: (f(x)) ")
        m = input("What is your m? (y=mx+b) ")
        x = input("What is you x? (y=mx+b) ")
        b = input("What is your b? (y=mx+b) ")
        answer = numworksLibs.solve_linear_func(func_name, m, x, b)
        print(answer)
        return answer
    elif (prgrmchoice == "4"):
        choice = input("Choose Input Method:\n1. Equation\n2. Ordered Pairs\nMethod: ")
        if (choice == "1"):
            equation = input("Input Your Equation: ")
            answer = numworksLibs.find_domain_range_equation(equation)
            print(answer)
            return answer
        elif (choice == "2"):
            ordered_pair_num = 1
            xs = []
            ys = []
            answer = numworksLibs.get_ordered_pair(ordered_pair_num, xs, ys)
            print(answer)
            return answer
    elif (prgrmchoice == "q"):
        print("Bye, see you soon!")
        quit()
    else:
        print("You entered an invalid option")