import untangle

def getFractionOfOutagesBy(url, reason):
	doc = untangle.parse(url)
	tot = 0
	count = 0
	for outage in doc.NYCOutages.outage:
		tot += 1
		if outage.reason.cdata == reason:
			count += 1
	return float(count)/tot
