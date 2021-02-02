import requests
from bs4 import BeautifulSoup
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
pagination = indeed_soup.find("div", {"class":"pagination"})
links = pagination.find_all('a')
pages = []

for link in links[:-1]:             #[:-1] 원래 길이의 -1까지만
    pages.append(int(link.string))  # .string = Only string

max_page = pages[-1]
print(range(max_page))