# Author: Jace Ackerman
# Date: 11/25/24
# File: performAnalysis.py
# Description: This file contains the PerformAnalysis class. This class will integrate all the modules made for 
# project 3. So, phi3Interface.py, promptManager.py, graph.py, responseHandler.py, and sentimentAnalysis.py will 
# all be used in this class. Note that sentimentAnalysis.py alread integrated phi3Interface, promptManager, and 
# responseHandler. PerformAnalysis's function is to perform a sentiment analysis on reviews using phi3. Then graph
# the data generated using graph.py. This will be done using the 5 Apple Watch Products.

from sentimentAnalysis import SentimentAnalysis
from graph import Graph
class PerformAnalysis:
    def __init__(self):
        self.series5Analysis = SentimentAnalysis("series5Reviews.txt", "series5Responses.txt", "series5Prompt.txt")
        self.series6Analysis = SentimentAnalysis("series6Reviews.txt", "series6Responses.txt", "series6Prompt.txt")
        self.series7Analysis = SentimentAnalysis("series7Reviews.txt", "series7Responses.txt", "series7Prompt.txt")
        self.series8Analysis = SentimentAnalysis("series8Reviews.txt", "series8Responses.txt", "series8Prompt.txt")
        self.series9Analysis = SentimentAnalysis("series9Reviews.txt", "series9Responses.txt", "series9Prompt.txt")
        
        self.sentimentGraph = Graph()
        self.products = [self.series5Analysis, self.series6Analysis, self.series7Analysis, self.series8Analysis, self.series9Analysis]
        
    # Counts the responses for each product
    def getCountOfResponses(self):
        self.series5Analysis.countResponses()
        self.series6Analysis.countResponses()
        self.series7Analysis.countResponses()
        self.series8Analysis.countResponses()
        self.series9Analysis.countResponses()
        
    #Gets the sentiment for each product from phi3 interface
    def doAnalysis(self):
        self.series5Analysis.analyze()
        self.series6Analysis.analyze()
        self.series7Analysis.analyze()
        self.series8Analysis.analyze()
        self.series9Analysis.analyze()
    
    # This method will fill in the data arrays for each of the sentimentGraph objects. Index 0 in all the arrays will correspond
    # to the totals for the first product, and Index 1 will correspond to the totals for the second product.
    # Indices 3,4,5 will correspond to the third, fourth, and fifth products as well.
    def fillDataArraysForGraph(self):
        self.getCountOfResponses()
        
        for product in self.products:
            self.sentimentGraph.positives.append(product.responseHandler.positiveTotal)
            self.sentimentGraph.negatives.append(product.responseHandler.negativeTotal)
            self.sentimentGraph.neutrals.append(product.responseHandler.neutralTotal)
        
        