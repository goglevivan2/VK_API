import csv
import time
import requests
import config
def take_1000_posts():
    token = config.token
    version='5.101'
    domain='tnull'
    count = 100
    offset = 0
    all_posts = []
    while offset < 200:
        response=requests.get("https://api.vk.com/method/wall.get",
                      params={
                          'access_token':token,
                          'v':version,
                          'domain': domain,
                          'count': count,
                          'offset':offset
                      })

        data = response.json()["response"]["items"]
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts





def file_writer(all_posts):
    with open("dev_null.csv",'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow((('likes'),('content'),('url')))
        img_url=''
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img_url =  post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow(((post['likes']['count']),(post['text']),(img_url)))


all_posts = take_1000_posts()
file_writer(all_posts)
print(1)
