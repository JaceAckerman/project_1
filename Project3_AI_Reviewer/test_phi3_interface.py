import pytest
from phi3Interface import Phi3Interface

def test_initialization():
    phi3 = Phi3Interface("testPhi3PromptFile.txt")
    assert phi3.promptFile == 'testPhi3PromptFile.txt'

def test_get_response():
    phi3 = Phi3Interface("testPhi3PromptFile.txt")
    
    #Testing for a positive review
    positiveResponse = phi3.getResponse("Classify the following review as either 'positive', 'negative', or 'neutral' in one word: I love this product")
    assert positiveResponse.lower().strip() == 'positive'
    
    #Testing for negative review
    negativeResponse = phi3.getResponse("Classify the following review as either 'positive', 'negative', or 'neutral' in one word: I hate this product")
    assert negativeResponse.lower().strip() == 'negative'
    
    #Testing for a neutral review
    neutralResponse = phi3.getResponse("Classify the following review as either 'positive', 'negative', or 'neutral' in one word: I do not hate it, but I do not love it either. I am pretty neutral about the product")
    assert neutralResponse.lower().strip() == 'neutral'
    
    #Testing when phi3 does not respond with one of three option in the first word of the response
    response = phi3.getResponse("Classify the following review as either 'positive', 'negative', or 'neutral' in one word: :)")
    assert response.strip().lower() in ['positive', 'negative', 'neutral']
    
    #Testing for the case if phi3's response does not contain the word 'positive', 'negative', or 'neutral' at all
    #To do this test I gave phi3 a randome prompt that has nothing to do with the original prompt. 
    #This should simulate the case where one of the three options is not in the response at all
    #The response should be 'neutral' because of how the getResponse() handles this case.
    response = phi3.getResponse("What is 2+2")
    assert response.strip().lower() == 'neutral'
    
def test_write_reply_to_file():
    phi3 = Phi3Interface('test.txt')
    phi3.writeReplyToFile(phi3.promptFile, "This is a test")
    with open(phi3.promptFile, 'r') as file:
        for line in file:
            assert line == "This is a test\n"
    #clear the test file for other testing
    with open(phi3.promptFile,'w') as file:
        file.write("")

def test_ask_and_write():
    phi3 = Phi3Interface('testPhi3PromptFile.txt')
    phi3.askAndWrite('test.txt') #writing responses to test.txt
    with open('test.txt', 'r') as file:
        for line in file:
            assert line.strip().lower() in ['positive', 'negative', 'neutral']
            
    #clear the test file for other testing
    with open('test.txt','w') as file:
        file.write("")