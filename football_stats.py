from bs4 import BeautifulSoup
import urllib2

def print_players():
	nlf_url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns'
	req = urllib2.Request(nlf_url)
	response = urllib2.urlopen(req)
	the_page = response.read()
	soup = BeautifulSoup(the_page, 'html.parser')
	data = soup.findAll(class_ = {'row1','row2'})[:20]
	results = 'Player: {:^20}| Position: {:^3}| Team: {:^4}| TD\'s {:^3}'
	for row in data:
	    print results.format(row.contents[0].text, row.contents[1].text, 
	    	row.contents[2].text, row.contents[6].text)


def print_stocks():
	pass

        
if __name__ == '__main__':
    print_players()
    
