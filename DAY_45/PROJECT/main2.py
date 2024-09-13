from bs4 import BeautifulSoup
import requests

# Fetch the web page
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# Parse the HTML
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Find all span tags containing the article links
span_tags = soup.find_all(name='span', class_='titleline')

article_texts = []
article_links = []

# Iterate over each span tag
for span in span_tags:
    # Find the 'a' tag within the span tag
    a_tag = span.find('a')
    if a_tag:
        article_text = a_tag.get_text()
        article_link = a_tag.get('href')
        
        article_texts.append(article_text)
        article_links.append(article_link)

# Find all the upvote scores
upvote_spans = soup.find_all(name='span', class_='score')
article_upvotes = [score.getText() for score in upvote_spans]

# for text,link,vote in zip(article_texts,article_links,article_upvotes):
#     print(text,link,vote)
#     print()

article_upvotes_int = [int(ele.split()[0])for ele in article_upvotes]
# print(article_upvotes_int)
max_ele = 0
index_ele = -1

for index,value in enumerate(article_upvotes_int):
    if value>max_ele:
        max_ele = value
        index_ele = index

print(f"Text: {article_texts[index_ele]}\nLinks: {article_links[index]},\nUpvotes:{max_ele} ")




