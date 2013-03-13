"""Python course session 7 assignment"""

import argparse
import time
import multiprocessing
#import iPython.parallel

RANGE = (2,50000)

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

def function1():
	t0 = time.clock()
	"""Sequential non-parallel function"""
	factor_count = {}
	fco = {}
	for i in xrange(*RANGE):
		count = len(set(factorize(i)))
		factor_count[i] = count
		if count in fco:
			fco[count] += 1
		else:
			fco[count] = 1
	""" 
	factors = set([factor for i in xrange(RANGE) for factor in factorize(i)])
	"""
	print("{}".format(time.clock()-t0))
	return fco

def function2():
	"""Parallelized using multiprocessing"""
	pass

def function3():
	"""Parallelized using iPython"""
	pass

def main(arg):
	modes = {"s": function1, "i": function2, "i": function3}
	if not arg in modes:
		raise NameError
	else:
		print(modes[arg]())

if __name__ == "__main__":
	p = argparse.ArgumentParser("...")
	p.add_argument("mode", help="The mode to run in: s: sequential, " +
		"m: parallel with multiprocessing, i: parallel with iPython",
		choices=("s","m","i"))
	args = p.parse_args()
	main(args.mode)
