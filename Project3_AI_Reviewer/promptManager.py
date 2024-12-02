# Author: Jace Ackerman
# Date: 11/25/24
# File: promptManager.py
# Description: This file contains the prompManager class. This class is responsible for creating the prompts
# that will be sent to the phi-3. The class formats the prompts in a specific way so that phi-3 determines
# a review to be either positive, nuetral, or negative. It does this by creating a new text file that
# contains the prompt, then the comment the user left for the product. This allows the phi3Interface class 
# to read the file line by line to ensure a single response.

import os
class PromptManager:
    def __init__(self, fileOfReviews):
        self.fileOfUserReviews = fileOfReviews
        self.promptString = "Classify the following review as either 'positive', 'negative', or 'neutral' in one word:"
    
    def setPrompt(self, promptToSet):
        self.promptString = promptToSet
        
    #formats the prompt that is going to be passed to language model    
    def setUpPrompt(self, reviewFromUser):
        tempString = self.promptString
        tempString += reviewFromUser
        return tempString
    
     #writes data to a file
    def writeToFile(self,fileToWrite, dataToWrite):
        with open(fileToWrite, 'a') as file:
            file.write(dataToWrite)
    
    #This is a decorator function that ensures the prompt files don't get written to once they are made.
    def preventDuplicateWrites(func):
        def wrapper(self, fileToWrite):
            # Check if the file exists and already contains data
            if os.path.exists(fileToWrite):
                 with open(fileToWrite, "r") as f:
                    existing_content = f.read()
            # If the content already exists, skip the operation
            if existing_content.strip():  # File has content
                print(f"File '{fileToWrite}' already contains data.")
                #return error msg for debugging sake
                return f"File '{fileToWrite}' already contains data."
             
            # Call the original function if file is empty or doesn't exist
            return func(self, fileToWrite)
        return wrapper
    
    #reads from the file of reviews, then writes a prompt with a review on each line.
    #Uses setUpPrompt() to create the prompts that are written to fileToWrite.
    @preventDuplicateWrites
    def createPromptFile(self, fileToWrite):
        with open(self.fileOfUserReviews, "r") as file:
            for line in file:
                newPrompt = self.setUpPrompt(line)
                self.writeToFile(fileToWrite,newPrompt)


                
                    
        
   