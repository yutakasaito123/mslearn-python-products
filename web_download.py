
import requests


res = requests.get('https://api.github.com/events')
#print(res.text[:100])

try:
    res.raise_for_status()
    play_file = open('playfile.txt', 'wb')
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
    play_file.close()
except Exception as exc:
    print('There was a problem: {}'.format(exc))
    exit(1) 




