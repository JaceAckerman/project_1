Name: Jace Ackerman

Project 2: Scrape Reviews From a Website and Put Reviews in a Text File

Description: This branch contains the file project2_webScrapper. Inside this file is software that can scrape a website, parse the data that was scrapped, and then put that data into an individual text file. This software does this for Apple Watch Series 5-9. It pulls the reviews for these products from eBay. All of this is done automatically when the software is ran. To run the software yourself, follow the steps below.

HOW TO RUN PROGRAM
=============================================================================================================================================================================

1) Download Miniconda
   - Follow install instructions at https://docs.anaconda.com/miniconda/miniconda-install/
   - Miniconda will allow you to create/run the program inside the necessary environment
     
2)  Make Sure you Have Python Downloaded On your Computer
    - Go to https://realpython.com/installing-python/ for a quick guide on how to install Pyhton.
      
3) Clone or Install This Git Hub Repository BRANCH
   - Navigate to this repository branch
   - Click on the code dropdown menu and you can either clone this repository branch using the link or download the zip file.
   - DO NOT DOWNLOAD FROM THE MAIN BRANCH, to run this software you must only use the files in this branch. Any other branch will be for different software.
   - Make sure to put repository files in a place you can access in your file system.
     
   
5) Navigate To the Folder Where You Stored The Repository's Files From THIS Branch
   - Open up CDM. On Windows search 'CMD' in the Windows search bar. On MAC press command + spacebar and then type 'Terminal' to open Terminal.
   - Navigate to the directory where you stored the files in this repository. On Windows you can type this command: cd C:\FullPath\To\Your\Directory.
   - Alternatively, in windows, you can just keep typing cd "name of folder" to access the next folder or cd .. to get out of the current folder and go to the previous folder until you have navigated to the folder where you stored the files from this branch.
     
6) Create an Environment on your Computer
   - After installing Miniconda you should be able to run conda commands in your command prompt or terminal
   - Make sure when you type the following conda command you are inside the folder with the repository files you just downloaded, again make sure its from this branch
   - Type the following command: conda env create -f requirements.yml
   - Then type: conda clean -p
   - conda will automatically name the environment to what the environment was originally called
     
7) Activate Conda Environment 
   - In the same directory, type: conda activate project2Env
   - You should see '(project2Env)' in front of the command line now
  
8) Run Python Script
   - Inside the environment type the following command: python executable.py
   - Hit enter, the program might take a while to run because it is scrapping all the data from the website

You have successfully ran this software! Look at all the output text files to see the reviews that were scrapped from the website. For example, "series5Reviews.txt" should have all the reviews for a series 5 Apple Watch listed on eBay.

    
