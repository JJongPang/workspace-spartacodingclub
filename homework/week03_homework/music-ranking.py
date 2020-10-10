import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)
client = MongoClient('localhost', 27017)
db = client.dbsparta

soup = BeautifulSoup(data.text, 'html.parser')
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for i in musics:
    musics_rank = i.select_one('td.number').text[0:2].strip()
    music_title = i.select_one('td.info > a.title.ellipsis').text.strip()
    music_artist = i.select_one('td.info > a.artist.ellipsis').text.strip()

    dic = {
        'rank': musics_rank,
        'title': music_title,
        'artist': music_artist
    }
    db.musics.insert_one(dic)







