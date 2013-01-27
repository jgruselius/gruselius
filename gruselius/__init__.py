import untangle

def getFractionOfOutagesByReason(url, reason)
	doc = untangle.parse(url)
	tot = 0
	count = 0
	for outage in doc.NYCOutages.outage:
		tot += 1
		if outage.reason.cdata == reason:
			n += 1
	return n/tot
