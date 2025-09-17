# Code Contributing Guidelines 
![GitHub commit activity](https://img.shields.io/badge/Repository%20Status-Migration!-yellow) &nbsp;

> [!CAUTION]
> Any contributions that violates these guidelines will be ignored/not approved for change (if you forgot one simple thing like marking your changes in the code then our team may remind you there and *you may not receive a warning*. But if you intentionally ignore a rule multiple times or break a rule like rewrite code from scratch without forking you will have warning) and you will be given a warning. If you receive 3 warnings, you will not be able to contribute anymore and our team will ignore all contributions made by you! Please read this carefully, thank you.

To consider *changing programs and codes* in this `Software` repository you have to **pull request first and wait for approval** which should be *reviewed* in the **maximum delay of ***7 days***** **unless** the repository is in inactive mode (in that case it will be noted in the [README.md](/README.md) file of this repository)! The "Pull Requests" tab is located on the top left corner of your screen (on computer), most generally under the word Software, and the "Issues" tab just on its left.

## Repository Modes:

Repository mode will be shown at the top left corner of this file as well as at the top of the repository [README](/README.md)

- Active: *All active repository maintainers working full-time on the `Software` repository and will review any issue*, pull request or any other thing within a **maximum delay of ***7 days*****.
- Semi Active: *One or more maintainers are working part-time on this repository*. Review time extends to ***30 days maximum***.
- Inactive: *No active maintainers are available due to certain circumstances*. This will usually be announced beforehand, but this time the delay extends to a period of ***6 to 12 months***.
- Offline: *No active helper person is available*. This will usually be announced beforehand, and ***replies are not guaranteed!***
- Busy: *All active repository maintainers are working on a certain task*, meaning that **delays may occur**, usually from ***30 days to 90 days long***.
- Migration: Although pretty rare to occur, this means *alll active repository maintainers are working on migration*, meaning that any issues and pull requests **will not be looked at *until* migration is over** and commits will **focus on migration tasks**. This usually makes the time of delay extend to a period of time of **minimum *1 to 2 months***.
- HIBERNATION: *ABSOLUTELY NO STAFF ACTIVE*. THIS WILL USUALLY BE ANNOUNCED 1 DAY OR MORE BEFORE THE EVENT. **ABSOLUTELY NO COMMITS WILL BE STAGED BY ANYONE AND NO REPLIES WILL BE PROVIDED DURING STATED DURATION TIME**

## Guidelines

> [!IMPORTANT]
> ### The new code must meet these basic guidelines:
> - The person who changes it **must *clearly* mark what they changed through any means** (code comments, start of programs *or/and* in program descriptions in the programs, commit logs are welcome, recommended and appreciated but aren't required yet).
> - It must follow a similar style of the original code (example: Rewriting ["security management system.py"](https://github.com/T1taniumF0rge-Industries-Inc/Software/blob/Main/PySoft/Utilities/security%20management%20system.py) in classes and imports module would most likely get rejected because this program uses while, input and print clauses, if you want to do that then you can copy the program onto your own fork of this repository and change it).
> - The new version of the file must still include the original copyright names and symbols, however you may still mention your username on any new code - see [this](https://github.com/T1taniumF0rge-Industries-Inc/Software/blob/Main/.github/faq.md#who-do-i-credit-if-i-fork-the-repository) section of the FAQ for more information on attribution and credits.
> - The new code must function properly including handling edge cases and malformed inputs, as well as not breaking the existing unchanged code. It must have some types of error handling and not just crumple in case an unexpected error happen.
> - The code must abide to the security, Code of Conduct and licenses and warranty/liability disclaimers that are present in the repository at the time of the pull request being made.
> - You are not allowed to do a pull request by just looking at the code and seeing something is wrong (unless it's blatantly obvious like print(passwod) instead of print(password), which in this case our team will thank you), such as [here](https://github.com/T1taniumF0rge-Industries-Inc/Software/blob/0d873336c748148a44703f6b852f641656674fa8/PySoft/Utilities/security%20management%20system%20-%20advanced%20edition.py#L234). This is a hack, but it works pretty well, and doesn't affect the user experience in the slightest. For a more in-detail issue that might look like an issue but it isn't, you must use the code before doing a pull request. Failing to do so will result in a warning.

> [!NOTE]
> - Please try and use meaningful commit messages that explain the changes in a precise but short manner (example: avoid commit messages like "fixed bug", instead try to aim for something like "fixed input bug that caused crashes in security management system"). It is very much appreciated, and it only has to be mentioned somewhere in the commit (could have a joke title and have the actual change underneath in the extended description)
> - The workflows in this repository may not work properly. It is expected to have workflow failures on each commit. If this happens, just ignore it. We are trying to find a solution to this problem.
> - If this repository is in inactive mode, the code may not get reviewed until 6 months of a pull request being opened. If it is in semi-active mode, expect the code to be reviewed within 30 days of a pull request being opened. The status can be viewed in the repository's [README](/README.md) or at the top left corner of this file.
> - You may want to add new languages to the repository (for now, we don't have official Bash scripts, but if you wanted you could create a new folder named BashSoft and go from there making your own Bash scripts)
> - For individual small files, it is best to use the web editor as this repository will take about 30 minutes on average to clone using Git Bash (12 minutes fastest on a speedy SSD), since this repository's local size is higher than 35GB (make sure you update)!
> - If you still want to use Git Bash, it is highly recommended to use and read the [Developer File Area](/DEVELOPER.md) to avoid any potential failures that Git can throw.
> - Your code may generate new security warnings. While not ideal, our team will review the situation and will make a decision based on the code.

### Example Case:

The python program underneath is broken and could use some improvements:

```py
print("Made by T1taniumF0rge")
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
print("Made by T1taniumF0rge")
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

> [!NOTE]
> In any situation where a warranty or liability disclaimer is present in the `Software` repository, "we", "The Software Team", "The Devs", "The Developers" all refer to the main developers of this repository. A warranty or liability disclaimer is a paragraph that includes "We will ***not*** be liable for **any damages caused by**", etc... and explains that we aren't liable for any damages no matter what.
>  
> For full details, go [here](https://github.com/T1taniumF0rge-Industries-Inc/Software/blob/main/.github/WARRANTY_LIABILITY_DISCLAIMER.md)!
>
> This repository `Software` full name `/T1taniumF0rge-Industries-Inc/Software` (old name `/GamerSoft24/Software`) is under the control of the **Titan1um™ & T1taniumF0rge® Industries Incorporated organization**.
