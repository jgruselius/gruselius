"""Python course session 7 assignment"""

import argparse
import time
import multiprocessing
from IPython.parallel import Client

RANGE = (2,50000)

"""
Build a collection of all unique factors:
Method 1, building a set (8.9 s):
unique_factors = set()
for i in xrange(*RANGE):
	unique_factors.update(factorize(i))
Method 2, set from list comprehension (8.7 s):
unique_factors = set([factor for i in xrange(*RANGE) for factor in factorize(i)])
Method 3, set from map (9.33 s):
unique_factors = set([factor for factors in map(factorize, xrange(*RANGE)) for factor in factors])
return len(unique_factors)
"""

def factorize(n):
	if n < 2:
		return []
	factors = []
	p = 2
	while True:
		if n == 1:
			return factors
		r = n % p
		if r == 0:
			factors.append(p)
			n = n / p
		elif p * p >= n:
			factors.append(n)
			return factors
		elif p > 2:
			p += 2
		else:
			p += 1

def number_of_unique_factors(n):
	return len(set(factorize(n)))

def count_unique(iterable):
	counts = {}
	for n in iterable:
		if n in counts:
			counts[n] += 1
		else:
			counts[n] = 1
	return counts

def function1():
	"""Sequential non-parallel function"""
	return [number_of_unique_factors(i) for i in xrange(*RANGE)]

def function2():
	"""Parallelized using multiprocessing"""
	pool = multiprocessing.Pool()
	return pool.map(number_of_unique_factors, xrange(*RANGE))

def function3():
	"""Parallelized using iPython"""
	dview = Client()[:]
	return dview.map(number_of_unique_factors, xrange(*RANGE))

def main(arg):
	modes = {"s": function1, "m": function2, "i": function3}
	if not arg in modes:
		raise NameError
	else:
		t0 = time.time()
		print(count_unique(modes[arg]()))
		print("Timer: {0} s".format(time.time()-t0))

if __name__ == "__main__":
	p = argparse.ArgumentParser("Factorize integers from {0} to {1}".format(*RANGE))
	p.add_argument("mode", help="The mode to run in: s: sequential, " +
		"m: parallel with multiprocessing, i: parallel with iPython",
		choices=("s","m","i"))
	args = p.parse_args()
	main(args.mode)
