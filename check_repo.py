
import sys
import os
from gruselius.session3 import CourseRepo, TemporarilyChangeDir

def main(args):
	with TemporarilyChangeDir(args[0]):
		cr = CourseRepo(os.path.basename(args[0]))
		if cr.check():
			print("PASS")
		else:
			print("FAIL")

if __name__ == "__main__":
	main(sys.argv[1:])
