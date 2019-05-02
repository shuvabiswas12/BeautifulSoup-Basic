import requests
from fake_useragent import UserAgent

# Background on user agent

ua = UserAgent() # creating object

header = {'user-agent': ua.chrome}
page = requests.get('https://www.google.com', headers = header)
print(page.content) # return the content of that pages ...


# Background on timeout
page = requests.get('https://www.google.com', timeout = 3)
print(page)