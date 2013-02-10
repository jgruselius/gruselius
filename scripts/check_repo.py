
import sys
import os
from gruselius.session3 import CourseRepo, TemporarilyChangeDir

def main(args):
	if len(args) != 1:
		help()
	elif not os.path.exists(args[0]):
		print("The path '{0}' does not exist".format(args[0]))
	else:
		path = os.path.abspath(args[0])
		with TemporarilyChangeDir(path):
			cr = CourseRepo(os.path.basename(path))
			if cr.check():
				print("PASS")
			else:
				print("FAIL")

def help():
	print("Usage:\n\tcheck_repo.py <path>\n")

if __name__ == "__main__":
	main(sys.argv[1:])
