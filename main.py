import feedparser, datetime, numpy

blog_url="https://star77sa.github.io/"
feed = feedparser.parse(blog_url+"/index.xml")
 
markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=250&section=header&text=Kyeongsoo%20Ko&fontColor=FFFFFF&fontSize=70&fontAlign=50)


- Name : 고경수         
- Email : star77sa@gmail.com 
- Education:
  - GIST M.S. in AI Graduate School
  - JBNU B.S. in Statistics & Computer Science Engineering (Double Major)
  
- Award:
  - 2023 위밋 프로젝트 교육부 장관상
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
  - JBNU CV Lab 인턴 (2023.02 ~ 2023.08)
  - GIST AI Lab 인턴 (2022.01 ~ 2022.02)
  
<!--
[![solved.ac tier](http://mazassumnida.wtf/api/v2/generate_badge?boj=star77sa)](https://solved.ac/star77sa)
-->

[![Notion Badge](https://img.shields.io/badge/Notion-000000?style=flat-square&title_bg=%235C5F64&logo=Notion&logo_color=%23F0F4F0&link=https://www.notion.so/ksko/Kyeongsoo-Ko-8383246d72ab463daba2b1f49f6486a1?pvs=4)](https://www.notion.so/ksko/Kyeongsoo-Ko-8383246d72ab463daba2b1f49f6486a1?pvs=4)
[![Tech Blog Badge](http://img.shields.io/badge/-Tech%20blog-black?style=flat-square&logo=github&link=https://ksko0424.tistory.com/)](https://star77sa.github.io)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/%EA%B2%BD%EC%88%98-%EA%B3%A0-8b7781206/)](https://www.linkedin.com/in/%EA%B2%BD%EC%88%98-%EA%B3%A0-8b7781206/)
[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:star77sa@gmail.com)](mailto:star77sa@gmail.com)


- 🌱 I’m currently learning `Mathematical Statistics`, `Time Series Analysis`

<!--
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fstar77sa&count_bg=%234100EA&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=VIEW&edge_flat=false)](https://hits.seeyoufarm.com)
-->

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

## Recent blog posts
""" # list of blog posts will be appended here
 
random = numpy.random.randint(0, 30)

for i in feed['entries'][:7]:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %Z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])
    markdown_text += ' '*random

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
