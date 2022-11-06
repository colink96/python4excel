# do imports
import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import urljoin

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
url = ("https://www.youtube.com/user/guru99com")
download_queue = []

def get_links(url, parent_url, file_location):
 try:
  # For reference: https://stackoverflow.com/questions/7933417/how-do-i-set-headers-using-pythons-urllib
  req = Request(url)
  req.add_header("referer", url)
  req.add_header("user-agent", UserAgent)
  html = urlopen(req).read()

  soup = BeautifulSoup(html, 'html.parser')
  for link in soup.find_all('a'):

# What is this 'if' block for?
#    if(link.text == '../'):
#     continue
  
   link_name = urljoin(parent_url, link.get('href'))
   location_name = file_location + link.text

#  What is the purpose of calling get_links again? Right now the below lines will 
#  infinitely loop.
#    if(link_name.endswith('/')):
#     get_links(link_name, url, location_name) #call again over the gathered links
#    else:

   download_queue.append(tuple((link_name, file_location)))
  
 # In general, try to print out error messages so it's easier to find 
 # where the problems are.  
 except Exception as e: print(e)


def download(url, location):
 command = 'wget ' + url + ' -P ' + location
 os.system(command)


print('Enter the base url that you want to scrape')
url = input()

print('Enter the base location to save')
location = input()

get_links(url, url, location) #get all the links from the base url

print('All links crawled, starting download now')

for i in range(len(download_queue)):
 download(download_queue[i][0], download_queue[i][1])