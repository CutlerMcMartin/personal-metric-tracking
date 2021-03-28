import csv, webbrowser, sys, requests, bs4, re

res = requests.get('http://www.webdesignforums.net/forum/members/cutler.html?tab=activitystream&type=user#activitystream')

soup = bs4.BeautifulSoup(res.text, 'html.parser') ## Making the Beautiful Soup object

scraped_info = soup.select('.forum_post .content')

data_array = []
for row in scraped_info:
    date_string = row.select('.hasavatar .datetime .date')[0].text.strip().split('\xa0')[0][:-1]
    data_array.append([row.select('.hasavatar .title')[0].text.strip(), date_string])

print(data_array[5])