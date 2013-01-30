#!/Users/joelgruselius/.virtualenvs/py2.7/bin/python
import sys
from gruselius import getFractionOfOutagesBy

def main(args):
	xmlUrl = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
	reason = "REPAIR"
	fraction = getFractionOfOutagesBy(xmlUrl, reason)
	print("Fraction of outages with reason {0}: {1}".format(reason, fraction))

if __name__ == "__main__":
	main(sys.argv[1:])
