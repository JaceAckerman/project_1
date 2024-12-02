# Author: Jace Ackerman
# Date: 11/25/24
# File: sentimentAnalysis.py
# Description: This file contains the SentimentAnalysis class. SentimentAnalysis is responsible for integrating
# phi3Interface.py, promptManager.py, and responseHandler.py. This class will be able to declare an object for each
# product. This way the data for each product is modularized and will reside in objects. This class
# will set up a prompt file to pass as input to the phi3 model. Then will prompt and save the responses from
# phi3 for each review. Finnally, it will count and save the number of positive, negative, and neutral responses.

from phi3Interface import Phi3Interface
from promptManager import PromptManager
from responseHandler import ResponseHandler
class SentimentAnalysis:
    def __init__(self, fileOfReviews, fileToWriteResponses, promptFile):
        self.fileToWriteResponses = fileToWriteResponses
        self.promptFile = promptFile
        self.promptManager = PromptManager(fileOfReviews)
        self.responseHandler = ResponseHandler(fileToWriteResponses)
        self.phi3 = Phi3Interface(promptFile)
    
    #Analyze() creates the prompt file for the products, then askAndWrite analyzes the reviews to get the 
    #senttiment of each review.
    def analyze(self):
        self.promptManager.createPromptFile(self.promptFile)
        self.phi3.askAndWrite(self.fileToWriteResponses)
    
    #countResponses uses the responseHandler object to count the number of 'positives', 'negatives', and 'neutrals'
    #phi3 generated per each review.
    def countResponses(self):
        self.responseHandler.readResponses()
