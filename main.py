import feedparser, datetime
 
tistory_blog_uri="https://ksko0424.tistory.com/"
feed = feedparser.parse(tistory_blog_uri+"/rss")
 
markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=250&section=header&text=Kyeongsoo%20Ko&fontColor=FFFFFF&fontSize=70&fontAlign=50)


- Name : 고경수         
- Email : star77sa@naver.com 
- Education: 전북대학교 통계학/컴퓨터공학 4학년 재학중
- Award:
  - 2022 데이터톤 경진대회 대상
  - 2022 전북대학교 통계학과 빅데이터 분석 경진대회 1회 최우수상
  - 2022 전북대학교 통계학과 빅데이터 분석 경진대회 2회 우수상
  - 2021 데이터 크리에이터 캠프 최우수상
  - 2021 성적우수 총장상

- Scholarships
  - 전북 차세대 과학인재 장학금
  - 국가우수장학(이공계)
  - 성적 우수 장학금 (2018-2, 2021-1)

- Work Experience:
  - GIST AI Lab 인턴 (2022.01 ~ 2022.02)
<!--  
- 데이터 분석 대회
  |대회|대회명|순위|상위|
  |---|-------|----|----|
  |Dacon|[구내식당 식수 인원 예측 AI 경진대회](https://github.com/star77sa/DACON-The_number_of_diners_in_the_cafeteria_Prediction)|51/481|11%|
-->
- Notion : [Notion](https://ksko.notion.site/)
- Blog : [Github Blog](https://star77sa.github.io/TIL-Blog/)<!--, [CV page](https://star77sa.github.io/)--> 
<!--
[![solved.ac tier](http://mazassumnida.wtf/api/v2/generate_badge?boj=star77sa)](https://solved.ac/star77sa)
-->

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>   <img src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=R&logoColor=white"/>
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=C%2B%2B&logoColor=white"/>
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white"/>


- 🌱 I’m currently learning `Mathematical statistics`, `Computer Vision`

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fstar77sa&count_bg=%234100EA&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=VIEW&edge_flat=false)](https://hits.seeyoufarm.com)

<!--
**star77sa/star77sa** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

""" # list of blog posts will be appended here
 
lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
