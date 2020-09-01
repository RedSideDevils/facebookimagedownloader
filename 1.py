import requests
from bs4 import BeautifulSoup

url = input("[~]Enter URL To Post: ")
response = requests.get(url)

if response.status_code == 200:
	print("[+]Connected")
	soup = BeautifulSoup(response.text,'html.parser')
	time.sleep(1)
	image = soup.find_all('img')

	if image is not None:
		print('[+]Success')
		try: 
			load_image = requests.get(image[0]['src'])
			file = open("sample_image.png", "wb")
			file.write(response.content)
			file.close()

		except: print('[-]Something went wrong!')

	else:
		print('[-]Something went wrong')
else:
	print("[-]Can not connect")

