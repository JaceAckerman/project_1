##//
#Author: Jace Ackerman
#Date:9/10/20204
#File: promptInterface.py
#Description: Prompts phi3 model by reading from 3 different text files with
#   desired prompts. Then storing the responses in seperate text files as well.
#   This program is meant to run in the project1325 environment that I created.
#   I pipped installed ollama into this environment. This is how ollama will run locally.
#
#//

import time
import ollama #Able to import because ollama is installed in the environment this file is meant to run in
import re
import os
class Phi3Interface:
    
    def __init__(self, promptFile):
        self.promptFile = promptFile
        
    #The getResponse() prompts phi3 and generate a response from phi3. The response is cleaned, and the entire 
    #response is put into an array, where white space determines each index. So "How are you" becomes [How, are, you] 
    #when the split() is used. Commas and periods are removed. If the first index is not one of three options
    #then the response is searched through using regex to find where phi3 used one of the three options in the response.
    #if no option is used in the response at all then it is assumed the comment is neutral.
    #This function also uses the ollama package to interact with phi3 model. 
    #Below ollama's generate function is used to return the response from phi3
    
    def getResponse(self, userReviewPrompt):
        try:
            replyFromPhi3 = ollama.generate(model='phi3', prompt=userReviewPrompt)
            response = replyFromPhi3['response'].strip().split()[0]
            #remove any period and commans from the response
            response = response.replace(".","")
            response = response.replace(",","")
            
            #if the first word in response is not positve, negative, or neutral
            if(response.lower() not in ['positive', 'negative', 'neutral']):
                match = re.search(r"\b(positive|negative|neutral)\b", replyFromPhi3['response'].strip(), re.IGNORECASE)
                if match:
                    #get the first match and set that equal to response.
                    response = match.group(1)
                #if the response had no mention of positive, negative, or neutral at all. Assume the review is neutral
                #because phi3 did not rate it positive or negative.
                else:
                    response = 'neutral'
           
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            time.sleep(1)  # Retry after 2 seconds
            return "Error"
        
    #writes data to a file then adds a new line afterwords
    def writeReplyToFile(self,fileToWrite, reply):
        with open(fileToWrite, 'a') as file:
            file.write(reply)
            file.write('\n') 
    
    #This is a decorator function that ensures the files don't get written to once they are made.
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
    
    #prompts phi3 by reading from a text file that already has prompts on every line. The method below reads
    #the prompt file line by line then generates a response for each line,and each line is a prompt.
    # each response should be a single answer.
    @preventDuplicateWrites
    def askAndWrite(self, fileToWrite):
        with open(self.promptFile, "r") as file:
            for line in file:
                if line: #do not read empyt lines
                    response = self.getResponse(line.strip())
                    self.writeReplyToFile(fileToWrite,response)
            
