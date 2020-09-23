import csv
import bs4 as bs
from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

reg_url = 'https://www.boxofficemojo.com/year/world/?sort=worldwideGrossToDate&ref_=bo_ydw__resort#table'
req = Request(url = reg_url,headers = headers)
source1 = urlopen(req).read()
soup = bs.BeautifulSoup(source1,'html.parser')

csv_file = open('Movie Rank List Worldwide.csv','w',encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank','Name','Worldwide Collection','Movie Link'])

i=0
for movies in soup.find('table',class_="mojo-body-table"):
    i +=1
    if(i<=1):
        continue
    for individual_movie_rank in movies.find_all('td',class_="mojo-field-type-rank"):
        print(individual_movie_rank.text,end=" ")
    for individual_movie_name in movies.find_all('td',class_="mojo-field-type-release_group"):
        print(individual_movie_name.text,end = " ")
    for individual_movie_worldwide in movies.find('td',class_="mojo-field-type-money"):
        print(individual_movie_worldwide,end=" ")
    for movie_links in movies.find_all('a',class_="a-link-normal"):
        link = movie_links.get('href')
        link = "https://www.boxofficemojo.com"+link
        print(link)

    csv_writer.writerow([individual_movie_rank.text,individual_movie_name.text,individual_movie_worldwide,link])

csv_file.close()