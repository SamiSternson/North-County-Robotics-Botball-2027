# How To Use Some of These Files
## Sending Files To The Wombat
### How This Actually Works 
Because KIPR does all this weird stuff with the way it runs files with their IDE and botUI it is hard to replicate their process and create files that can be viewed and run from their IDE and botUI program page. Instead, what we do is load all scripts into a folder called scripts. We then run a program through the botUI program page that lets us run this python program (explained more later). 
### How To Send Files From VS-Code to the Wombat
1. Connect to the Wombat's WiFi
2. Run send_file_to_wombat.py
3. Enter the global file paths to the file you want to send over.
4. Enter the password for the Wombat (default password is **botball**)
### How to run files you sent to the Wombat from VS-Code
1. Copy the file main.py from the RunPythonFile project in Default User into your project on your user. 
2. Edit the file name to the name of the file you sent to the wombat using VS-Code (*make sure to include the .py*).
3. Compile the project and run.
### Best Practices for Files You Are Sending Over
1. ***Make sure you are not using the same file name as someone else.*** This is increadibly important because all the files go into a communal scripts folder, and if you use the same file name as someone else you will overwrite their file. I recomend naming your file your Name/Username and then the normal file name (for example: ```main.py``` should be ```Sami_main.py```).

2. If you want your program to output anything more complicated than a simple print statement (for example a graph), don't use a libraries built in method to automatically show the graph/image/whatever in a new custom window. Instead, make it so that the program saves the file to ```/home/kipr/Documents/KISS/outputs/```. At some point, I (more like Claude) will write a script to find a file you want from this folder and ssh it back to your computer. Again, make sure the file you are exporting into the ```/home/kipr/Documents/KISS/outputs/``` folder has a unique name. 

Currently, this is pretty experimental and subject to change. I have only tested this on linux, so it may not work on Windows or Mac. 