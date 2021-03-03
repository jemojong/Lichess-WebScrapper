from bs4 import BeautifulSoup
import requests

handles=['blackrebel256','Rick_andMorty','marasmus01','wanyaland','kirekachesschamp','harunov','Magufuli','UGgm_Manuel256','my_crush','IwantAnIphone','mandiallabenj']
results=[]

for handle in handles:
    source=requests.get(f'https://lichess.org/@/{handle}').text
    soup = BeautifulSoup(source,'html5lib')
    #player_name = soup.find('span',class_ = 'offline user-link')['data-href'][3:]
    bullet_rating= soup.find('a',title = 'Very fast games: less than 3 minutes').span.rating.strong.text
    blitz_rating = soup.find('a',title = 'Fast games: 3 to 8 minutes').span.rating.strong.text

    results.append(
        {
            'Handle':handle,
            'Bullet rating': bullet_rating,
            'Blitz rating':blitz_rating
        }
    )
    results.sort(key=lambda result: result['Blitz rating'],reverse=True)

for result in results:
    for key,value in result.items():
        print(f'{key}:{value}')
    print()

