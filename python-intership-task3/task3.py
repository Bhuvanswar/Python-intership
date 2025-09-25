import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com"  
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the page")
else:
    print(f"Failed to retrieve page. HTTP Status Code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

headlines = soup.find_all(['h1', 'h2', 'h3'])  

with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, 1):
        text = headline.get_text(strip=True)  
        if text: 
            file.write(f"{i}. {text}\n")

print("Headlines have been saved to headlines.txt")
