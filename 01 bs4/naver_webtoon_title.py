from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#월요웹툰영역 추출하기
data1=soup.findAll('div',{'class':'col_inner'})

week_title_list = [t.text for t in data1]
pprint(week_title_list)

# pprint(len(data1_list))

# data2 = data1.findAll('a', {'class':'title'})
# # pprint(data2)

# # 텍스트만 추출
# # title_list = []
# # for t in data2:
# #     title_list.append(t.text)

# title_list = [t.text for t in data2]

# pprint(title_list)

# 전체 웹툰 영역 추출하기
data1_list=soup.findAll('div',{'class':'col_inner'})
pprint(len(data1_list))

# 전체 웹툰 리스트
week_title_list = []

for data1 in data1_list:
    data2 = data1.findAll('a', {'class':'title'})
    title_list = [t.text for t in data2]
    # pprint(title_list)

    # week_title_list.append(title_list)
    week_title_list.extend(title_list)
pprint(week_title_list)
