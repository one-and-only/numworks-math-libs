_A='Division by 0 - result undefined'
from decimal import Decimal
from math import sqrt
def gcd(a,b):
	while b:a,b=b,a%b
	return a
def simplify_fraction(numer,denom):
	A='/'
	if denom==0:return _A
	common_divisor=gcd(numer,denom);reduced_num,reduced_den=numer/common_divisor,denom/common_divisor
	if common_divisor==1:print(str(Decimal(numer).normalize())+A+str(Decimal(denom).normalize()))
	elif reduced_den>denom:
		if reduced_den*reduced_num<0:print(str(Decimal(-reduced_num).normalize())+A+str(Decimal(-reduced_den).normalize()))
		else:print('Debug divisor other than');print(str(Decimal(reduced_num).normalize())+A+str(Decimal(reduced_den).normalize()))
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