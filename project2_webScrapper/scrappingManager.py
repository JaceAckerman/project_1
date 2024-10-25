# Author: Jace Ackerman
# Date: 10/24/24
# File: urlManager.py
# Description: This file contains the ScrapingManager class. This class is responsible for integrating all the
# other classes. ScrapingManager just needs the url file and the file name that is going to have all the reviews
# written to passed into the constructor method. Then ScrapingManager uses all the other objects to get the 
# reviews in getReviewsForProducts. The result of calling getReviewsForProducts is all the reviews for that
# product will be written to fileToWrite.

from scraper import Scraper
from parser import Parser
from urlManager import UrlManager
from dataHandler import DataHandler

class ScrapingManager:
    
    #Creates a scraper, parser, urlManager, and dataHandler object. It passes the urlFile to the urlManager 
    # object and then passes fileToWrite to the dataHandler object.
    def __init__(self, urlFile, fileToWrite):
        self.scraper = Scraper()
        self.parser = Parser()
        self.urlManager = UrlManager(urlFile)
        self.dataHandler = DataHandler(fileToWrite)
        
    def getReviewsForProduct(self):
        self.urlManager.getURLS()
        for url in self.urlManager.urlList:
            #set url value in scraper and scrape url
            self.scraper.setURL(url)
            response = self.scraper.scrape()
            
            #set the value for soup and then get the reviews users wrote from soup
            self.parser.setSoup(response)
            self.parser.getReviews()
        
        #write the data to the output file
        self.dataHandler.saveToFile(self.parser.reviews)
            
            
            
            
        