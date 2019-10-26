import urllib.request
from bs4 import BeautifulSoup 

#-------------We used emag page------------------#


### 1.Marina Morosanu

laptop_Apple = 'https://www.emag.ro/laptop-apple-macbook-air-13-cu-procesor-intelr-dual-coretm-i5-1-80ghz-13-3-8gb-128gb-ssd-intelr-hd-graphics-6000-int-kb-silver-mqd32ze-a/pd/DLXM4KBBM/'
apple = urllib.request.urlopen(laptop_Apple) 
print(apple)

soup = BeautifulSoup(apple, 'html.parser') 
print(soup)

apple_name = soup.find('h1', attrs={'class':'page-title'}) 
print(apple_name)
apple_name = apple_name.text.strip()

apple_price = soup.find('p', attrs={'class': 'product-new-price'}) 
print(apple_price)
apple_price = apple_price.text.strip()
print(apple_price)

apple_description = soup.find('div', attrs={'class': 'product-page-description-text'}) 
print(apple_description)
apple_description = apple_description.text.strip()
print(apple_description)

apple_specications = soup.find('table', attrs={'class': 'table table-striped product-page-specifications'}) 
print(apple_specications)
apple_specications = apple_specications.text.strip()
print(apple_specications)

apple_reviews = soup.find('small', attrs={'class':'hidden-xs'}) 
print(apple_reviews)
apple_reviews = apple_reviews.text.strip()




#### 2.) Catalina Nicorescu

laptop_gaming_page = 'https://www.emag.ro/laptop-gaming-asus-tuf-fx504gd-cu-procesor-intelr-coretm-i7-8750h-pana-la-4-10-ghz-coffee-lake-15-6-full-hd-8gb-1tb-nvidiar-geforcer-gtx-1050-4gb-free-dos-black-fx504gd-e4075/pd/D703CFBBM/?ref='
gaming = urllib.request.urlopen(laptop_gaming_page) 
print(gaming)

soup = BeautifulSoup(gaming, 'html.parser') 
print(soup)

name_laptop = soup.find('h1', attrs={'class':'page-title'}) 
print(name_laptop)
name_laptop = name_laptop.text.strip()

price_laptop = soup.find('p', attrs={'class':'product-new-price'}) 
print(price_laptop)
price_laptop = price_laptop.text.strip()

description_laptop = soup.find('div', attrs={'id':'description-body'}) 
print(description_laptop)
description_laptop = description_laptop.text.strip()

specifications_laptop = soup.find('div', attrs={'class':'col-md-12'}) 
print(specifications_laptop)
specifications_laptop = specifications_laptop.text.strip()

reviews_laptop = soup.find('small', attrs={'class':'hidden-xs'}) 
print(reviews_laptop)
reviews_laptop = reviews_laptop.text.strip()


#### 2.) Bogdan Donu

laptop_asus_page = 'https://www.emag.ro/laptop-asus-cu-procesor-intelr-coretm-i5-6300hq-2-30ghz-skylaketm-15-6-4gb-1tb-dvd-rw-nvidiar-geforcer-gtx-950m-2gb-free-dos-silver-x550vx-xx015d/pd/D8RLV3BBM/'
asus = urllib.request.urlopen(laptop_asus_page) 
print(asus)

soup = BeautifulSoup(asus, 'html.parser') 
print(soup)

asus_name = soup.find('h1', attrs={'class':'page-title'}) 
print(asus_name)
asus_name = asus_name.text.strip()

asus_price = soup.find('p', attrs={'class':'product-new-price'}) 
print(asus_price)
asus_price = asus_price.text.strip()

asus_description = soup.find('div', attrs={'id':'description-body'}) 
print(asus_description)
asus_description = asus_description.text.strip()

asus_specifications = soup.find('div', attrs={'class':'col-md-12'}) 
print(asus_specifications)
asus_specifications = asus_specifications.text.strip()

asus_reviews = soup.find('small', attrs={'class':'hidden-xs'}) 
print(asus_reviews)
asus_reviews = asus_reviews.text.strip()



import csv 
from datetime import datetime 

with open('emag.csv', 'a', newline='') as csv_file: 
    fieldnames = ['name', 'price', 'description', 'specifications', 'reviews', datetime.now()]
    thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
    thewriter.writeheader()
    thewriter.writerow({'name' : 'Laptop Gaming ASUS TUF FX504GD cu procesor Intel® Core™ i7-8750H pana la 4.10 GHz, Coffee Lake, 15.6", Full HD, 8GB, 1TB, nVIDIA® GeForce®  GTX 1050 4GB, Free DOS, Black', 'price' : '4.10700 Lei', 'description' : 'ASUS TUF Gaming FX504 este un laptop puternic ce combina o experienta foarte imersiva in segmentul jocurilor cu o durata de viata ce depaseste cu mult standardele in acest segment. Sistemul patentat de Racire Anti-Praf (Anti-Dust Cooling - ADC) asigura longevitatea si stabilitatea performantelor, in timp ce afisajul extraordinar si sistemul sonor surround pe 7.1 canale va vor pune la incercare toate simturile — FX504 bifeaza totate cerintele voastre, si la un pret accesibil!', 'specifications' : 'Procesor: Producator procesor:Intel®, Tip procesor:i7', 'reviews' : '82 de review-uri'})
    thewriter.writerow({'name' : 'Laptop Apple MacBook Air 13 cu procesor Intel® Dual Core™ i5 1.80GHz, 13.3", 8GB, 128GB SSD, Intel® HD Graphics 6000, INT KB, Silver', 'price' : '4.19999 Lei', 'description' : 'MacBook Air de 11 inchi are o autonomie de pana la 9 ore intre incarcari, iar modelul de 13 inchi are o autonomie incredibila, de pana la 12 ore. Asa ca poti sa lucrezi de dimineata pana seara fara sa-l mai incarci. Daca vrei sa te relaxezi, ai la dispozitie pana la 10 ore de redare de filme iTunes pe modelul de 11 inchi si pana la 12 ore pe modelul de 13 inchi. Datorita modului standby de 30 de zile, poti sa pleci pentru cateva saptamani si apoi sa reiei totul de unde ai ramas.', 'specifications' : 'Producator procesor: Intel®, Tip procesor:i5', 'reviews' : '63 de review-uri'})
    thewriter.writerow({'name' : 'Laptop ASUS X550VX-XX015D cu procesor Intel® Core™ i5-6300HQ 2.30GHz, Skylake™, 15.6", 4GB, 1TB, DVD-RW, nVIDIA® GeForce® GTX 950M 2GB, Free DOS, Silver', 'price' : '3.19901 Lei', 'description' : 'Proiectat pentru multitasking si divertisment, laptopul Asus X550VX din seria X este un notebook practic pentru toti utilizatorii. Cu un design elegant, avand un finisaj in cercuri concentrice, seria X adauga o nota de rafinament si eleganta.', 'specifications' : 'Procesor: Producator procesor:Intel®, Tip procesor:i5', 'reviews' : '62 de review-uri'})