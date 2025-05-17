import requests, bs4
res = requests.get('https://nostarch.com/')
res.raise_for_status()
noSoup = bs4.BeautifulSoup(res.text, 'html.parser')  #  beautifulsoup4オブジェクトとして取り込む
#print(noSoup.select('#skip-link'))  # titleタグを取得
#elms = noSoup.select('#skip-link')  # titleタグを取得
#print(type(elms))  # タグの型を取得
#print(len(elms))  
#print(type(elms[0]))  # タグの型を取得
#print(elms[0].getText())  # タグのテキストを取得
#print(str(elms[0]))  # タグの文字列を取得
#print(elms[0].attrs)  

p_elms = noSoup.select('p')  
print(len(p_elms))  # タグの数を取得    
print(p_elms[0])
print(p_elms[42].getText())  