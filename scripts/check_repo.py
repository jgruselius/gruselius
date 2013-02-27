
import argparse
import os
from gruselius.session3 import CourseRepo, TemporarilyChangeDir

#@profile
def main(path):
	if not os.path.exists(path):
		print("The path '{0}' does not exist".format(path))
	else:
		path = os.path.abspath(path)
		with TemporarilyChangeDir(path):
			cr = CourseRepo(os.path.basename(path))
			if cr.check():
				print("PASS")
			else:
				print("FAIL")

if __name__ == "__main__":
	# To work with profilers the last argument is used as path
	p = argparse.ArgumentParser(description="Checks if the specified path" +
		"contains the required files")
	p.add_argument("path", help="The path to check", nargs="+")
	args = p.parse_args()
	main(args.path[-1])
