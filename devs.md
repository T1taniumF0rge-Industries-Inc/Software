# Developer Area

This file is only important and applicable to the collaborators and developers of the `Software` repository. If you are a standard user, this information does not apply and will not serve you anything

## IMPORTANT 

Use this section to tell developers about important information about this repository.

## Git Pull Errors:

> [!IMPORTANT]
>
> Before you leave your computer for any reason, make sure to push the last files that you have committed, otherwise you may encounter problems when pulling or pushing new files.
>
> 
## Git LFS file size limitations:

> [!WARNING]
>
> Git LFS limits any individual file to 2GB, and if not respected then will throw error ` [422] Size must be less than or equal to 2147483648
`. This error will not disappear and mess up your pushes and pulls, and re-cloning the Git repository will be required.

## GitHub file size precautions:

> [!WARNING]
>
> If you try and upload a file that is over 100MB, make sure that the file extension type is correctly set in the .gitattributes file so that Git LFS can recognize the file as an LFS file and add the required pointers to point the file when the repository is getting cloned. Failure to do so will throw an error and usually (not always) mess up the commit history and file headers, and re-cloning the Git repository will potentially be required.
> 
## Last Pull/Clone & Last Push:

### Last Pull/Clone:

| Order | Date & Time      | Computer name |
|-------|------------------|---------------|
| 1     | 21/04/2025 08:51 | COMPBC2       |
| 2     | Not Available    | Not Available |
| 3     | Not Available    | Not Available |

### Last Push:

| Order | Date & Time      | Computer name |
|-------|------------------|---------------|
| 1     | Not Available    | Not Available |
| 2     | Not Available    | Not Available |
| 3     | Not Available    | Not Available |

### Formats:

 - Order Number. The closer the backup number is to 1, the newer
 - Date in DD/MM/YYYY format (the standard EU format, and the most used)
 - Time (if applicable, say you did git clone on 2 computers on the same day
 - PC Name (can be the owner + type of device or the computer name, e.g COMPBC2)
 - Drive path (if applicable, say you put it on a USB or something)
