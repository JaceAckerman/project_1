Name: Jace Ackerman

Project 1: Generate Prompt and Save Response From Phi-3

Description: This Repository contains a Python script. The script takes three files that contain prompts. These three prompts are read and stored as strings.
These strings are passed to phi-3 using the Ollama package's generate(). The responses are stored in three different text files, "responseFromPromptA.txt", 
"responseFromPromptB.txt", and "responseFromPromptC.txt." 

HOW TO RUN PROGRAM
=============================================================================================================================================================================

1) Download Miniconda
   - Follow install instructions at https://docs.anaconda.com/miniconda/miniconda-install/
   - Miniconda will allow you to create/run the program inside the necessary environment
     
2)  Make Sure you Have Python Downloaded On your Computer
    - Go to https://realpython.com/installing-python/ for a quick guide on how to install Pyhton.
      
3) Clone or Install This Git Hub Repository
   - Navigate to this repository
   - Click on the code dropdown menu and you can either clone this repository using the link or download the zip file.
   - Make sure to put repository files in a place you can access in your file system.
   
5) Navigate To the Folder Where You Stored The Repository's Files
   - Open up CDM. On Windows search 'CMD' in the Windows search bar. On MAC press command + spacebar and then type 'Terminal' to open Terminal.
   - Navigate to the directory where you stored the files in this repository. On Windows you can type this command: cd C:\FullPath\To\Your\Directory.
     
6) Create an Environment on your Computer
   - After installing Miniconda you should be able to run conda commands in your command prompt or terminal
   - Make sure when you type the following conda command you are inside the folder with the repository files you just downloaded
   - Type the following command: conda env create -f requirement.yaml
   - Then type: conda clean -p
     
7) Activate Conda Environment 
   - In the same directory, type: conda activate project1325
   - You should see '(project1325)' in front of the command line now
  
8) Run Python Script
   - Inside the environment type the following command: python promptInterface.py
   - Hit enter, the program might take a while to run because it has to wait on responses from Phi-3.

You have successfully ran this software! Look at the response text files to see the responses Phi-3 generated when asked the prompts from the prompt text files.

    
