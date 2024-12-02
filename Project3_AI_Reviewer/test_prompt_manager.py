import pytest
from promptManager import PromptManager

def test_initialization():
    promptManager = PromptManager("test.txt")
    assert promptManager.fileOfUserReviews == "test.txt"
    assert promptManager.promptString == "Classify the following review as either 'positive', 'negative', or 'neutral' in one word:"


def test_set_prompt():
    promptManager = PromptManager("test.txt")
    promptManager.setPrompt("hello")
    assert promptManager.promptString == 'hello'
    
def test_set_up_prompt():
    promptManager = PromptManager('test.txt')
    assert promptManager.setUpPrompt("I love this product") == (promptManager.promptString + "I love this product")
    
def test_write_to_file():
    promptManager = PromptManager('test.txt')
    promptManager.writeToFile(promptManager.fileOfUserReviews, "This is a test")
    with open(promptManager.fileOfUserReviews, 'r') as file:
        for line in file:
            assert line.strip() == "This is a test"
    #clear the test file for other testing
    with open(promptManager.fileOfUserReviews,'w') as file:
        file.write("")
        

def test_create_prompt_file():
    promptManager = PromptManager('test.txt')
    
    #manually writing a fake review to the test file
    promptManager.writeToFile(promptManager.fileOfUserReviews, "I love this product")
    promptManager.createPromptFile('testPromptFile.txt')
    with open('testPromptFile.txt', 'r') as file:
        for line in file:
            assert line.strip() == (promptManager.promptString + "I love this product")

    #now that the file is already made, the decorator function shouldn't allow data to be added to the prompt
    #file. Calling the createPromptFile() again should result in a message being thrown to the user that
    #the file attempting to be written to already has data in it. The following tests for that.
    promptManager.createPromptFile('testPromptFile.txt') == "File 'testPromptFile.txt' already contains data."
    
    #delete the content of the test files
    with open("testPromptFile.txt", 'w') as file:
        file.write("")
    with open(promptManager.fileOfUserReviews,'w') as file:
        file.write("")
     