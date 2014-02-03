from BeautifulSoup import BeautifulSoup 
import urllib2
import re

tripler_URL = "http://www.rrr.org.au/"



def get_podcasts():
    url = "http://rrrfm.libsyn.com/rss/category/Breakfasters"
    page = urllib2.urlopen(url, "xml")
    soup = BeautifulSoup(page.read())
    #urls = soup.findAll(type="audio/mpeg")
    urls = soup.findAll(text=re.compile("traffic.libsyn.com"))
    titles = soup.findAll('title')
    output = []
    for i in urls:
        for t in titles:
            output.append({'url': i, 'title': t.text})
            final_output = output[0:20]
    return final_output

