import urllib2
import re


def getUrl(name,page_code):
	match = re.compile(r'/show/[0-9]+\">%s</a>' % name,re.IGNORECASE)
	m = match.search(page_code) #search in text
	if m:
		word = page_code[m.start()+6:m.end()] #only the number
		quote = word.index('"')
		close_href = word.find('</a>',quote)
		name = word[quote+2:close_href]
		return word[:quote], name 
	else:
		return None, None

def getUrlSubtitle(s_season, s_chapter, page_code):
	form = s_season+"x"+s_chapter
	match = re.compile(r'/%s' % form, re.IGNORECASE)
	m = match.search(page_code)

	if m:
		start_url = page_code.find('http://www.subtitulos.es/updated/1', m.end())
		end_url = page_code.find('"', start_url)
		subtitle = page_code[start_url:end_url]
		return subtitle
	else:
		return None


def main():
	r = urllib2.urlopen("http://www.subtitulos.es/series")
	page_code = r.read()
	s_name = raw_input("Ingresa el nombre de tu serie: ")
	url, name = getUrl(s_name,page_code)

	s_season = raw_input("Ingresa la temporada: ") #1,2,3,4
	s_chapter = raw_input("Ingresa el capitulo de la temporada: ") # 01,02...10,11...

	url_req = "http://www.subtitulos.es/ajax_loadShow.php?show="+url+"&season="+s_season
	q = urllib2.urlopen(url_req)
	page_code = q.read()
	url_subtitle = getUrlSubtitle(s_season, s_chapter, page_code)
	print "URL SUBTITLE ", url_subtitle
   
main()

