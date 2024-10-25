# Author: Jace Ackerman
# Date: 10/24/24
# File: dataHandler.py
# Description: This file creates the DataHandler class. DataHandler is responsible for taking the raw 
# strings of reviews from the websites, cleaning the strings, and then writing the strings to a textfile.
# DataHandler utilizes the emoji package to remove any emoji's in the sting. DataHandler also utilizes the 
# replace() on the string to remove a specific object placeholder that was located in some of the removes. 
# The emojis and object place holders have numerical representations that cannot be processed, thus they have 
# get removed.

import emoji

class DataHandler:
    
    def __init__(self, fileToWrite):
        self.fileToWrite = fileToWrite
    
    #removes any emojis from review because emojis can't be processed when writing to text file
    #Also removes the character \ufffc which is an object place holder, it also cannot be processed
    def cleanString(self,string):
        string = emoji.replace_emoji(string, replace='')
        string = string.replace('\ufffc', '')
        return string
    
    #writes all the strings to self.fileToWrite that are within listOfReviews
    def saveToFile(self, listOfReviews):
        with open(self.fileToWrite, 'w') as file:
            for review in listOfReviews:
                review = self.cleanString(review)
                file.write(review + "\n")
                #file.write( + "\n")
                file.write("-" * 20 + "\n")
                
    
    
            