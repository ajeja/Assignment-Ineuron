from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

search = input('Enter the search term')
url = 'https://www.flipkart.com/search?q='+search
# url ='https://www.flipkart.com/search?q=iphone'
print(url)

uClient = uReq(url)
page = uClient.read()
uClient.close()

page_h =soup(page,'html.parser')
page_hp = soup.prettify(page_h)
# print(page_hp)
artics = page_h.findAll("div", {"class": "_2pi5LC col-12-12"})

# artic =artics[0]
print("Length" ,len(artics))
# artic = soup.prettify(artics[6])
NAME= []; RATING =[]; PRICE =[]; LINK = []
for i in range(len(artics)):
    try:
        try:
            artic = artics[i]
            name =  artic.div.div.img["alt"]
            NAME.append(name)
            # print(name)
        except:
            name = 'null'
            NAME.append(name)
        try:
            price = artic.findAll("div", {"class": "col col-5-12 nlI3QM"})
            Price = (price[0].text)
            # print(Price[0:7])
            PRICE.append(Price[0:7])
        except:
            Price = 'null'
            PRICE.append(Price)
        try:
            rating = artic.findAll("div", {"class": "_3LWZlK"})
            # print(rating[0].text)
            RATING.append(rating[0].text)
        except:
            rating = 'null'
            RATING.append(rating)
            # articsp = soup.prettify(artics[6])
            # print(articsp)
        try:
            pdturl = artic.div.div.div.a['href']
            pdturlf = "https://www.flipkart.com" + pdturl
            # print(pdturlf)
            LINK.append(pdturlf)
        except:
            pdturlf = 'null'
            RATING.append(pdturlf)
            # print("An error occured")
    except:
        print("An error occured")

countnam = NAME.count('null')
for i in range(1,countnam+1):
    NAME.remove('null')


countrat = RATING.count('null')
for i in range(1,countrat+1):
    RATING.remove('null')

countpri = PRICE.count('null')
for i in range(1,countpri+1):
    PRICE.remove('null')

diff = [len(NAME),len(RATING),len(PRICE)]
diffi =["NAME","RATING","PRICE"]
# print(min(diff))
maxval =max(diff)
maxval_pos = []
for i in range(len(diff)):
    if diff[i] == maxval:
        maxval_pos.append(i)
# print(maxval_pos)
if len(maxval_pos)==1:
    diff1 = sorted(diff)
    for i in range(len(diff1)-1):
        red = diff1[i+1]-diff1[0]
        if red >>0:
            # print(red)
            for j in range(1,red+1,1):
                print(j)
                ind = diffi[diff.index(diff1[i+1])]
                # print(ind)
                vars()[ind].pop(0)
                print(vars()[ind])
k=0;
if len(maxval_pos)!=1:
    diff1 = sorted(diff)
    for i in range(len(diff1)-1):
        red = diff1[i+1]-diff1[0]
        if red >>0:
            # print(red)
            for j in range(1,red+1,1):
                print(j)
                ind = diffi[maxval_pos[k]]
                # print(ind)
                vars()[ind].pop(0)
                print(vars()[ind])
        k=k+1;



Dict = {"Name":NAME,"Rating":RATING,"Price":PRICE}
# print(Dict)
Dictp =pd.DataFrame(Dict)
print(Dictp)


prefer = int(input("Enter the Product no you need further details"))
print(prefer)
prefer_pdt_url = LINK[prefer]
print(prefer_pdt_url)

uClient = uReq(prefer_pdt_url)
pdt_page = uClient.read()
uClient.close()

pdt_page_h =soup(pdt_page,'html.parser')
page_hp = soup.prettify(page_h)
# print(page_hp)
review = pdt_page_h.findAll("div", {"class": "t-ZTKy"})
print(len(review))
REVIEW=[]
PDTRATING =[]
USER = []
REVIEW_TITLE = []
for i in range(len(review)):
    try:
        REVIEW.append(review[i].text)
        # print(REVIEW)
    except:
        REVIEW.append("null")
    try:
        pdt_rating = pdt_page_h.findAll("div", {"class": "_3LWZlK _1BLPMq"})
        PDTRATING.append(pdt_rating[i].text)
        # print(PDTRATING)
    except:
        rating = 'null'
        PDTRATING.append(rating)



    try:
        user_name = pdt_page_h.findAll("div", {"class": "row"})
        user_name = pdt_page_h.findAll('p')
        # print(len(user_name))
        # print(user_name)
        User = user_name[2].text
        Review_Title = user_name[1].text
        USER.append(User)
        REVIEW_TITLE.append(Review_Title)
    except:
        USER.append("null")
        REVIEW_TITLE.append("null")
        # print(user_name)
        # print(USER)
        # print(REVIEW_TITLE)


Dict1 = {"_id": NAME[prefer],"Product Rating":PDTRATING,"Review":REVIEW}

Dict1p =pd.DataFrame(Dict1)
print(Dict1p)



import pymongo

DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
DB_NAME = "REVIEW"

# Establish a connection with mongoDB
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

# Create a DB
dataBase = client[DB_NAME]

COLLECTION_NAME = "Mobile"
collection = dataBase[COLLECTION_NAME]

collection.insert_one(Dict1)