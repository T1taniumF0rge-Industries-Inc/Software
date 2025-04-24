# Frequently Asked Questions (FAQ, NOT DONE YET!)

This document aims to answer some common questions regarding the [`Software`](/) repository.

## Repository Questions:

### Why is there so many things?

The goal of the `Software` repository is that everything is in one centralised area. We cover many topics and languages, such as Python, Batch, C/C++, Visual Basic Script (VBS), HyperText Markup Language (HTML) as well as other formats, such as useful software installers in InstallerSoft, game hacks in HackSoft, movies and music in MovieSoft, Minecraft Modpacks in MinecraftSoft, repository downloads in RepoSoft and useful Office templates in OfficeSoft.

### Why are half the workflows failing?

This is because our workflow configuration hasn't been finished yet, and the best solution is to ignore it.

### Why are there closed security warnings that may matter?

Sometimes, code like this triggers CodeQL's automatic alert system (security management system in this example because you print the `password` variable straight to the terminal):
```
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
However, our team at the `Software` repository have deemed these warnings an exaggeration, as in reality nobody is going to spy on your terminal, and stuff printed to the terminal can be easily deleted by just closing the terminal or clearing it. And for your information, we don't use logs because our programs aren't important enough that logs are required.

### Where do I find the programs?

We have a lot of software available at your disposal for a lot of applications. It would be very inefficient and inconvenient to either navigate through every single binary in releases or have to move repositories just to download a side program that's an add-on to a regular program. So we have created the [program chart](/Programs.md) where you can find all of your required files, properly sorted and sectioned.

### Why does the repository take 36GB of disk space?

We store a lot of binary files using Git LFS, including executables, movies, etc.

## PySoft Questions:

### Why does the program crash on startup?

This could be for multiple reasons, so first, make sure all dependencies and modules are correctly installed for any and all Python versions that are installed on your computer. You can find the list of modules that you need to install in the [PySoft requirements.txt](https://github.com/GamerSoft24/Software/blob/Main/PySoft/requirements.txt) file, and to simplify installation, you can run `pip install -r requirements.txt` and Pip will automatically find the newest version of that module and install it for you.

Otherwise the best way to see what error has occured is to open a command-line window (bash, powershell, cmd) and run the script from the terminal, as it will print any errors to the terminal. Then it is highly recommended to consult the [error chart](/PySoft/Errors%20chart.md) for any possible solutions, and then you may open an issue.

### Why are programs mostly all in one and use outdated code writing methods (many elif statements, logic and UI in one program)?

For the longest time, we stuck to our philosophy of 1 file maximum per project, for user convenience as they would only have to download one single file. However, for larger projects that may require multiple files, we have put them in the [Large Files](/PySoft/Large%20Projects) folder, but to maintain user convenience we bundle all of the files into a ZIP2EXE NSIS installer so that again, the user only has to download and run one file.

### Can I rewrite the programs to have better security (e.g not triggering CodeQL warnings) or better coding structure?

There is a clear difference between a bugfix and rewriting the entire program, and before changing any file in this repository, it is best to consult the [Contributing Guidelines](/CONTRIBUTING.md) first. But as a whole, if you want to rewrite a program that is all in one file and you want to seperate the logic and the UI, you may do it on a [fork](https://github.com/GamerSoft24/Software/fork), and if you want to change a small thing in the programs then you have to make sure to keep the program in the same writing style as the original program.

## InstallerSoft Windows Loader Questions:

### What is the point?

Some people don't want to pay Microsoft for a Windows key, and generally except for Office there isn't much use in tools like MAS or DAZ because modern Windows versions have very few limitations if you don't activate Windows. However in older versions like Windows 7 and Vista, tools like DAZ loader are required because otherwise severe restrictions on the computer are applied. Windows 7 is out of support, and Microsoft wants people to get off that OS, so they wouldn't care much if people are pirating W7, especially as if you want to install Windows 7 Ultimate on a computer that originally came with Windows XP Home Edition, then DAZ is the only option (you're not going to pay $120 for an OS that isn't even supported right?).

### Are they safe?

Personally, our team at Software have used MAS and DAZ for a long time (2-3 years) and so far we have **never** been hacked or had any sort of computer problems, and for DAZ loader it is especially important since it is hard to find a reliable download link with no viruses, until I found one so I made an installer of it so that now I have a reliable way of downloading DAZ loader to activate my old Windows 7 computer.

### I got fired from my company from using this!

That's on you mate, if you had any sense of downloading these files through the program chart (or just read the LICENSE or README files) then you must have agreed to the terms [here](https://github.com/GamerSoft24/Software/blob/Main/InstallerSoft/Windows/Windows%20Loaders/README.md), meaning that we are ***not* liable for any damages that these programs may have caused.**
