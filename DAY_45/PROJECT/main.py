from bs4 import *
# import lxml

with open('DAY_45/PROJECT/my_website.html', encoding='utf-8') as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.a)
# print(soup.p)

# Searching in html files

all_ancher_tags=soup.find_all(name='a')
# print(all_ancher_tags)

for tag in  all_ancher_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name='h1',id='name')    
print(heading)

section_heading = soup.find(name='h3',class_='heading')
print(section_heading)

comapany_url = soup.select_one(selector='p a')
print(comapany_url)

headings = soup.select('.heading')
print(headings)



