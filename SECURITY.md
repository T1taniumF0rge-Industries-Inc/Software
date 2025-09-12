# Security Policy

## Our Programs:
All of our programs hosted on this repository are carefully made and have been revised and scanned for **any types** of *sneaky viruses or script problems.* They are **mostly trustable** and for the most part **completely safe, exluding explicitely marked programs such as viruses/pranks and Windows Loaders. Most material will include the source if you are unsure of the contents of our *carefully* repackaged installers** As the programs are very *hardware intensive*, they may take some time to load. Please be patient!

## Supported Security versions:

Use this section to tell people about which versions of your project are
currently being supported with security updates. 

| Version | Supported          |
| ------- | ------------------ |
| 5.2.x   | :white_check_mark: |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :warning:          |
| 4.1.x   | :x:                |
| < 4.1   | :x:                |

## Ignored security warnings:

Sometimes, code like this triggers CodeQL's automatic alert system (["security management system.py"](/PySoft/Utilities/security%20management%20system.py) in this example because you print the `password` variable straight to the terminal in a non-encrypted way - as plain text):
```py
elif optionpwd_manager == 7:
  cyrillic_character_set = "АаВеЕЗМоНОРрСсТуХхЈјҮԁԌԚԛԜԝ"
  standard_chars = '¦¬`1!23#4$5%6^7&8*9(0-_=+q"~{[]}=+QwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~^%#\|zZxXcCvVbBnNmMm,<.>/?)'
  chars = [cyrillic_character_set, standard_chars]
  length = int(input("Please enter your password length: "))
  pwd = ""
  for x in range(length):
      pwd += random.choice(random.choice(chars))
  print("")
  print(password)
  print("")
  print('Password generated! Now saving...')
  filename = input("Please enter a valid file name (leave blank to a default file of pwd_openscs.pwd). If the file does not
```
However, our team at the `Software` repository have deemed these warnings an exaggeration, as in reality nobody is going to spy on your terminal, and stuff printed to the terminal can be easily deleted by just closing the terminal or clearing it. And for your information, we don't use logs because our programs aren't important enough that logs are required. More literal explanation is that for a password manager system like Security Management System, there really isn't another way to show the password to the user (nowadays we use pyperclip but only in SMS (security management system) advanced) However, some newer programs are updated to be more compliant security measures so it is recommended to always use the newest available programs for your needs.

> [!WARNING]
>
> **This is a reminder that it is always important to protect your personal information through any means possible. This can be done with a number of methods, such as encrypting files, using strong passwords, storing files on USB drives that aren't plugged into any computers stored in a safe, etc.**

## Pull requests:
To consider *changing programs and codes* in this `Software` repository you have to **pull request first and wait for approval** which should be *reviewed* in the **maximum delay of ***7 days***** **unless** the repository is in inactive mode! The 'Pull requests' tab is located on the top left corner of your screen (on computer).

For more information, see the [Contributing Guidelines File.](/CONTRIBUTING.md)

## Reporting (private and official) and suggestions: 
To *report* privately and officially or make any *suggestions* to the repository, click the 'Issues' tab also located on the top left corner of your screen. Then, choose a template that suits you the best or just open a blank template and then write your issue report(s) or suggestion(s) down. Once finished, just submit and your all good!

To *report* violence, unacceptable behaviour or security vulnerabilities, you can:

1 -> Email: "gamersoftware.corp@gmail.com" (private reporting) if the issue is just violation to our Code of Conduct and etc... (Although you could always directly submit reports to GitHub themselves if you feel that the situation is really serious. Also specify the username of the violator and the details of the situation. We will respond to you and confirm that we've seen your email as soon as possible. It is recommended that you don't use your main / personal email if you wish to not disclose those type of informations but be notified that we would still need to be able to contact you just in case so make sure that your provided contact methods are reliable!

2 -> Submit a GitHub Bug Bounty report (official reporting) in the 'Issues' tab (you should know where it is by now) if the issue is a security vulnerability. Submit once finished an GitHub should be informed unless their servers are down.

## Liability Disclaimer:

> [!IMPORTANT]
>
> Despite our programs being selected and tested to not break your computer with any sort of *sneaky* viruses or other problems **unless explicitely marked and/or said otherwise**, we can not fully guarantee maximum compatibility for your system (e.g whether it will run on your device, make it break or so on) due to your hardware capabilities. If you have low hardware power, then the program might crash on you, and vice-versa. To use **any material** from this repository, you must agree to the **[license](/LICENSE)** and its terms of conditions, as well as ***any* and *all* disclaimers and warranty information (if applicable)**. We will ***not*** be liable for **any damages caused by any file, software package, individual program or other material from this repository *in your possession (this includes, but is not limited to, modification, execution or download of the files)*! This includes, but is not limited to, unintentional bugs, user error caused by an unclear prompt (usually an old outdated program), clearly marked dangerous programs that may crash your computer or user negligence (didn't read the warnings) and more. However you may open an issue at any time for support and improvement of the material present, and we will try our best to resolve the issues as best as we can.**

> [!NOTE]
> In any situation where a warranty disclaimer is present in the `Software` repository, "we", "The Software Team", "The Devs", "The Developers" all refer to the main developers of this repository. A warranty disclaimer is a paragraph that includes "We will ***not*** be liable for **any damages caused by**", etc... and explains that we aren't liable for any damages no matter what.
>  
> This repository `Software` full name `/T1taniumF0rge/Software` (old name `/GamerSoft24/Software`) is under the control of the **Titan1um™ & T1taniumF0rge® Industries Incorporated organization**.
