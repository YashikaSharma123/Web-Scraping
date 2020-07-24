
import requests #access from web browser

from bs4 import BeautifulSoup

res = requests.get('http://yahoo.com')
print(res) #ok request connected

print(res.text) #gives html code of the site

data = res.text
#print(data)
print(type(data)) #string
html  = BeautifulSoup(data,'html.parser') #source code to object code , parsing / compressing / machine readable / html code divided into parts 
print(html)  #to apply functions (converted to list)
      

 
el = html.find_all('a')#fetches letter a from html code
print(el)

#show count of a tags 
print(len(el))

b=[]

for e in el:
    print(e.getText()) #gets text from the webpage of the website

    r=e.getText()
    b.append(r)
    #print(find_all('did'))

print(b)
print("no of occurance:",b.count('Reactions'))
#for i in b :       #access contents of list
    
