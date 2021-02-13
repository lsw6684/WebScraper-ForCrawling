import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True) # before the last one
    return int(last_page)               # beautifulSoup이 알아서 공백 제거


def extract_job(html):
    title = html.find("h2", {"class":"mb4"}).find("a")["title"]
    company, location=html.find("h3",{"class" : "mb4"}).find_all("span", recursive=False)
    print(company.get_text(strip=True), location.get_text(strip=True))
    return{'title' : title}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):    # range는 integer를 사용
        result = requests.get(f"{URL}pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs