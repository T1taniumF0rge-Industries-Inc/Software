# Code Contributing Guidelines 

To consider *changing programs and codes* in this `Software` repository you have to **pull request first and wait for approval** which should be *reviewed* in the **maximum delay of ***7 days***** **unless** the repository is in inactive mode (located in the README file)! The 'Pull requests' tab is located on the top left corner of your screen (on computer), most generally under the word Software.

> [!IMPORTANT]
> ### The new code must meet these basic guidelines:
>
> - The person who changes it must clearly mark what they changed through any means (code comments, start of programs or in program descriptions in the programs)
> - It must follow a similar style of the original code (example: Rewriting [Security Management System](https://github.com/GamerSoft24/Software/blob/Main/PySoft/Utilities/security%20management%20system.py) in classes and imports module would most likely get rejected because this program uses while, input and print clauses, if you want to do that then you can copy the program onto your own fork of this repository and change it.)
> - The new version of the file must still include the original copyright names and symbols, however you may still mention your username on any new code.
> - The new code must function properly including handling edge cases and malformed inputs, as well as not breaking the existing unchanged code
> - The code must abide to the security, code of conduct and licenses that are present in the repository at the time of the pull request being made.
>   
> ### Some things to take note about:
>
> - The DEVELOPER.md Last Push/Pull section can be ignored, this is only for the repository collaborators and owners.
> - The workflows in this repository may not work properly. It is expected to have workflow failures on each commit. If this happens, just ignore it.
> - If this repository is in inactive mode, the code may not get reviewed until 6 months of a pull request being opened. If it is in semi-active mode, expect the code to be reviewed within 30 days of a pull request being opened.
> - You may want to add new languages to the repo (for now, we don't have official BASH scripts, but if you wanted you could create a new folder named BASHSoft and go from there making your own BASH scripts)
> - For individual small files, it is best to use the web editor as this repository will take about 30 minutes on average to clone using Git BASH, since this repo is 35.6GB on a local computer.
> - If you still want to use Git BASH, it is highly recommended to use the [Developer File Area](/DEVELOPER.md) to avoid any potential failure
> - Your code may generate new security warnings. While not ideal, our team will review the situation and will make a decision based on the code.
> - 

### Example Case:

The python program underneath is broken and could use some improvements:

```py
print("made by gamersoft24")
number = 1
def random_math_function(amount):
  for x in range(amount):
    number = number + number
  return number + amount
input("Enter a random number")
random_math_function
```

A change like so is a good starting spot, although in this case if you could make the inputs explain what they do it would be even better:

```py
print("made by gamersoft24")
print("Fixed made by GmaerSoft42")
number = input("Enter a random number to add:") #By GmaerSoft42: Input added so that you can choose the base starting number
def random_math_function(amount)
  for x in range(amount):
    number += number
    number += amount
  return number
amount = input("Enter a random number to recurse") # fixed broken input, GmaerSoft42
random_math_function(amount) #Calling function properly - GmaerSoft42
```

