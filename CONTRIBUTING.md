# Code Contributing Guidelines 

To consider *changing programs and codes* in this `Software` repository you have to **pull request first and wait for approval** which should be *reviewed* in the **maximum delay of ***7 days***** **unless** the repository is in inactive mode (in that case it will be noted in the [README.md](/README.md) file of this repository)! The "Pull Requests" tab is located on the top left corner of your screen (on computer), most generally under the word Software, and the "Issues" tab just on its left.

> [!IMPORTANT]
> ### The new code must meet these basic guidelines:
> - The person who changes it **must *clearly* mark what they changed through any means** (code comments, start of programs *or/and* in program descriptions in the programs, commit logs are welcome, recommended and appreciated but aren't required yet).
> - It must follow a similar style of the original code (example: Rewriting ["security management system.py"](https://github.com/GamerSoft24/Software/blob/Main/PySoft/Utilities/security%20management%20system.py) in classes and imports module would most likely get rejected because this program uses while, input and print clauses, if you want to do that then you can copy the program onto your own fork of this repository and change it).
> - The new version of the file must still include the original copyright names and symbols, however you may still mention your username on any new code - see [this](https://github.com/GamerSoft24/Software/blob/Main/.github/faq.md#who-do-i-credit-if-i-fork-the-repository) section of the FAQ for more information on attribution and credits.
> - The new code must function properly including handling edge cases and malformed inputs, as well as not breaking the existing unchanged code. It must have some types of error handling and not just crumple in case an unexpected error happen.
> - The code must abide to the security, Code of Conduct and licenses that are present in the repository at the time of the pull request being made.

> [!NOTE]
> - Please try and use meaningful commit messages that explain the changes in a precise but short manner (example: avoid commit messages like "fixed bug", instead try to aim for something like "fixed input bug that caused crashes in security management system"). It is very much appreciated, and it only has to be mentioned somewhere in the commit (could have a joke title and have the actual change underneath in the extended description)
> - The workflows in this repository may not work properly. It is expected to have workflow failures on each commit. If this happens, just ignore it. We are trying to find a solution to this problem.
> - If this repository is in inactive mode, the code may not get reviewed until 6 months of a pull request being opened. If it is in semi-active mode, expect the code to be reviewed within 30 days of a pull request being opened. The status can be viewed in the repository's [README](/README.md)
> - You may want to add new languages to the repository (for now, we don't have official Bash scripts, but if you wanted you could create a new folder named BashSoft and go from there making your own Bash scripts)
> - For individual small files, it is best to use the web editor as this repository will take about 30 minutes on average to clone using Git Bash (12 minutes fastest on a speedy SSD), since this repository's local size is higher than 35GB (make sure you update!
> - If you still want to use Git Bash, it is highly recommended to use and read the [Developer File Area](/DEVELOPER.md) to avoid any potential failures that Git can throw.
> - Your code may generate new security warnings. While not ideal, our team will review the situation and will make a decision based on the code.

### Example Case:

The python program underneath is broken and could use some improvements:

```py
print("Made by GamerSoft24")
number = 1
def random_math_function(amount):
  for x in range(amount):
    number = number + number
  return number + amount
input("Enter a random number: ")
random_math_function
```

A change like so is a good starting spot, although in this case if you could make the inputs explain what they do it would be even better with comments across the code or a print at the start of the code. If you want a better example, you could look inside the PySoft folder with the evolution of `security management system.py` into `AssistantApp` or `SQLite Password Manager`, as those are massive improvements over time.:

```py
print("Made by GamerSoft24")
print("Fixes made by GmaerSoft42")
number = int(input("Enter a random number to add:") # By GmaerSoft42: Input added so that you can choose the base starting number) #bruh the program was broken even on the fixed version: gmaersoft42
def random_math_function(amount):
  for x in range(amount):
    number += number
    number += amount
  return number
amount = input("Enter a random number to recurse: ") # Fixed broken input, GmaerSoft42
random_math_function(int(amount)) # Calling function properly - GmaerSoft42
```

