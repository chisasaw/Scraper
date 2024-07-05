"""Gets an image from Github profile"""
import requests
from bs4 import BeautifulSoup as bs

user_name = input("Enter github user name:" )
github_link = "https://github.com/"+user_name

r = requests.get(github_link)
soup = bs(r.content, "html.parser")

profile_image = soup.find("img")["src"]
print(profile_image)
