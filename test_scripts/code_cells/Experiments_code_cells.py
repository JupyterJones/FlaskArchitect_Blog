from bs4 import BeautifulSoup
import requests
import re
from urllib.request import Request, urlopen
import os
import cookiejar
import json

def get_soup(url,header):
    soup = BeautifulSoup(urlopen(url))
    return soup# BeautifulSoup(url, "html.parser")#,headers={'User-Agent': 'Mozilla/5.0'}),'html.parser')


#query = input("query image: ")# you can change the query for the image  here
#query ="mechanical spider"
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://search.naver.com/search.naver?sm=tab_sug.top&where=image&query=Roman+Architecture&oquery=steampunk+armor&tqi=hyXQywp0J1ZssU6w%2Bjlssssstmw-046608&acq=roman+archi&acr=2&qdt=0"
print (url)
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("img"):#,{"class":"rg_meta"}):
    print(a)

from urllib.request import Request, urlopen#from urllib.request import urlopen
url="https://search.naver.com/search.naver?sm=tab_sug.top&where=image&query=Roman+Architecture&oquery=steampunk+armor"
headers = {'User-Agent': 'Mozilla/5.0'}
request = Request(url, headers=headers)
html = urlopen(request).read()
store = open("TEMP.html","a+")
store.write(str(html))


from urllib.request import Request, urlopen#from urllib.request import urlopen
url="https://pxhere.com/en/photos?q=frogs&search="
headers = {'User-Agent': 'Mozilla/5.0'}
request = Request(url, headers=headers)
html = urlopen(request).read()
store = open("TEMP2.html","a+")
store.write(str(html))


stored = open(r"TEMP2.html","r").readlines()
for line in stored:
    line = str(line)
    lines = line.split("https:")
    for data in lines:
        #print(data)
        if "jpg" in data:
            print("https:"+data)
        #print ("https"+str(line))
        #print(line)

import requests
url = 'https://www.inside.com.tw'
headers = {'User-Agent': 'Mozilla/5.0'}
html = requests.get(url, headers=headers).content

With urllib, you need to create a Request object, and add your headers to it:

from urllib.request import Request, urlopen
url = 'https://www.inside.com.tw'
headers = {'User-Agent': 'Mozilla/5.0'}
request = Request(url, headers=headers)
html = urlopen(request).read()


from bs4 import BeautifulSoup
import requests
import re
from urllib.request import Request, urlopen
import os
import cookiejar
import json

def get_soup(url,header):
    soup = BeautifulSoup(urlopen(url))
    return soup# BeautifulSoup(url, "html.parser")#,headers={'User-Agent': 'Mozilla/5.0'}),'html.parser')


#query = input("query image: ")# you can change the query for the image  here
#query ="mechanical spider"
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://search.naver.com/search.naver?sm=tab_sug.top&where=image&query=Roman+Architecture&oquery=steampunk+armor&tqi=hyXQywp0J1ZssU6w%2Bjlssssstmw-046608&acq=roman+archi&acr=2&qdt=0"
print (url)
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("img"):#,{"class":"rg_meta"}):
    print(a)
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print  ("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        req = urllib2.Request(img, headers={'User-Agent' : header})
        raw_img = urllib2.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print (cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print ("could not load : "+img)
        print (e)

from urllib.request import Request, urlopen  # for Python 3: from urllib.request import urlopen
from bs4 import BeautifulSoup
query = "flowers"
URL = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
soup = BeautifulSoup(urlopen(URL))



The urllib module doesn't quite work the same way as the preferred requests module.
Where with requests you might use:

import requests
url = 'https://www.inside.com.tw'
headers = {'User-Agent': 'Mozilla/5.0'}
html = requests.get(url, headers=headers).content

With urllib, you need to create a Request object, and add your headers to it:

from urllib.request import Request, urlopen
url = 'https://www.inside.com.tw'
headers = {'User-Agent': 'Mozilla/5.0'}
request = Request(url, headers=headers)
html = urlopen(request).read()



# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

search_queries =['The smartphone also features an in display fingerprint sensor.',
'The pop up selfie camera is placed aligning with the rear cameras.',
'''In terms of storage Vivo V15 Pro could offer
up to 6GB of RAM and 128GB of onboard storage.''',
'The smartphone could be fuelled by a 3 700mAh battery.',]


def downloadimages(query):
	# keywords is the search query
	# format is the image file format
	# limit is the number of images to be downloaded
	# print urs is to print the image file url
	# size is the image size which can
	# be specified manually ("large, medium, icon")
	# aspect ratio denotes the height width ratio
	# of images to download. ("tall, square, wide, panoramic")
	arguments = {"keywords": query,
				"format": "jpg",
				"limit":4,
				"print_urls":True,
				"size": "medium",
				"aspect_ratio":"panoramic"}
	try:
		response.download(arguments)
	
	# Handling File NotFound Error	
	except FileNotFoundError:
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":4,
					"print_urls":True,
					"size": "medium"}
					
		# Providing arguments for the searched query
		try:
			# Downloading the photos based
			# on the given arguments
			response.download(arguments)
		except:
			pass

# Driver Code
for query in search_queries:
	downloadimages(query)
	print()


# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

#search_queries =['mechanical beetles', 'mechanical grasshopper.', 'steampunk spiders',]
search_queries =['beetles', 'grasshopper', 'spiders',]

def downloadimages(query):
	# keywords is the search query
	# format is the image file format
	# limit is the number of images to be downloaded
	# print urs is to print the image file url
	# size is the image size which can
	# be specified manually ("large, medium, icon")
	# aspect ratio denotes the height width ratio
	# of images to download. ("tall, square, wide, panoramic")
	arguments = {"keywords": query,
				"format": "jpg",
				"limit":4,
				"print_urls":True,
				"size": "medium",
				"aspect_ratio":"panoramic"}
	try:
		response.download(arguments)
	
	# Handling File NotFound Error	
	except FileNotFoundError:
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":4,
					"print_urls":True,
					"size": "medium"}
					
		# Providing arguments for the searched query
		try:
			# Downloading the photos based
			# on the given arguments
			response.download(arguments)
		except:
			pass

# Driver Code
for query in search_queries:
	downloadimages(query)
	print()




