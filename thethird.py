import requests

url = 'https://www.python.org/'
response = requests.get(url)
html = response.text

counter = {}
for char in html:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

for char, count in counter.items():
    print(f"{char}: {count}")

with open('readme.md', 'w') as f:
    f.write('Result:\n\n')
    for char, count in counter.items():
        f.write(f"{char}: {count}\n")