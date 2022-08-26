from bs4 import BeautifulSoup
import requests
import csv

# getting a html document from jumia
tradingeconomics = requests.get("https://www.jumia.com.ng/?gclid=CjwKCAjwu5yYBhAjEiwAKXk_eH9BoL04WkSeXAMyNu7n5pf0hGtK2v3-NFT2DLXcTR0l1zLRiiCCcRoCdUcQAvD_BwE").text



soup = BeautifulSoup(tradingeconomics,"lxml")

# selecting a section from the document with the specific class "card -oh _fw -rad4"
section = soup.find("section" ,class_="card -oh _fw -rad4")


# selecting all img from the section 
img =section.find_all("img")
obj =[]

for val in img:
    print(val)
    obj =[*obj,val["src"]]



# we then write our list of images in a csv file 
#noe this are data urls , hence can not be use in a another browser window except from where it was created

with open('img.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["imgs"])
    for val in obj:
        writer.writerow([f"{val}"])
    




# select with BeautifulSoup
# This is the link to this lab.

# Now that you have explored some parts of BeautifulSoup, let's look how you can select DOM elements with BeautifulSoup methods.

# Once you have the soup variable (like previous labs), you can work with .select on it which is a CSS selector inside BeautifulSoup. That is, you can reach down the DOM tree just like how you will select elements with CSS. Let's look at an example:





