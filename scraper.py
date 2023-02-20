apiKey = "# USE YOUR OWN API KEY"
base = "https://youtube.googleapis.com/youtube/v3/"
maxResults = "20"

from bs4 import BeautifulSoup
import requests
import json
import re

regex = ".*v=(.*)"
with open("bb.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    links = soup.select("a[href*=watch]")
    print(links)
    for link in links:
        print("\n")
        videoId = re.search(regex,link['href']).group(1)
        #print("Searching: " + videoId)
        apiString = base + 'commentThreads?part=snippet&maxResults=' + maxResults + '&videoId=' + videoId + '&key=' + apiKey
        commentsJSON = requests.get(apiString).json()
        try:
            for commentJSON in commentsJSON['items']:
                comment = commentJSON['snippet']['topLevelComment']['snippet']['textOriginal']
                if "Old Yeller" in comment or "old yeller" in comment or "yeller" in comment:
                    print(videoId + " " + comment)
        except:
            print("Something went wrong. Skipping video.")
