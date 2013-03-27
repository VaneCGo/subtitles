#You can save the season that you actualy are seeing and
#then the program list the chapters. You choose one and then its being downloaded.

#class NombreClase():

#	def __init__(self):
	
import urllib2
import re

def getUrl(name):
	r = urllib2.urlopen("http://www.subtitulos.es/series")
	page_code = r.read()
	match = re.compile(r'/show/[0-9]+\">%s</a>' % name,re.IGNORECASE)
	m = match.search(page_code) #search in text
	if m:
		pal = page_code[m.start():m.end()]
		quote = pal.index('"')
		return pal[:quote] 
	else:
		return None

def main():
	s_name = raw_input("Ingresa el nombre de tu serie: ")
	url = getUrl(s_name)
	if url:
		print "url:",url,"name:",s_name

   
main()

