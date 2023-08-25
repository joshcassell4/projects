import requests
from bs4 import BeautifulSoup
import shutil

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"}
m = requests.Session()
print('start')
for page in range(110,300):
    
    url = f"https://wallpaperswide.com/1366x768-wallpapers-r/page/{str(page+1)}"
    method = 'GET'
    print(f'getting {url}')
    x = requests.Request(method=method, \
                        url=url,\
                            headers=headers)
    h =m.send(x.prepare())

    soup = BeautifulSoup(h.text)
    print('made soup')
    print('getting links')
    alinks = soup.find_all('a')
    nextone=False
    first = True

    for y in alinks:
        if y['href']==f'/1366x768-wallpapers-r/page/{str(page)}':#.format('5'):
            nextone=False
        if nextone:
            if first:
                first=False
                print('found one:')
                print(y['href'])
            else:
                first=True
                continue
            downloadurl='https://wallpaperswide.com/download/'+y['href'][:-6]+'-1366x768.jpg'
            # pictureurl = f'https://wallpaperswide.com{y["href"]}'
            print('getting: '+downloadurl)
            r = requests.get(downloadurl, stream=True)
            if r.status_code == 200:
                with open('/home/josh/Downloads/scrapes/'+str(y['href'][1:-6])+'.jpg', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f) 
            
            # soup2 = BeautifulSoup(h.text)
            # alinks2 = soup2.find_all('a')
            # for alink2 in alinks2:
            #     print(alink2['href'])           

        if y['href']=='/rss/1366x768-wallpapers-r':
            nextone=True