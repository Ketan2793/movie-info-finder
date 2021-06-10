import requests
import bs4

def get_movie_score(movie_name):
    movie_name = movie_name.replace(" ","_")
    res = requests.get("https://www.rottentomatoes.com/m/"+movie_name)
    if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text,"lxml")
            score=soup.select('.scoreboard')[0].get('tomatometerscore')
    else:
	        score='NA'
    return score
	
	
	
def get_imdb_rating(movie_name):
    try:
        url = 'https://www.imdb.com'
        query = '/search/title?title='   
        MovieNameQuery = query+'+'.join(movie_name.strip().split(' '))
        res = requests.get(url+MovieNameQuery+'&title_type=feature')
        soup = bs4.BeautifulSoup(res.text,"lxml")
        movie_query=url + soup.select('h3')[0].find('a').get('href')+'ratings/'
        res = requests.get(movie_query)
        soup = bs4.BeautifulSoup(res.text,"lxml")
        rating=soup.select('.ipl-rating-star__rating')[0].text
        return rating
    except:
        return 'NA'
		

def get_critical_consensus(movie_name):
    movie_name = movie_name.replace(" ","_")
    res = requests.get("https://www.rottentomatoes.com/m/"+movie_name)
    if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text,"lxml")
            consensus=soup.select('.what-to-know__section-body')[0].find('span').text
    else:
            consensus='NA'
    return consensus
	
def get_imdb_plot(movie_name):
    try:
        url = 'https://www.imdb.com'
        query = '/search/title?title='   
        MovieNameQuery = query+'+'.join(movie_name.strip().split(' '))
        res = requests.get(url+MovieNameQuery+'&title_type=feature')
        soup = bs4.BeautifulSoup(res.text,"lxml")
        movie_query=url + soup.select('h3')[0].find('a').get('href')+'plotsummary'
        res = requests.get(movie_query)
        soup = bs4.BeautifulSoup(res.text,"lxml")
        plot=soup.select('.ipl-zebra-list__item')[0].find('p').text
        return plot
    except:
        return 'NA'

	
	
	

