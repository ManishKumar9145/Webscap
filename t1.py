import requests #importing requests module
from bs4 import BeautifulSoup #importing Beautiful soup module
from csv import writer #from csv importing writer

res=requests.get('https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar')   #rquest to get yhe given web page
soup=BeautifulSoup(res.content,'html.parser')   #getting html code of the given web page and contet of the same
lists=soup.find_all('div',class_="a-section a-spacing-base")  #finding all the element with div tag and class a-section a-spacing-base

with open('amazon.csv','w',encoding='utf8',newline='') as x: #to write the csv file
    thewriter = writer(x)
    header=['Name','Price','Rating'] #used to make the heding in the csv file
    thewriter.writerow(header) #writing the row of the header

    for list in lists: #finding all the elemnents from lists 
        name=list.find('span',class_="a-size-base-plus a-color-base a-text-normal").text #storing the name of product
        price=list.find('span',"a-price-whole").text #storing price of the product
        rating=list.find('span',"a-size-base").text  #storing rating of the product
        info=[name,price,rating]  #storing all the informations in the form of list
        thewriter.writerow(info) #writing all the details in the csv file
        

        
        
    
    


    





    
