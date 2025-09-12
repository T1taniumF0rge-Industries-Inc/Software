# Frequently Asked Questions (FAQ)

> [!NOTE]
> More stuff are getting added to this file. Please be patient while our team finishes the FAQ.

This document aims to answer some common questions regarding the `Software` repository.

## Repository Q&A:

### Why is there so many things?

The goal of the `Software` repository is that everything is in one centralised area. We cover many topics and languages, such as Python, Batch, the C-family, Visual Basic Script (VBS), HyperText Markup Language (HTML) as well as other formats, such as useful software installers in InstallerSoft, game hacks in HackSoft, movies and music in MovieSoft, Minecraft-related stuff in MinecraftSoft, useful repository downloads in RepoSoft, pictures in PictureSoft and useful Office templates in OfficeSoft.

### Who do I credit if I fork, use code or any material from this repositoru?

For most programs, you must copyright Midnight_G0ldX Corporation **AND** T1taniumF0rge-Industries-Inc, and if the original program had some parts made by Okmeque1 Corporation or Lan Internet LLC, you must mention them respectively (but not both, they are seperate entities), like so.

`© Midnight_G0ldX Corporation`

`© T1taniumF0rge-Industries-Inc `

`© Okmeque1 Corporation`

`© Lan Internet LLC`

If you are going to copy a file that isn't in a fork or traceable really, you must include a `Credits.md` file in the same directory as the copied project, in an appropriate and neat format like so:
```
# Credits

### © One of the three company names above: [`Display Text Hyperlink`](Link to the copied project)
```
Example:
```
# Credits

### © Okmeque1 Corporation: [`/Okmeque1/Software`](https://github.com/Okmeque1/Software)
```

It should render like [so](/.github/credits_template.md/)

### Why are half the workflows failing?

This is because our workflow configuration hasn't been finished yet, and the best solution is to ignore it.

### Why are there closed security warnings that may matter?

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


### Where do I find the programs?

We have a lot of software available at your disposal for a lot of applications. It would be very inefficient and inconvenient to either navigate through every single binary in releases or have to move repositories just to download a side program that's an add-on to a regular program. So we have created the [Programs.md](/Programs.md) - a program chart, where you can find all of your required files, properly sorted and sectioned.

### Why does the repository take higher than 35GB of disk space?

We store a lot of binary files using Git LFS, including executables, movies, etc... Thanks to [Git LFS](https://git-lfs.com/) and their [GitHub](https://github.com/git-lfs/git-lfs) for making the `Software` repository project possible.

### Why are the commit messages meaningless?

You may find that some commit messages have absolutely nothing to do with the change, which is not ideal but usually in those cases the changes will be very easy to see and modify if ever needed. However our team is actively working to make clearer commit messages whenever possible.

## PySoft Q&A:

### Why does the program crash on startup?

This could be for multiple reasons, so first, make sure all dependencies and modules are correctly installed for any and all Python versions that are installed on your computer. You can find the list of modules that you need to install in the PySoft [requirements.txt](https://github.com/T1taniumF0rge/Software/blob/Main/PySoft/requirements.txt) file, and to simplify installation, you can run `pip install -r requirements.txt` and Pip will automatically find the newest version of that module and install it for you [(read the PySoft's README.md for clarifications!)](/PySoft/README.md)

Otherwise the best way to see what error has occured is to open a command-line window (Bash, PowerShell, CMD) and run the script from the terminal, as it will print any errors to the terminal. Then it is highly recommended to consult the [error chart](/PySoft/Errors%20chart.md) for any possible solutions, and then you may open an issue.

### Why are programs mostly all in one and use outdated code writing methods (many elif statements, logic and UI in one program)?

For the longest time, we stuck to our philosophy of 1 file maximum per project, for user convenience as they would only have to download one single file. However, for larger projects that may require multiple files, we have put them in the [Large Projects](/PySoft/Large%20Projects) folder, but to maintain user convenience we bundle all of the files into a zip2exe NSIS installer so that again, the user only has to download and run one file. *In this example, the Large Projects folder happens to be in PySoft, however it can exist in any of the language folders. Check [`programs.md`](/Programs.md) for more information*

### Can I rewrite the programs to have better security (e.g not triggering CodeQL warnings) or better coding structure?

There is a clear difference between a bugfix and rewriting the entire program, and before changing any file in this repository, it is best to consult the [Contributing Guidelines](/CONTRIBUTING.md) first. But as a whole, if you want to rewrite a program that is all in one file and you want to seperate the logic and the UI, you may do it on a [fork](https://github.com/T1taniumF0rge/Software/fork), and if you want to change a small thing in the programs then you have to make sure to keep the program in the same writing style as the original program.

## Windows Loader Q&A:

### What is the point?

Some people don't want to pay Microsoft for a Windows key, and generally except for Office there isn't much use in tools like MAS or DAZ because modern Windows versions have very few limitations if you don't activate Windows. However in older versions like Windows 7 and Vista, tools like DAZ loader are required because otherwise severe restrictions on the computer are applied. Windows 7 is out of support, and Microsoft wants people to get off that OS, so they wouldn't care much if people are pirating Windows 7, especially as if you want to install Windows 7 Ultimate on a computer that originally came with Windows XP Home Edition, then DAZ is the only option (you're not going to pay $120 for an OS that isn't even supported right?). 

> [!CAUTION]
> Only thing is: NEVER PUT THE DAZ LOADER AND THE SOPHOS ENDPOINT AGENT TOGETHER! THEY HAVE GENERATIONAL BEEF!!!

### Are they safe?

Personally, our full team at `Software` have used MAS and DAZ for a long time (2-3 years) and so far we have **never** been hacked or had any sort of computer problems, and for DAZ loader it is especially important since it is hard to find a reliable download link with no viruses, until I found one so I made an installer of it so that now I have a reliable way of downloading DAZ loader to activate my old Windows 7 computer.

> [!IMPORTANT]
>
> The results described above may or may not apply to your hardware, software or environmental (environment in which you use it, such as home, work or IT) configuration, as such you should not interpret these resuls completely literally (rather take it with a grain of salt), but still have re-assurance that the `Software` team doesn't use activation software that's pure malware.

### I got fired from my company from using this!

That's on you mate, if you had any sense of downloading these files through the [Programs.md](/Programs.md) file (or just read the LICENSE or README.md files) then you must have agreed to the terms [here](https://github.com/T1taniumF0rge/Software/blob/Main/InstallerSoft/Windows/Windows%20Loaders/README.md), meaning that we are ***not liable* for *any damages that these programs may have caused*.**

## InstallerSoft Q&A:

### Why are there repackaged NSIS installers of stuff?

The reason why some programs are repackaged in an NSIS installer, is because (to put it simply), some of the software are packaged in horrendous installers (ones that are buggy to hell, ones that don't let you choose the install location, etc) and our team at `Software` does not want our users to suffer. However for such installers, they are *mostly* trustable as we use and package the software in house, and in those cases we provide the source and a *.NSI file so that in case of doubt, you can make the installer yourself and prove that we're not liars. 

### Why are you hoarding old versions of programs?

Whenever there is an old version of a program (360AFChrome for example), there is a reason to keep it. In 360AFChrome, many people use it on computers that are running Windows XP to access the internet, and in other cases like AOMEI 8.7, this version is kept because new AOMEI, just sucks (some free features in version 8.7 are paid features in 10.4.1 such as the Disk Clone feature because of greedy capitalist investors who think they're the only ones on this planet. As I've said with the Roblox corporation in Programs.md and some commit messages, the only thing most (that way I don't anger the 5 nice investors on this planet) investors want is money no matter the consequences. Or if you want a disk manager that has a slightly less polished UI but more features, try DiskGenius.)


