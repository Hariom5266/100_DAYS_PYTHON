# Ethics
# Public API First
# Respect the Web Owner
# url/robots.txt  https://www.google.co.in/robots.txt
# Limit Your Rate

# ==================== 100 MOVIES YOU WATCH =============================== #

from bs4 import BeautifulSoup
import requests

# URL of the website to scrape
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)

# Get the website HTML content
website_html = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(website_html, 'html.parser')

# Find all <h3> tags
all_movies = soup.find_all(name="h3")
all_movies_txt = []

# Extract and print the text from each <h3> tag
for movie in all_movies:
    # all_movies_txt.append(movie.get_text())
    all_movies_txt.append(movie.getText())

print(all_movies_txt)

all_movies_txt.reverse()

with open('DAY_45/PROJECT/movies.txt','w') as file:
    for movie in all_movies_txt:
        file.write(f"{movie}\n")







