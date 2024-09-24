Name: Jace Ackerman
Project 1: Generate Prompt and Save Response From Phi-3
Description: This Repository contains a Python script. The script takes three files that contain prompts. These three prompts are read and stored as strings.
These strings are passed to phi-3 using the Ollama package's generate(). The responses are stored in three different text files, "responseFromPromptA.txt", 
"responseFromPromptB.txt", and "responseFromPromptC.txt." 

HOW TO RUN SCRIPT
1) Download Miniconda
   Follow install instructions at https://docs.anaconda.com/miniconda/miniconda-install/
  - Miniconda will allow you to create/run the program inside the necessary environment
2)  Make Sure you Have Python Downloaded on your Computer
    - Go to https://realpython.com/installing-python/ for a quick guide on how to install Pyhton. 
3) Clone this git hub repository
    - Navigate to this repository.
    - Under the <code> tab
4) Create an Environment on your Computer
  - After installing Miniconda you should be able to run conda commands in your command prompt
  - Open up CDM. On Windows search 'CMD' in the Windows search tab. On MAC press command + spacebar and then type 'Terminal' to open Terminal.
  - type the following command: conda env create -f requirement.yaml
