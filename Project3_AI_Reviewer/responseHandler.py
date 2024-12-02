# Author: Jace Ackerman
# Date: 11/25/24
# File: responseHandler.py
# Description: This file contains the responseHandler class. This class will handle the responses that phi3
# generates. The idea is that each response is put into an array. The values put into the array will either be
# "positive", "negative", or "neutral." This class will help gather the data so that it can be used to create
# the graph. 
import re
class ResponseHandler:
    def __init__(self, fileOfResponses):
        self.fileOfResponse = fileOfResponses
        self.positiveTotal = 0
        self.negativeTotal = 0
        self.neutralTotal = 0

    #read from the response file and increments the instance variables positives, negatives, or neutral
    # depending on what the line is eqaul to. If a line has a 'positive' string then positives is incremented
    # this keeps track of how many positive, negative, and neutral reviews a product has. This will help with 
    # making the plot.
    def readResponses(self):
        with open(self.fileOfResponse, 'r') as file:
            for line in file:
                if(line.lower().strip() == 'positive'):
                    self.positiveTotal +=1
                elif(line.lower().strip() == 'negative'):
                    self.negativeTotal +=1
                    #the line has to be 'neutral'
                elif(line.lower().strip() == 'neutral'):
                    self.neutralTotal +=1

        