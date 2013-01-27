from gruselius import getFractionOfOutakesCausedBy

xmlUrl = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
reason = "REPAIR"
fraction = getFractionOfOutakesCausedBy(xmlUrl, reason)
print("Fraction of outages with reason {0}: {1}".format(reason, fraction))
