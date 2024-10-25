# Author: Jace Ackerman
# Date: 10/24/24
# File: scraper.py
# Description: This file contains the Scraper class. Scraper has a variable called url, which represents
# the current url that the user wants to scrape from. Scraper has a setURL() which changes the url variable to 
# the passed string in setURL(). Scraper utilizes the request package. It makes a GET request and if there is
# an error, it will be caught. Otherwise, scrape() returns the response from the GET request in the form of 
# text.

import requests

class Scraper:
    
    def __init__(self):
        self.url = "Not Assigned Yet"
     
    #Returns the value of the resposne from the get method from the requests library if valid
    #otherwise it raises an exception    
    def scrape(self):
        try:
            scrapedData = requests.get(self.url)
            scrapedData.raise_for_status()
            #return the data as text
            return scrapedData.text
        except requests.RequestException as e:
            print(e)
            return None
    
    def setURL(self, url):
        self.url = url
