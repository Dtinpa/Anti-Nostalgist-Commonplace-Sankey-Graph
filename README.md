Installation:

  macOS / Linux:

  You will need to ensure you have the latest version of python, pip, and the plotly package.
    
    Run to install python: sudo apt-get install python3
    Run to install pip: sudo apt-get install python3-pip
    Run to install plotly graphing package: pip install plotly

  From there you should be good to run the python script and interact with the graph in your web browser of choice.

  Windows:
    
    You'll need to download one of the latest versions of python.  Some parts of this will require opening the Windows
    Command Prompt to install packages.

    Go to the Windows Store, and download a version of python that is greater than 3.10.
    Open Windows Command Prompt and run the following command: py -m pip install plotly
    Go to your Windows search bar and search for the python application.  Run it to get a default window open.
    From there, you can select File >> Open, and locate the sankey.py file.
    Now you should be good to select Run >> Run Module, or hit the F5 key.  Make sure sankey.py and DataSet.txt are in the same directory, they are by default.

  The graph will appear in your browser window, and it has slight interactability.  You'll be able to highlight the connections between nodes, seeing which books realte to which topoi.
  Do not edit the Dataset.txt file.  You do not need to edit it.
  Get a fucking linux computer at this point.  Ubuntu is so easy to use.

  Purpose:

  To plot out all of the notes and their relationship to high level topics (topoi) and their location within the Anti-Nostalgist Commonplace.
  John Locke created an indexing system for commonplace books, and this graph is an attempt to create a new way of doing the same thing.
  By plotting the topics and their relationship to different reading material, I wanted to show the degree of overlap to get a birds eye view
  of what the reader may want to check out in regards to my notes.
