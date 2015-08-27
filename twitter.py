import requests


def tweet(body):
    # placeholder function so that imports work
    pass

def list_twitter_repos():
	"""
	Get the first page of twitter repo information from the GitHub API
	"""
	url = 'https://api.github.com/orgs/twitter/repos'
	repo_response = requests.get(url)
	
	if repo_response.status_code == 500:
		return 'The GitHub API is currently unavailable'
		
	return [r['name'] for r in repo_response.json()]