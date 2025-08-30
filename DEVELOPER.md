# Developer Troubleshooting Area

This file is only important and applicable to the collaborators and developers of the `Software` repository for *troubleshooting purposes only*. If you are a standard user, this information does not apply and will not serve you anything unless you are using Git actively on this repository.

## Important

.COMING_SOON → *"Use this section to tell developers about important information about this repository"*

## Git LFS Smudge Errors:

While cloning this repository, you may encounter a similar error as the following: 
```sh
$ git clone https://github.com/GamerSoft24/Software.git /c/GitHub
Cloning into 'C:\GitHub'...
remote: Enumerating objects: 10371, done.
remote: Counting objects: 100% (541/541), done.
remote: Compressing objects: 100% (225/225), done.
remote: Total 10371 (delta 467), reused 312 (delta 312), pack-reused 9830 (from 2)
Receiving objects: 100% (10371/10371), 7.06 GiB | 1.10 MiB/s, done.
Resolving deltas: 100% (3595/3595), done.
Updating files: 100% (4515/4515), done.
Downloading InstallerSoft/Windows/Chromium & Supermium/Thorium/thorium_m128installer.exe (297 MB)
Error downloading object: InstallerSoft/Windows/Chromium & Supermium/Thorium/thorium_m128installer.exe (4bd2cc1): Smudge error: Error downloading InstallerSoft/Windows/Chromium & Supermium/Thorium/thoriu
m_m128installer.exe (4bd2cc1c9f695f0cdea23e0d3278490c6e91b5d07b781977f3feb0ed8e5ee878): batch response: This repository exceeded its LFS budget. The account responsible for the budget should increase it
to restore access.

Errors logged to 'C:\GitHub\.git\lfs\logs\20250421T105547.0425862.log'.
Use `git lfs logs last` to view the log.
error: external filter 'git-lfs filter-process' failed
fatal: InstallerSoft/Windows/Chromium & Supermium/Thorium/thorium_m128installer.exe: smudge filter lfs failed
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry with 'git restore --source=HEAD :/'
```

This error is known to happen, and you will have to wait until either the next Git LFS package is paid by the repository owner or the Git LFS budget is reset or disactivated.

## Git Pull Errors:

> [!IMPORTANT]
>
> Before you leave your computer for any reason, make sure to push the last files that you have committed, otherwise you may encounter problems when pulling or pushing new files (git merge problems) and may have to reclone the entire repository again (just hope your suppresion of the file doesnt take ages).
>
> 
## Git LFS file size limitations:

> [!WARNING]
>
> Git LFS limits any individual file to 2GB, and if not respected then will throw error 422 ` [422] Size must be less than or equal to 2147483648
`. This error will not disappear and mess up your pushes and pulls, and re-cloning the Git repository will be required.

## GitHub file size precautions:

> [!CAUTION]
>
> If you try and upload a file that is over 100MB, make sure that the file extension type is correctly set in the .gitattributes file so that Git LFS can recognize the file as an LFS file and add the required pointers to point the file when the repository is getting cloned. Failure to do so will throw an error and usually (not always) mess up the commit history and file headers, and re-cloning the Git repository will potentially be required.
> 

## Windows File Sharing recommendations:

> [!TIP]
>
> While not really repository focused, if you are trying to setup a file share with the sharing machine being a Windows 10 computer, make sure to enable all permissions and disable most security features to ensure compatability and that you create or move the files into the shared directory **AFTER** having shared the folder. Failure to do so will result in other computers throwing permission errors and failure to read the shared folder contents.

## Linux boot failure on G31 (2007) era systems:

Most if all Linux distributions will fail to load a GUI after the initial loading process due to an auto-detection bug that causes wrong graphics parameters to be loaded that older BIOS cannot support. The temporary fix is to go into the boot menu of Linux (should show your distro name and other options) and select the main distro and press E. This will open the options flags. Find the line that starts with `linux` and add to the end of that line `nomodeset acpi=off` which will force super old VESA drivers which are guaranteed to work.

For a permanent solution, it is recommended to find proper video drivers, failing that you could always patch the GRUB bootloader.

## Docker madness:

If you install Docker Desktop on your Windows computer, and you get the error `Virtualization is not detected`, firstly make sure that you are running Windows Pro (and not Home, Enterprise, etc) because some features that Docker needs are blocked/not accessible in Home. Secondly make sure to check if virtualization is enabled (by any means, BIOS check, Task Manager CPU Performance Tab, VMWare with Windows ME, etc). If that's the case then go into `Turn Windows features on or off` by searching that in the start menu. Then enable any option that is Hyper-V and WSL (Windows Subsystem for Linux) as well as enabling Network Discovery in the Network tab in Windows Explorer, and just to make sure you should also enable a telnet client *for that one rogue docker program made in 2002*. After you did that make sure to update WSL to the latest version by doing `wsl --update`, and then you just have to restart the computer and Docker will magically work. (And yes I know I hate docker too)

## Basic Git Guide:

- 1/ Clone this repository to any location using `git clone https://github.com/GamerSoft24/Software.git /c/GitHub` (you can replace `/c/GitHub` with any file path you want so long as it respects the format, which is /a/folder)
- 2/ Do any changes you want so long as it follows the rules previously mentioned (re-cloning will be required if this is not respected)
- 3/ Add the folder or file that you want. If you want to be lazy, you can add the entire folder (so if you changed `/c/GitHub/PySoft/Demos/Code\ Rain.py`, you can simply do `git add /c/GitHub`. Note that it will add any files in any directories starting from the directory that you specified)
- 4/ Commit using a helpful commit message: `git commit -m "Code Rain: made the Code Rain even cooler"`
- 5/ Push. You can do `git push` but I personally like using `git push --all` as it ensures that all files are properly commited to `Main`
