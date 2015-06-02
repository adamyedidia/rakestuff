import sys
import math
import matplotlib.pyplot as pl

def fac(n):
	if n <= 0:
		return 1
	else:
		return n*fac(n-1)

def choose(n, k):
	return fac(n)/(fac(k)*fac(n-k))

T = int(sys.argv[1])

y = [math.log(sum([choose(T, p) for p in range(P+1)]), 2) for P in range(T+1)]
x = range(T+1)

print math.log(sum([choose(T, p) for p in range(int(2*T/math.log(T, 2)))]), 2)/T

print int(2*T/math.log(T, 2))

pl.plot(x, y)

