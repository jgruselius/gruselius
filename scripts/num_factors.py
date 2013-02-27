"""Python course session 7 assignment"""

import argparse

def function1():
	"""Sequential non-parallel function"""
	pass

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
		modes[arg]()

if __name__ == "__main__":
	p = argparse.ArgumentParser("...")
	p.add_argument("mode", help="The mode to run in: s: sequential, " +
		"m: parallel with multiprocessing, i: parallel with iPython",
		choices=("s","m","i"))
	args = p.parse_args()
	main(args.mode)
