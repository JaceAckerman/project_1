# Author: Jace Ackerman
# Date: 10/24/24
# File: parser.py
# Description: This file contains the Parser class. Parser utilizes the BeautifulSoap package. This package
#  is how the response from Scraper gets processed. The setSoup() allows for the Parser's soup variable to be
# changed. The getReviews() uses find_all() to extract all the review blocks and find() to get the reviews
# themselves. Some reviews only had a title, so if this is the case the title is then used as the review.
# All of the reviews are stored in the reviews array.

from bs4 import BeautifulSoup

class Parser:
    
    #Parser has two variables, soup and a review array.
    def __init__(self):
        #takes the Response object and puts it in soup so it's in a structured format.
        self.soup = "None"
        self.reviews = []
    
    #set the soup value by passing a response from Scraper's GET request
    def setSoup(self, responseFromScrape):
            self.soup = BeautifulSoup(responseFromScrape, 'html.parser')
    
                
    def getReviews(self):
        #gets all of the review bodies in the html document
        reviewsFromHTML = self.soup.find_all('div', class_='ebay-review-section-r') 
        
        #gets each review from the people who left a review for a product on eBay
        for review in reviewsFromHTML:
            # Get the review text, if no review then uses the title as the review.
            if review.find('p', class_='review-item-content') == None:
                userReview = review.find('h3', class_='review-item-title').text.strip()  
            else:
                userReview = review.find('p', class_='review-item-content').text.strip() 
                
            self.reviews.append(userReview)
            
         
            

            
        
