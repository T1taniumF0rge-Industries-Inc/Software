# Developer Area

This file is only important and applicable to the collaborators and developers of the `Software` repository. If you are a standard user, this information does not apply and will not serve you anything

## Important

.COMING_SOON → *"Use this section to tell developers about important information about this repository"*

## Git LFS Smudge Errors:

While cloning this repository, you may encounter a similar error as the following: 
```
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

> [!WARNING]
>
> If you try and upload a file that is over 100MB, make sure that the file extension type is correctly set in the .gitattributes file so that Git LFS can recognize the file as an LFS file and add the required pointers to point the file when the repository is getting cloned. Failure to do so will throw an error and usually (not always) mess up the commit history and file headers, and re-cloning the Git repository will potentially be required.
> 

