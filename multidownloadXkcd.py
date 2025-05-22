import requests, os,bs4,threading
os.makedirs('xkcd', exist_ok=True)



def download_xkcd(start_comic, end_comic): 
    for url_number in range(start_comic, end_comic):
        print('Downloading page https://xkcd.com/{}...'.format(url_number))
        res = requests.get('https://xkcd.com/{}'.format(url_number))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = 'https:' + comic_elem[0].get('src')
            print('Downloading image {}...'.format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
            image_file.close


donwlaod_threads = []
for i in range(1, 1400, 100):
    donwlaod_thread = threading.Thread(target=download_xkcd, args=(i, i+100))
    donwlaod_threads.append(donwlaod_thread)
    donwlaod_thread.start()
