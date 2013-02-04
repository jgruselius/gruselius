
import sys
import os
from gruselius.session3 import CourseRepo, TemporarilyChangeDir

def main(args):
	if len(args) != 1:
		help()
	else:
		with TemporarilyChangeDir(os.path.abspath(args[0])):
			cr = CourseRepo("gruselius")
			if cr.check():
				print("PASS")
			else:
				print("FAIL")

def help():
	print("Usage:\n\tcheck_repo.py <path>\n")

if __name__ == "__main__":
	main(sys.argv[1:])
