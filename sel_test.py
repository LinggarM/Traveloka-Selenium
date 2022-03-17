from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options= chrome_options)
link = "https://m.traveloka.com/id-id/hotel/indonesia/hotel-ciputra-semarang-managed-by-swiss-belhotel-international--62307"
link2 = "https://m.traveloka.com/id-id/hotel/indonesia/oyo-231-hotel-andita-syariah-near-rsu-katholik-surabaya-kota-surabaya-3000010004935"
link3 = "https://m.traveloka.com/id-id/hotel/indonesia/hotel-asri-banjarnegara-3000020009544"
driver.get(link3)

# semua ulasan
nxt = driver.find_element(By.XPATH,'//div[@class="_1uXCv"]')
element = driver.find_element(By.XPATH,'//div[@class="_3uVKw"]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
nxt.click()

# bahasa
bahasa = driver.find_elements(By.XPATH,'//div[@class="_2TzAV _2qq6s _2WrKe"]')[1]
tenger = driver.find_element(By.XPATH,'//div[@class="Ck-bZ"]')
tenger.location_once_scrolled_into_view
bahasa.click()
time.sleep(2)
bahasaIndonesia = driver.find_element(By.XPATH,'//span[text()="Bahasa Indonesia"]').click()

# init data
data = []

# open review (n halaman x 10 review)
n = 20 # jumlah halaman
nxt2 = driver.find_element(By.XPATH,'//div[@class="_1hiwh"]')
for i in range(n):
	time.sleep(2)
	nxt2.location_once_scrolled_into_view
	nxt2.click()

# parse html
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
divs = soup.find_all("div", "css-901oao r-1sixt3s r-1b43r93 r-majxgm r-rjixqe r-fdjqy7")

# get data
for div in divs:
	try :
		if ((len(div.string) > 20) and (not div.string.startswith("Kepada "))) :
			data.append(div.string)
	except :
		print("Bukan teks!")

# save file
with open("reviews_data.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	for item in data :
		writer.writerow([item])

driver.close()