import requests
import re

url = 'http://www.gutenberg.org/files/2638/2638-0.txt'
text = requests.get(url).text

start = re.search(r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK THE IDIOT \*\*\*', text).end()
print(start)
end = re.search(r'II\.', text).start()
print(end)
print(text[start:end])
