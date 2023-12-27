from bs4 import BeautifulSoup
import requests

#BeatifulSoup Docs - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# with open("website.html") as file:
#     contents = file.read()
#print(contents)

# soup = BeautifulSoup(contents, 'html.parser')
# #<title>Angela's Personal Site</title>
# print(soup.title)
# #title
# print(soup.title.name)
# #Angela's Personal Site
# print(soup.title.string)

#Prints the first element that matches.
# print(soup.a)
# print(soup.li)

#Above only returns the first element, but if you want to see all the elements of a type use .find_all() - returns a list
# print(soup.find_all(name='a'))
# print(soup.find_all(name='p'))

# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
#print(heading)

# section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)

#Find an anchor tag inside of an paragraph tag by using select_one (find first one)
# company_url = soup.select_one(selector="p a")
# print(company_url)

#Find by id selector (first one)
# name = soup.select_one(selector="#name")
# print(name)

#Find by class selector (find all)
# heading = soup.select(selector=".heading")
# print(heading)

response = requests.get("https://news.ycombinator.com/news")
#print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# article_tag = soup.find(name="a", rel="noreferrer")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_link)
# print(article_upvote)

articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)



article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvotes = max(article_upvotes)
max_votes_index = article_upvotes.index(max_upvotes)
max_text = article_texts[max_votes_index]
max_link = article_links[max_votes_index]

print(f"The article with the most upvotes ({max_upvotes}) is '{max_text}' - {max_link}")



