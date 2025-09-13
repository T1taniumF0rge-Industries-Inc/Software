# PySoft
Welcome to `Software`'s PySoft section, where I will be storing all of my and some of Okmeque1's Python codes and programs.

If you don't know Python or don't have a Python Interpreter installed, go download one version (like 3.12.2, 3.10, 3.8.2, etc...) depending on your computer [here](https://www.python.org/downloads/) from Python's website or from our [InstallerSoft category](https://github.com/T1taniumF0rge/Software/tree/Main/InstallerSoft/Windows/Python). Python3 and pip3 are recommended. ⚠ Make sure you have version 3.8 or above since most Python modules won't be able to run below that version (neither can modules be installed with pip). 

> [!NOTE]
>
> Some of these programs contains modules that have to be installed. To install these modules, you can go to [Pypa's repository](https://github.com/pypa/pip) and follow the instructions on how to install and use pip/pip3 if you don't have it on your PC although most of the Python3 interpreters will install pip/pip3 automatically (usually located in the "scripts" directory in the install location so make sure to try pip first before reading pypa).
After you have pip/pip3 installed, go to your computer's terminal (Mac Terminal, Windows Command Prompt, PowerShell, etc...) and type `pip install` + the module's name. *Example:* `pip install pygame`. Using `pip3 install` will also work if you have pip3 although it is only really required if you have Python 2 and Python 3 installed at the same time on your PC

> [!TIP]
>
> To install these modules faster, download the requirements.txt file in this folder, then run "pip install -r requirements.txt" in the same directory where you downloaded that text file. Note that if you have to run pip from the `scripts` folder, you may have to specify the full file name path with the drive name included (for easier installation next time, you might want to consider adding Pip to PATH but it is not required)! Pip will automatically find the newest compatible versions of these modules, and this could be more convenient than manually installing every single module. However it is not recommended if you are low on hard disk space as some modules may take up a lot of space, in which case it is recommended to choose which modules to install manually to check how much disk space they will use, as pip doesn't tell you how much disk space they will take before installation.
> 
By-the-way, are you interested in a short Python program that draws colorful rainbow void using a module named `turtle` (Python Graphics Drawing Module)? If you are, then copy this script down in your text editor (like Notepad++, Xcode, IDLE or your preferred):
```py
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
Then name your file making sure it ends in `.py` and save it. For me, I named it `rainbow void.py`. Run it by double-clicking the file just as you would with any files and programs and make sure you have an interpreter installed and configured to automatically run Python files. If you do have an interpreter, it should run properly and you should get a result like this:

![Screenshot 2024-03-10 at 19 24 55](https://github.com/T1taniumF0rge/Software/assets/136463938/07d213aa-acf2-4a58-bfae-32a5b3fce544)

If you encounter any problems with any Python files (*.py), please make sure to consult the [PySoft Errors Chart](/PySoft/Errors%20chart.md), the [FAQ](/.github/faq.md) and the Python manual. Programs will mostly come with error codes (0211, 6510B) so make sure to take that in mind if the program does specify it

## Extra Information:

> [!TIP]
>  If your computer contains multiple Python projects that are using module versions that are incompatible with the modules specified in the requirements.txt file, it is recommended to use a *Virtual Environment* to isolate the modules to a specific folder (and its subfolders). This means that any installed modules in this folder will not be installed and detected in any other folder of the computer. To do that, all you have to do is open a terminal, and then type `python -m venv {Directory for Virtual Environment}`. For example: `python -m venv C:\Python\PySoft` will make a virtual environment in `C:\Python\PySoft`. However it is not strictly required and for most users you can skip this step.
