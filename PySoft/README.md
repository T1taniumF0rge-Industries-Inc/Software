### PySoft
Welcome to `Software`'s PySoft section, where I will be storing all of my and some of Okmeque1's Python codes and programs.

Some of these codes contains modules that have to be installed. To install these modules, you to go to [Pypa's PIP repository](https://github.com/pypa/pip) and follow the instructions on how to install PIP if you don't have it on your PC although most of the Python interpreters will install PIP automatically.
After you have PIP installed, go to your PC's Command Prompt (CMD) and type `pip install` + the module's name. *Example:* `pip install pygame`.

If you don't know Python or don't have a Python Interpreter installer, go choose and download one depending on your computer [here](https://www.python.org/downloads/) from Python's website or from our [InstallerSoft category](https://github.com/GamerSoft24/Software/tree/Main/InstallerSoft/Windows/Python).

Do you want a short Python program that draws colorful rainbow void? Copy this script in your text editor:
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
Then name your file `rainbow void.py` and save it. Run it by double-clicking the file just as you would with any files and programs and make sure you have an interpreter installer (3.12.2, 3.10, 3.8.2, etc...). If you do, have an interpreter, it should run properly and you should get a result like this:

![Screenshot 2024-03-10 at 19 24 55](https://github.com/GamerSoft24/Software/assets/136463938/07d213aa-acf2-4a58-bfae-32a5b3fce544)
