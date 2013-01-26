import untangle

xmlUrl = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
lookFor = "REPAIR"
doc = untangle.parse(xmlUrl)

tot = 0
count = 0
for outage in doc.NYCOutages.outage:
	tot += 1
	if outage.reason.cdata == lookFor:
		n += 1

print("Fraction of outages with reason {0}: {1}".format(lookFor, count/tot))
