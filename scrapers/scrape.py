import requests
from bs4 import BeautifulSoup as bs
import jinja2 as j2

x = requests.get("http://www.google.com")

# print(x.text)
print(j2.Template("{{x.text}}").render(x=x))
