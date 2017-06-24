from BeautifulSoup import BeautifulSoup
import urllib2
import requests # required modules
import sys
links = [] # array for storing the crawled links of the webpage
brokenLinks = []
def crawl(p): #function to check for broken links of a particular *webpage*
	html_page = urllib2.urlopen(p)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll("a"):  # crawling the <a> tags for links
		x = link.get("href")
		if 'https' in x:   	# filtering out the links
			# print x : debug mode
			links.append(x)
			continue
		if 'http' in  x:
			# print x : debug mode
			links.append(x)
			continue
		
	final_links = []
	for lin in soup.findAll("img"): # crawling the <img> tags
		x = lin.get("src")
		# print x : debug mode
		final_links.append(x)
	for y in final_links:
		if 'data' in y:	# filtering out the links
			continue
		links.append(x)
		# print x : debug mode
	for li in soup.findAll("script"): # crawling the <script> tags
		x = li.get("src")
		# print x : debug mode
		if x != None : 	#filtering out written script from external script
			links.append(x)
	for l in soup.findAll("link"): # crawling the <link> tags
		x = l.get("href")
		# print x : debug mode
		l.append(x) 
	for y in links:         	# now making a get request to the links found and determining whether they are broken 
		resp = requests.get(y)
		status = resp.status_code
		if status != 200 : 	# if status code is not 200 then assuming it to be a broken link 
			brokenLinks.append(y)
			print "\t\033[91m[%d] %s" %(status,y)        	
		else:
			print "\t\033[92m[%d] %s" %(status,y)	
		
crawl(sys.argv[1])
