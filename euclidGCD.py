# Euclids algorithm to find Greatest Common Denominator

import sys
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
def gcd(a, b): 
	while a!=b: 
		if b>a : 
			a,b = b,a 
		a = a-b 
	return a 
print gcd(a, b) 
