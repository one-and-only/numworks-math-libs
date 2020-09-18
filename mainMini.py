import numworksLibsMini
def page1():
	B='2';A='1';prgrmchoice=input('Select From One of the Programs:\n1. Simplify a Fraction (Numerical)\n2. Factor a Quadratic Function\n3. Solve Y in Linear Functions\n4. Find D:{}, R:{} of Function\n"q" to quit\nYour Choice: ')
	if prgrmchoice==A:numer=int(input('Enter the Numerator of the Fraction: '));denom=int(input('Enter the Denominator of the Fraction: '));numworksLibsMini.simplify_fraction(numer,denom)
	elif prgrmchoice==B:a=input('What is your a? (y=ax^2+bx+c) ');b=input('What is your b? (y=ax^2+bx+c) ');c=input('What is your c? (y=ax^2+bx+c) ');numworksLibsMini.quadratic_function(int(a),int(b),int(c))
	elif prgrmchoice=='3':func_name=input('Function Name: (f(x)) ');m=input('What is your m? (y=mx+b) ');x=input('What is you x? (y=mx+b) ');b=input('What is your b? (y=mx+b) ');numworksLibsMini.solve_linear_func(func_name,m,x,b)
	elif prgrmchoice=='4':
		choice=input('Choose Input Method:\n1. Equation\n2. Ordered Pairs\nMethod: ')
		if choice==A:equation=input('Input Your Equation: ');numworksLibsMini.find_domain_range_equation(equation)
		elif choice==B:ordered_pair_num=1;xs=[];ys=[];numworksLibsMini.get_ordered_pair(ordered_pair_num,xs,ys)
	elif prgrmchoice=='q':print('Bye, see you soon!');quit()
	else:print('You entered an invalid option')
page1()