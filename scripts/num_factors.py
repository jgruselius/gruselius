import argparse

def main(arg):
	modes = {"s": method1, "i": method2, "i": method3}
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