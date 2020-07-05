from bs4 import BeautifulSoup as bs
import requests
from pytube import YouTube

path = 'D:\EDUCATION\django'
url = 'https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'
src= requests.get(url).text
soup=bs(src,'lxml')
# print(soup.prettify())
lst= soup.find_all('a',{'class':'pl-video-title-link'})
cnt=0
for l in lst[]:
    name=l.text.strip()
    name=f'{cnt+1}. {name}'
    print(name)
    link=l['href'].split('&')
    yt_lnk=f'https://www.youtube.com/{link[0]}'
    print(yt_lnk)
    s=YouTube(yt_lnk)
    mp4= s.streams.filter(file_extension = 'mp4',res='720p',progressive="True")
    # s.set_filename(l.text.strip())
    mp4.filename= l.text.strip()
    print(mp4)
    d_video=mp4.first()
    d_video.download(output_path=path, filename=name)
    cnt=cnt+1

