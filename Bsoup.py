import requests

page = requests.get("https://247ctf.com/scoreboard")
# print(page.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, "html.parser")

print(soup.text)

print(soup.title)
print(soup.title.name)x
print(soup.title.string)

print(soup.find("a"))

for line in soup.find_all("a"):
    print(line)
    print(line.get("href"))

print(soup.find(id="fetch-error"))
print(soup.find(class_="nav-link"))
print(soup.find("a",class_="nav-link"))

table = soup.find("table")
# print(table)

table_body = table.find("tbody")
rows = table_body.find_all('tr')

for row in rows:
    print("----------------------")
    # print(row)
    cols = [x.text.strip() for x in row.find_all('td')]
    print(cols)

    print(f"{cols[2]} is in {cols[0]} place with {cols[4]} points")