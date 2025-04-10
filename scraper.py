import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com/jobs"  # replace with a real job board URL
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for job_elem in soup.select(".job-post"):  # adapt selectors to actual site
    title = job_elem.select_one(".title").get_text(strip=True)
    company = job_elem.select_one(".company").get_text(strip=True)
    link = job_elem.select_one("a")["href"]
    jobs.append({"title": title, "company": company, "link": link})

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "company", "link"])
    writer.writeheader()
    writer.writerows(jobs)

print(f"Saved {len(jobs)} job listings to jobs.csv")
