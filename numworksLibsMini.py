_A='Division by 0 - result undefined'
import mainMini
from math import sqrt
def RepresentsFloat(s):
	try:float(s);return True
	except ValueError:return False
def gcd(a,b):
	while b:a,b=b,a%b
	return a
def simplify_fraction(numer,denom):
	A='/'
	if denom==0:return _A
	common_divisor=gcd(numer,denom);reduced_num,reduced_den=numer/common_divisor,denom/common_divisor
	if common_divisor==1:print(str(numer)+A+str(denom))
	elif reduced_den>denom:
		if reduced_den*reduced_num<0:print(str(-reduced_num)+A+str(-reduced_den))
		else:print('Debug divisor other than');print(str(reduced_num)+A+str(reduced_den))
	else:print(str(reduced_num)+A+str(reduced_den))
def simplify_fraction_quadratic(numer,denom):
	if denom==0:return _A
	common_divisor=gcd(numer,denom);reduced_num,reduced_den=numer/common_divisor,denom/common_divisor
	if common_divisor==1:return numer,denom
	elif reduced_den>denom:
		if reduced_den*reduced_num<0:return-reduced_num,-reduced_den
		else:return reduced_num,reduced_den
	else:return reduced_num,reduced_den
def quadratic_function(a,b,c):
	A='+'
	if b**2-4*a*c>=0:
		x1=(-b+sqrt(b**2-4*a*c))/(2*a);x2=(-b-sqrt(b**2-4*a*c))/(2*a);mult1=-x1*a;mult2=-x2*a;num1,den1=simplify_fraction_quadratic(a,mult1);num2,den2=simplify_fraction_quadratic(a,mult2)
		if num1>a or num2>a:print('No factorization')
		else:
			if den1>0:sign1=A
			else:sign1=''
			if den2>0:sign2=A
			else:sign2=''
			print('({}x{}{})({}x{}{})'.format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
	else:print('Solutions are imaginary')
	return
def solve_linear_func(func_name,m,x,b):mx=int(m)*int(x);y=int(mx)+int(b);print(func_name+'('+str(x)+')= '+str(y))
def find_domain_range_equation(equation):
	if'x'or'X'in equation:print('Infinite domain and range')
def find_domain_range_ordered(xs,ys):
	A=', ';sd=A;sr=A;xsu=[];ysu=[]
	for i in xs:
		if i not in xsu:xsu.append(i)
	for i in ys:
		if i not in ysu:ysu.append(i)
	sd=sd.join(xsu);domainstr='Domain: '+sd;print(domainstr);sr=sr.join(ysu);rangestr='Range: '+sr;print(rangestr);exit()
def get_ordered_pair(ordered_pair_num,xs,ys):
	B='Must be a number!';A=None;x=0;y=0
	while x is not A and y is not A:
		x=input('x for point #'+str(ordered_pair_num)+'(sbm): ')
		if x=='':print('Got empty, quitting...');mainMini.page1()
		elif x!='':
			if RepresentsFloat(x):print('Loading...')
			elif x=='sbm':
				if xs==[]or ys==[]:print("Submission can't be empty");get_ordered_pair(ordered_pair_num,xs,ys)
				find_domain_range_ordered(xs,ys)
			elif any((c.isalpha()for c in x)):print(B);get_ordered_pair(ordered_pair_num,xs,ys)
		y=input('y for point #'+str(ordered_pair_num)+': ')
		if y=='':print('y cannot be empty');get_ordered_pair(ordered_pair_num,xs,ys)
		elif y!='':
			if RepresentsFloat(y):print('loading...');ordered_pair_num+=1
			elif any((c.isalpha()for c in x)):print(B);get_ordered_pair(ordered_pair_num,xs,ys)
		xs+=x;ys+=y