import pytest
from responseHandler import ResponseHandler

def test_initialization():
    response = ResponseHandler('testResponses.txt')
    assert response.fileOfResponse == 'testResponses.txt'
    assert response.negativeTotal == 0
    assert response.positiveTotal == 0
    assert response.neutralTotal == 0

def test_read_responses():
    #testResponses contains 6 positives, 3 negatives, and 3 neutrals. All of these are on seperate lines
    response = ResponseHandler('testResponses.txt')
    response.readResponses()
    assert response.negativeTotal == 3
    assert response.positiveTotal == 6
    assert response.neutralTotal == 3