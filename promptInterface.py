##//
#Author: Jace Ackerman
#Date:9/10/20204
#File: promptInterface.py
#Description: Prompts phi3 model by reading from 3 different text files with
#   desired prompts. Then storing the responses in seperate text files as well.
#   
#
#//

import sys
import subprocess
import ollama

#uses with statement to read and close the filename aswell as returns the contents as a string.
def read(filename):
    # Read the file
    with open(filename) as file:
        content = file.read()   #read() copies entire file into one string
    return content

#This function uses the above read() to get the prompt from one of the prompt text files
#This function also uses the ollama package to interact with phi3 model. 
#Below ollama's generate function is used to generate a prompt and return the response from phi3
def askPrompt(filename):
    promptFromFile = read(filename)
    replyFromPhi3 = ollama.generate(model='phi3', prompt = promptFromFile)
    return replyFromPhi3['response'] #this only returns the 'response' element from replyFromPhi3
 
#writes 
def writeReplyToFile(fileToWrite, reply):
    with open(fileToWrite, 'w') as file:
        file.write(reply)

#dictionary containing options A,B, and C that corresponds to the file name
#if the user wants to use option A, they will simply type that option.
prompts = ['promptA.txt', 'promptB.txt', 'promptC.txt']   
replies = ['replyFromPromptA.txt', 'replyFromPromptB.txt','replyFromPromptC.txt']  

#prompts phi3 with desired prompts and writes the replies in seperate text files
#Does this for all 3 prompts
def askAndWrite():
    for i in range(len(prompts)):
        writeReplyToFile(replies[i],askPrompt(prompts[i]))
        
        
askAndWrite()      
