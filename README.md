# Web-Scraping   
                          

#### Web Scraping, Web Data Extraction technique used to extract large amounts of data from "yahoo.com" website page whereby the data extracte and saved to a local file or to a database in table (spreadsheet) format.

### Extracting data from **" yahoo.com "** main page :

Use the API of the website (if it exists). For example, Yahoo has the Yahoo Graph API which allows retrieval of data posted on **"yahoo page"**.
Access the HTML of the webpage and extract useful information/data from it. This technique is called web scraping or web harvesting or web data extraction.

### Steps involved in web scraping :

1. Send an HTTP request to the URL of the webpage you want to access. The server responds to the request by returning the HTML content of the webpage. For this task, we will use a third-party HTTP library for python-requests.
2. Once we have accessed the HTML content, we are left with the task of parsing the data. Since most of the HTML data is nested, we cannot extract data simply through string processing. One needs a parser which can create a nested/tree structure of the HTML data. There are many HTML parser libraries available but the most advanced one is html5lib.
3. Now, all we need to do is navigating and searching the parse tree that we created, i.e. tree traversal. For this task, we will be using another third-party python library, Beautiful Soup. It is a Python library for pulling data out of HTML and XML files.


![alt text](https://github.com/YashikaSharma123/Web-Scraping/blob/master/Img1.png)

**Note :** Web Scraping is considered as illegal in many cases. It may also cause your IP to be blocked permanently by a website.
