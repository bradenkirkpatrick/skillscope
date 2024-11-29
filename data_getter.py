
import requests
from bs4 import BeautifulSoup
# 100 miles from allentown,pa "software engineer" job search on indeed
url = 'https://www.indeed.com/jobs?q=software+engineer&l=Allentown%2C+PA&radius=100&vjk=d22626c2367cb366'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
bodies = soup.findAll("li", class_="css-1ac2h1w eu4oa1w0")
for body in bodies:
    print(body.text)
print(len(bodies))