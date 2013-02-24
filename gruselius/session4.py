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
	ORG_URL = "https://api.github.com/orgs/pythonkurs"
	repo_data = requests.get(ORG_URL+"/repos", auth=(user, password)).json()
	d = {}
	for repo in repo_data:
		url = repo["url"]+"/commits"
		commit_data = requests.get(url, auth=(user, password)).json()
		dates = []
		messages = []
		# Skip repos with no commits:
		if len(commit_data) > 1:
			for commit in commit_data:
				dates.append(parser.parse(commit["commit"]["committer"]["date"]))
				messages.append(commit["commit"]["message"])
			d[repo["name"]] = Series(messages, index=dates)

	return DataFrame(d)

# (Not part of session 4 task)
def get_date_of_most_commits(df):
	# Count all non-NA/null commit messages, resample index to per day and
	# return the index (day) with highest summed counts of commits:
	return df.count(1).resample("D",how="sum").idxmax()

def get_commits_by_weekday(df):
	commits_by_date = df.count(1).resample("D",how="sum").dropna()
	weekday_count = {}
	for i in xrange(len(commits_by_date)):
		day = commits_by_date.index[i].strftime("%A")
		commits = commits_by_date[i]
		if day in weekday_count:
			weekday_count[day] += commits
		else:
			weekday_count[day] = commits
	return weekday_count

def get_commits_by_hour(df):
	commits_by_hour = df.count(1).resample("H",how="sum").dropna()
	hour_count = {}
	for i in xrange(len(commits_by_hour)):
		hour = commits_by_hour.index[i].hour
		commits = commits_by_hour[i]
		if hour in hour_count:
			hour_count[hour] += commits
		else:
			hour_count[hour] = commits
	return hour_count

# Returns the key in d with highest value and that value:
def get_max(d):
	key = max(d, key=d.get)
	return(key, d[key])

