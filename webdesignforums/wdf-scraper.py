import csv, webbrowser, sys, requests, bs4, json
from datetime import datetime

res = requests.get('http://www.webdesignforums.net/forum/members/cutler.html?tab=activitystream&type=user#activitystream')

soup = bs4.BeautifulSoup(res.text, 'html.parser') ## Making the Beautiful Soup object

scraped_info = soup.select('.forum_post .content')

## Getting array of all the threads from the website
thread_array = []
for row in scraped_info:
    ## Convert "Today" and "Yesterday" posts

    date_array = row.select('.hasavatar .datetime .date')[0].text.strip().split(',')
    date_string = date_array[0][:-2] + ',' + date_array[1]
    date_string = datetime.strptime(date_string, '%b %d, %Y').strftime('%m/%d/%Y')
    thread_array.append([row.select('.hasavatar .title')[0].text.strip(), date_string])

    ##print(thread_array[5])

## Converting Existing JSON file into a dict
with open('webdesignforums/wdf-threads.json') as f:
  old_threads = json.load(f)

## Making a list of Titles
old_thread_array = []
for thread in old_threads['Threads']:
  old_thread_array.append(thread["title"])
print(old_thread_array)

## Left ntersect the arrays



## Any leftover gets added to the JSON string

## Remake the JSON file