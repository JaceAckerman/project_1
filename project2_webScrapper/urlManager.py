# Author: Jace Ackerman
# Date: 10/24/24
# File: urlManager.py
# Description: This file contains the UrlManager class. This class gets the urls from a text file that contains
# urls. The urls are then put into an array. The file that contains the urls for a specific version of a product
# is passed to an instance variable. Then UrlManager has a getURLS() that reads from the passed file and
# because there is one URL per line, the method reads each line and stores the line into the urlList array.
# This class allows for the URLS to be extracted from a text file.

class UrlManager:
    
    def __init__(self,fileWithProductURLS):
        self.fileWithProductURLS = fileWithProductURLS
        self.urlList = []
        
    def getURLS(self):
        with open(self.fileWithProductURLS, 'r') as file:
            for line in file:
                self.urlList.append(line)
            
