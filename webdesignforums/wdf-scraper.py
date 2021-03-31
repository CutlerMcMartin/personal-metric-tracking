import csv, webbrowser, sys, requests, bs4, re

res = requests.get('http://www.webdesignforums.net/forum/members/cutler.html?tab=activitystream&type=user#activitystream')

soup = bs4.BeautifulSoup(res.text, 'html.parser') ## Making the Beautiful Soup object

scraped_info = soup.select('.forum_post .content')

thread_array = []
for row in scraped_info:
    date_array = row.select('.hasavatar .datetime .date')[0].text.strip().split(',')
    date_string = date_array[0][:-2] + ',' + date_array[1]
    thread_array.append([row.select('.hasavatar .title')[0].text.strip(), date_string])

print(thread_array[5])