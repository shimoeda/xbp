#歌詞の習得テキスト化
import requests
from bs4 import BeautifulSoup
 
print("歌手名入力")
band = input()
print("歌名入力")
song = input()
 
def main():
    # URL の指定
    url = "https://utaten.com/lyric/" +str(band) + "/"+str(song)
    # ページの取得
    html = requests.get(url).text
    # HTML の保存
    with open("config.html", mode="w", encoding="utf-8") as file:
        file.write(html)
 
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", class_="contentsBox movie_box")
 
    # タイトルの取得
    span = article.find("span", class_="movieTtl_mainTxt")
    title = span.text[1:-1]
 
    # 作者の取得
    dl = soup.find("dl", class_="lyricWork")
    dds = dl.find_all("dd")
    lyricist = dds[0].text
    composer = dds[1].text
 
    # 歌詞の取得
    div = soup.find("div", class_="hiragana")
    div.find("span", class_="rt").extract()
 
    print(title)
    #print(lyricist, composer)
    print(div.get_text())
    
    #書き込み用ファイルの生成
    path_w = "kashi.txt"
 
    s = div.get_text()
 
    with open(path_w, mode='a') as f:
        f.write(s)
 
if __name__ == '__main__':
    main()
import requests
from bs4 import BeautifulSoup
print("歌手名入力")
band = input()
print("歌名入力")
song = input()
def main():
    # URL の指定
    url = "https://utaten.com/lyric/" +str(band) + "/"+str(song)
    # ページの取得
    html = requests.get(url).text
    # HTML の保存
    with open("config.html", mode="w", encoding="utf-8") as file:
        file.write(html)
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", class_="contentsBox movie_box")
u # タイトルの取得
span = article.find("span", class_="movieTtl_mainTxt")
title = span.text[1:-1]
 
    # 作者の取得
dl = soup.find("dl", class_="lyricWork")
dds = dl.find_all("dd")
lyricist = dds[0].text
composer = dds[1].text
 
    # 歌詞の取得
div = soup.find("div", class_="hiragana")
div.find("span", class_="rt").extract()
 
print(title)
print(lyricist, composer)
print(div.get_text())
 