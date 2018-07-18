import requests
import json
url='https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response=requests.get(url)

with open('music_show.json','w+',encoding='utf-8') as f:
    f.write(response.text)
person= json.loads(response.text)
# with open('music_show.json','r',encoding='utf-8') as f:
#     person= json.load(f)

a=open('music_show.txt','w+',encoding='utf-8')
for i in range(0,len(person)):
    a.write(person[i]['title']+' ：')
    a.write(person[0]['showInfo'][0]['time']+' ~ ')
    a.write(person[0]['showInfo'][0]['endTime'])
    a.write('\n')
a.closed

# print('{0:10}'.format(person[0]['title']))