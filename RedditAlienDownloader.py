# Library for reading page source
import urllib2

# Library for parsing page source
# This script requires the use of Beautiful Soup, found here:
# http://www.crummy.com/software/BeautifulSoup/
from BeautifulSoup import BeautifulSoup

# Libraries for downloading files
import os
import sys

downloadFolder = "/Users/alex/Desktop" # Replace with desired destination folder

# Get desired subreddit from user input
URLString = "http://www.reddit.com"
subreddit = raw_input("Enter subreddit name: ")
if len(subreddit) > 0:
    URLString += "/r/%s/" % subreddit

try:
    # Copy page source to pageSource variable
    hdr = {'User-Agent' : 'super happy flair bot by /u/spladug'}
    req = urllib2.Request(URLString, headers=hdr)
    page = urllib2.urlopen(req)
    pageSource = page.read()
    page.close()

    # Parse page source
    soup = BeautifulSoup(pageSource)
    imageTag = soup.find(id="header-img") # Get image with HTML id 'header-img'
    
    fileName = imageTag["src"].split("/")[-1] # Extract file name
    downloadPath = os.path.join(downloadFolder, fileName)

    # Download image
    output = open(downloadPath, 'w')
    output.write(urllib2.urlopen(imageTag["src"]).read())
    output.close()

except urllib2.HTTPError, e:
# For error code 429, refer to http://stackoverflow.com/questions/13213048/urllib2-http-error-429
    print "Cannot retrieve URL: HTTP Error Code", e.code
