# PySoft
Welcome to `Software`'s PySoft section, where I will be storing all of my and some of Okmeque1's Python codes and programs.

If you don't know Python or don't have a Python Interpreter installed, go download one version (like 3.12.2, 3.10, 3.8.2, etc...) depending on your computer [here](https://www.python.org/downloads/) from Python's website or from our [InstallerSoft category](https://github.com/GamerSoft24/Software/tree/Main/InstallerSoft/Windows/Python). Python3 and pip3 are recommended. ⚠ Make sure you have version 3.1 or above since most Python modules won't be able to run below that version (neither can it be installed with pip). 

Some of these programs contains modules that have to be installed. To install these modules, you can go to [Pypa's repository](https://github.com/pypa/pip) and follow the instructions on how to install pip/pip3 if you don't have it on your PC although most of the Python3 interpreters will install pip3 automatically (usually located in the "scripts" directory in the install location).
After you have pip/pip3 installed, go to your computer's terminal (Mac Terminal, Windows Command Prompt, PowerShell, etc...) and type `pip install` + the module's name. *Example:* `pip install pygame`. Using `pip3 install` will also work if you have pip3.

> [!TIP]
>
> To install these modules faster, download the requirements.txt file in this folder, then run "pip install -r requirements.txt" in the same directory where you downloaded that text file. Pip will automatically find the newest compatible versions of these modules, and this could be more convenient than manually installing every single module. However it is not recommended if you are low on hard disk space.
> 
By-the-way, are you interested in a short Python program that draws colorful rainbow void using a module named `turtle`? If you are, then copy this script down in your text editor (like Notepad++, Xcode or IDLE):
```
import turtle
q = turtle.Pen()
turtle.bgcolor("black")
sides = 7
colors = ["red","orange","yellow","green","cyan","blue","purple"]
for x in range(360):
  q.pencolor(colors[x%sides])
  q.forward(x*3/sides+x)
  q.left(360/sides+1)
  q.width(x*sides/200)
```
Then name your file `*.py` and save it. For me, I named it `rainbow void.py`. Run it by double-clicking the file just as you would with any files and programs and make sure you have an interpreter installed. If you do have an interpreter, it should run properly and you should get a result like this:

![Screenshot 2024-03-10 at 19 24 55](https://github.com/GamerSoft24/Software/assets/136463938/07d213aa-acf2-4a58-bfae-32a5b3fce544)
