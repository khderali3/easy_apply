 
# import requests
# from bs4 import BeautifulSoup

# url = "http://localhost:3000/ar"

# response = requests.get(url)

# # Force utf-8 encoding for response text
# response.encoding = 'utf-8' 

# html = response.text

# soup = BeautifulSoup(html, "html.parser")

# for tag in soup(["script", "style"]):
#     tag.decompose()

# clean_html = soup.prettify()

# print(clean_html)




import requests
from bs4 import BeautifulSoup

url = "http://localhost:3000/ar"

response = requests.get(url)

# Force utf-8 encoding for response text
response.encoding = 'utf-8'

html = response.text

soup = BeautifulSoup(html, "html.parser")

for tag in soup(["script", "style"]):
    tag.decompose()

clean_html = soup.prettify()

# Write the output to a file with UTF-8 encoding
with open("output.html", "w", encoding="utf-8") as file:
    file.write(clean_html)

print("Cleaned HTML saved to output.html")
