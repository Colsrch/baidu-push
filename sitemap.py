import re
import urllib
import requests

page = 'https://colsrch.cn/page-sitemap.xml'
post = 'https://colsrch.cn/post-sitemap.xml'
jxsfgz_articles = 'https://jxsfgz.club/sitemap/articles.xml'
jxsfgz_topics = 'https://jxsfgz.club/sitemap/topics.xml'

html = urllib.request.urlopen(page).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('urls-page.txt', 'w') as file:
  for data in result:
    print( data + '\n')
    file.write(data + '\n')
file.close()

html = urllib.request.urlopen(post).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('urls-post.txt', 'w') as file:
  for data in result:
    print( data + '\n')
    file.write(data + '\n')
file.close()

html = urllib.request.urlopen(jxsfgz_articles).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('jxsfgz_articles.txt', 'w') as file:
  for data in result:
    print( data + '\n')
    file.write(data + '\n')
file.close()

html = urllib.request.urlopen(jxsfgz_topics).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('jxsfgz_topics.txt', 'w') as file:
  for data in result:
    print( data + '\n')
    file.write(data + '\n')
file.close()
