import feedparser, datetime, numpy

blog_url="https://star77sa.github.io/"
feed = feedparser.parse(blog_url+"/index.xml")
 
markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=250&section=header&text=KyeongSoo%20Ko&fontColor=FFFFFF&fontSize=70&fontAlign=50)


- Name : KyeongSoo Ko         
- Email : ksko0424@gm.gist.ac.kr 
- Education:
  - GIST M.S. in AI Graduate School
  - JBNU B.S. in Statistics & Computer Science Engineering (Double Major)

- Award:
  - Minister of Education Award, 2023 WE-MEET Project
  - 1st Award, 2022 Dataton Competition
  - 1st Award, The 1st JBNU Statistics Bigdata Analysis Competition
  - 2nd Award, The 2nd JBNU Statistics Bigdata Analysis Competition
  - 2nd Award, Data Creator Camp Hackathon
  - JBNU President's Award(2021 Academic Excellence Award)

- Scholarships
  - National Science & Technology Scholarship(2022-2023)
  - Jeonbuk Next Generation Science Talent Scholarship(2022)
  - Academic Excellence Scholarship(2018, 2021)


  
<!--
[![solved.ac tier](http://mazassumnida.wtf/api/v2/generate_badge?boj=star77sa)](https://solved.ac/star77sa)
-->

[![Notion Badge](https://img.shields.io/badge/Notion-000000?style=flat-square&title_bg=%235C5F64&logo=Notion&logo_color=%23F0F4F0&link=https://www.notion.so/ksko/Kyeongsoo-Ko-8383246d72ab463daba2b1f49f6486a1?pvs=4)](https://www.notion.so/ksko/Kyeongsoo-Ko-8383246d72ab463daba2b1f49f6486a1?pvs=4)
[![Tech Blog Badge](http://img.shields.io/badge/-Tech%20blog-black?style=flat-square&logo=github&link=https://star77sa.github.io/)](https://star77sa.github.io)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/star77sa)](https://www.linkedin.com/in/star77sa)
[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:star77sa@gmail.com)](mailto:star77sa@gmail.com)


- 🌱 I’m currently learning `Image Processing`, `Diffusion`

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
