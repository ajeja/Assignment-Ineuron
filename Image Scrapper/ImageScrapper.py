from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time


# taking user input
print("What do you want to download?")
download = input()
n = input("How many images to be downloaded")
site = 'https://www.google.com/search?tbm=isch&q=' + download
print(site)
# providing driver path
driver = webdriver.Firefox(executable_path="C:\driver chrome\geckodriver.exe")

# passing site url
driver.get(site)



i = 0

while i < 2:
    # for scrolling page
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    try:
        # for clicking show more results button
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(5)
    i += 1

# parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')

# closing web browser
driver.close()

# scraping image urls with the help of image tag and class used for images
img_tags = soup.find_all("img", class_="rg_i")

count = 0
for i in img_tags:
    # print(i['src'])
    try:
        if count<n:
            # passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], "image" +str(count) + ".jpg")
            count += 1
            print("Number of images downloaded = " + str(count), end='\r')

    except Exception as e:
        count += 1



#REFERENCE YOUTUBE Link is https://youtu.be/Dfp2kqzgImw
# https://youtu.be/cImRC-AZs48