import requests #http requests
from bs4 import BeautifulSoup #web scraping



import datetime

now=datetime.datetime.now()



page= requests.get("https://www.skroutz.gr/c/1413/playstation_4_games.html")
soup=BeautifulSoup(page.content,"html.parser")
games=[]

for game in soup.find_all("a",attrs={"class":"js-sku-link"}):
    if game.text !="":
        games.append(game.text)


for i in range(1, len(games),2):
    games[i]= games[i][3:8]
date=str(now.day)  +"_"+ str(now.hour)+ "_"+ str(now.minute) 
f=open( f"{date}_games.txt","w+")
f.write(date + "\n")
for i in range(0,len(games),2):
    f.writelines(f'game : {games[i]} - price : {games[i+1]} \n')
f.close()
