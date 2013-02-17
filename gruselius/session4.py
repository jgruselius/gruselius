import requests
from dateutil import parser
from pandas import Series
from pandas import DataFrame
import getpass

def input_credentials():
	user = raw_input("GitHub username:")
	password = getpass.getpass("Password:")
	return (user, password)


def get_commit_history():
	user, password = input_credentials()
	org_url = "https://api.github.com/orgs/pythonkurs"
	repo_data = requests.get(org_url+"/repos", auth=(user, password)).json()
	d = {}
	for repo in repo_data:
		url = repo["url"]+"/commits"
		commit_data = requests.get(url, auth=(user, password)).json()
		dates = []
		messages = []
		if len(commit_data) > 1:
			for commit in commit_data:
				dates.append(parser.parse(commit["commit"]["committer"]["date"]))
				messages.append(commit["commit"]["message"])
			d[repo["name"]] = Series(messages, index=dates)

	return DataFrame(d)

def get_date_of_most_commits(df):
	df.count(1).resample("D",how="sum").idxmax()
