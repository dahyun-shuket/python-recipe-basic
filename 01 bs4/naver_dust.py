from bs4 import BeautifulSoup as bs
from pprint import pp, pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text, 'html.parser')
# pprint(soup)

data1 = soup.find('div', {'class':'status_wrap'}) # 영역 추출
# pprint(data1)

data2 = data1.findAll('dl', {'class':'summary_list'})
# pprint(data2[0])

# data2 = data1.findAll('dd')
# pprint(data2[0])

find_dust = data2[0].find('dd', {'class':'desc'}).text
pprint(find_dust)
