Name: Jace Ackerman

Project 3: Perform a sentiment analysis of product reviews for different versions of Apple Watches.

Description: This branch contains all of the files that are necessary for Project 3. It has new code as well as code from project 1 and project 2. In Project 2 I designed
a web scraper that scraped reviews of Apple Watch versions from eBay. A big requirement for this project was to rewrite our code to be modular and follow S or D principles. My code in Project 2 was already modularized and already followed the single responsibility principle. My code in Project 2 has a Scraper, Parser, DataHandler, UrlHandler, and ScrapingManager classes. Each class has one responsibility. Even the ScrapingManager just has the responsibility of integrating all the classes. The Scraper class just gets the HTML document. The Parser class filters through this document for the desired data. The DataHandler class just saves the data gathered from the parser class. The UrlManager class only gets the URLs to the review pages from a file. Each class serves one purpose thus this code satisfies the S principle in SOLID.

The code I wrote for project 1 did not satisfy the S principle. I had to write 6 new classes. PromptManager which has the responsibility of creating prompt files. Phi3Interface which has the responsibility of generating a response from Phi3 and then saving the responses. ResponseHandler has the responsibility of reading the generated output from phi3 and counting the number of positive, negative, and neutral responses. The Graph class is responsible for making the graph. The SentimentAnalysis class is responsible for integrating ResponseHandler, PromptManager, and Phi3Interface. The PerformAnalysis class integrates the SentimentAnalysis and Graph classes and is responsible for running the entire analysis of all five Apple Watches. Each product is a SentimentAnalysis object. This is very similar to how each product represents a ScrapingManager object in project 2. All of the classes I just described have a single purpose or do only one thing for the whole project. This is how the new classes satisfies the S principle. This means project 3 is modularized and satisfies the single responsibility principle.

HOW TO RUN PROGRAM
=============================================================================================================================================================================

1) Download Miniconda
   - Follow install instructions at https://docs.anaconda.com/miniconda/miniconda-install/
   - Miniconda will allow you to create/run the program inside the necessary environment
     
2)  Make Sure you Have Python Downloaded On your Computer
    - Go to https://realpython.com/installing-python/ for a quick guide on how to install Python.
      
3) Clone or Install This Git Hub Repository BRANCH
   - Navigate to this repository branch
   - Click on the code dropdown menu and you can either clone this repository branch using the link or download the zip file.
   - DO NOT DOWNLOAD FROM THE MAIN BRANCH, to run this software you must only use the files in this branch. Any other branch will be for different software.
   - Make sure to put repository files in a place you can access in your file system.
     
   
5) Navigate To the Folder Where You Stored The Repository's Files From THIS Branch
   - Open up CDM. On Windows search 'CMD' in the Windows search bar. On MAC press command + spacebar and then type 'Terminal' to open Terminal.
   - Navigate to the directory where you stored the files in this repository. On Windows, you can type this command: cd C:\FullPath\To\Your\Directory.
   - Alternatively, in Windows, you can just keep typing cd "name of folder" to access the next folder or cd .. to get out of the current folder and go to the previous folder until you have navigated to the folder where you stored the files from this branch.
     
6) Create an Environment on your Computer
   - After installing Miniconda you should be able to run conda commands in your command prompt or terminal
   - Make sure when you type the following conda command you are inside the folder with the repository files you just downloaded, again make sure it's from this branch
   - Type the following command: conda env create -f requirements.yaml
   - Then type: conda clean -p
   - conda will automatically name the environment to what the environment was originally called
     
7) Activate Conda Environment 
   - In the same directory, type: conda activate project2Env
   - You should see '(project2Env)' in front of the command line now
  
8) Run Python Script
   - Inside the environment type the following command: python executable.py
   - Hit enter, the program might take a while to run because it is scrapping all the data from the website

You have successfully ran this software! Look at all the output text files to see the reviews that were scrapped from the website. For example, "series5Reviews.txt" should have all the reviews for a series 5 Apple Watch listed on eBay.

    
