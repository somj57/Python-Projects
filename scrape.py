# Just run it and know what it is 🚀
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news?p=1')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')

subtext  = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
	return sorted(hnlist,key = lambda k:k['votes'],reverse = True)

def create_custom_hn(links,subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		votes = subtext[idx].select('.score')
		href = links[idx].get('href', None)
		#print(votes)
		if len(votes):
			points = int(votes[0].getText().replace(' points',''))
			if points >99:
				#print(points)
				hn.append({'title':title,'link':href, 'votes':points})
	return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(links,subtext))
#print(create_custom_hn(links,votes))
