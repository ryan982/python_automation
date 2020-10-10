import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import time

url = "http://indiannamesandsurnameslist.blogspot.com/p/a-to-z-modern-baby-boy-names.html"
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content, 'html.parser')
#print(soup)
table_tags = soup.find_all('td', attrs={"width" : "200"})
name = []
real_names = []
i = 0
ignored1 = ','
ignored2 = '-'
ignored3 = ' '
#print(len(name))
#print(name)

while i in range(0, len(table_tags)):
    for namey in table_tags:
        namey = table_tags[i].get_text()
        name = namey.replace("\n", "")
        if ignored1 not in name and ignored2 not in name and ignored3 not in name and name != 'NAMEMEANING':
            real_names.append(name)
        i=i+1
#for i in range()
#print(real_names)

url1 = "http://indiannamesandsurnameslist.blogspot.com/"
r1 = requests.get(url1)
content1 = r1.content
soup1 = BeautifulSoup(content1, 'html.parser')
#print(soup)
table_tags_surname = soup1.find_all('span', attrs= {"style": "font-family: Times New Roman;"})
#print(table_tags_surname)
#print(len(table_tags_surname))
j = 0
real_surnames = []
while j in range(0, len(table_tags_surname)):
    for surname in table_tags_surname:
        surname = table_tags_surname[j].get_text()
        real_surnames.append(surname)
        j = j+1
#print(real_surnames)

email = ['gmail', 'hotmail', 'protonmail', 'zohomail', 'protonmail', 'yahoo']
numbers = []
special = ['@', '#', '%', '&', '_', '-']
for number_int in range(1, 2000):
    number_str = str(number_int)
    numbers.append(number_str)
#print(numbers)

email_id = random.choice(real_names) + random.choice(real_surnames) + random.choice(numbers)+ '@' + random.choice(email)+'.com'
#print(email_id)
 
k = 0
for k in range(1,10*len(real_names)):
    name = random.choice(real_names)
    surname = random.choice(real_names)
    email_id = name + surname + random.choice(numbers)+ '@' + random.choice(email)+'.com'
    password = name[0].upper()+surname+random.choice(special)+ random.choice(numbers)
    print(email_id.lower())
    print(password)

#feeder
#p = 0
#for p in range(1, 2):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--incognito')

    #driver = webdriver.Chrome("C:\\Program Files (x86)\\chrome1\\chromedriver.exe")
    driver = webdriver.Chrome("C:\\Program Files (x86)\\chrome1\\chromedriver.exe", options = chrome_option)
    driver.get("https://www.howzat.com/signup?")

    time.sleep(3)

    #email_id
    reg_box = driver.find_element_by_xpath("//input[@placeholder = 'Email or mobile']")
    reg_box.send_keys(email_id.lower())

    #password
    reg_box = driver.find_element_by_xpath("//input[@placeholder = 'Password']")
    reg_box.send_keys(password)

    link = driver.find_element_by_class_name("button-inner")
    link.click()
    time.sleep(1)

    driver.quit()

    #link_more = driver.find_element_by_xpath("//html/body/ion-app/ng-component/ion-nav/page-lobby/ion-content/div[2]/ion-list/button[5]/img")
    #link_more.click()
    print(k)
    k = k + 1
