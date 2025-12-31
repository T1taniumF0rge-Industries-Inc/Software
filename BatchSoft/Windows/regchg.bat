@echo off
set RESTARTCOMPUTER=0
setlocal enabledelayedexpansion
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Please wait for admin privileges to be authorised. Admin privileges must be present in order for regchg to run properly.
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit /b
)
:START
cls
title REGISTRY EDITOR IV - Revision G (regchg.bat) - (c) Lan Internet Software
echo *** REGISTRY EDITOR IV - Revision G (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
echo.
echo This program will make it easy for you to disable certain annoying Windows Features by changing certain registry keys (basically small parameters that tell Windows how to function)
echo.
echo In the "Everything" options, all users will have their password expiry disabled.
echo [1] Disable Bing/Internet Start Menu Search Results
echo [2] Enable Verbose Boot Messages - This will make boot messages more precise (read extra informations for clarification)
echo [3] Uninstall Edge
echo [4] Restore Windows 10 style Right-click menu in Windows 11. (read extra informations for clarification)
echo [5] Everything 
echo [6] Everything except Edge Uninstall 
echo [7] Disable Microsoft Copilot (Main Copilot & Data Analysis, read extra informations for clarification)
echo [8] Disable password expiry for all users
echo [9] Disable password expiry for a user
echo [0] Quit Program
echo [M] MAS Windows Activator (Third-party program not made by Lan Internet Software, requires Internet Connection!)
echo [S] Configure Windows Shell
echo [F] Fix Blank Explorer Warning Pop-up on startup
echo [I] Informations about this program and its functions
echo [L] Last Updates/Changelog
echo.
echo Lan Internet Software is NOT responsible for ANY damages that arise from the use of any functions of this program. 
echo If you have any doubts, questions or problems, consult the informations screen first. For example, errors in option 3 may be normal.
echo.
choice /c:1234567890MSFIL /m "Choose an option : "
IF ERRORLEVEL 15 GOTO CHGLOG
IF ERRORLEVEL 14 GOTO INFO
IF ERRORLEVEL 13 GOTO FIX
IF ERRORLEVEL 12 GOTO SHELL
IF ERRORLEVEL 11 GOTO MAS
IF ERRORLEVEL 10 EXIT /B
IF ERRORLEVEL 9 GOTO SINGLEUSER
IF ERRORLEVEL 8 GOTO ALLUSERS
IF ERRORLEVEL 7 GOTO WINDOWSAI
IF ERRORLEVEL 6 GOTO EVERYTHING
IF ERRORLEVEL 5 GOTO AIO
IF ERRORLEVEL 4 GOTO W10
IF ERRORLEVEL 3 GOTO EDGE
IF ERRORLEVEL 2 GOTO VBM
IF ERRORLEVEL 1 GOTO WINSEARCH

:CHGLOG
cls
echo *** REGISTRY EDITOR IV - Revision G (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
echo.
echo ** CHANGELOG **
echo The changelog is a feature added in REGCHG IV Revision G.
echo.
echo Revision F: Add detailed information screen, add the changelog and polish the UI even more to make it super clear to the user.
echo.
echo Revision G: Fix small documentation mistakes and add mention to more advanced Windows AI Remover.
pause
goto START

:INFO
cls
echo *** REGISTRY EDITOR IV - Revision G (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
echo.
echo ** GENERAL DESCRIPTION **
echo This program will make it easy for you to disable certain annoying Windows Features by chainging certain registry keys. Lan Internet Software recommends using this program on brand new Windows Installations, as it will speed up the computer and extend battery life by disabling components that you are probably not going to use.
echo.
echo A registry key is a small piece of data that tells Windows (or a certain program) how to operate. This may include things such as startup files, configuration settings or more. These keys are very versatile for configuring Windows to your liking, however by default, your computer won't ship with REGCHG, and if you wanted to replicate the functions of this program, you'd have to manually search the corresponding keys on the Internet, and change them yourself, which could be potentially risky. This program condenses a lot of registry keys into one program, and has been tested to ensure stability of the operating system.
echo.
echo NOTE: If your computer is owned by an organisation, it is recommended to ask your administrator permission before using REGCHG or ask to do the relevant changes using the Group Policy Editor (gpedit.msc). Lan Internet Software is NOT responsible for ANY damages that arise from the use of any functions of this program.
echo.
echo In this program, REGCHG, regchg.bat and REGISTRY EDITOR all refer to this program.
echo.
pause
echo.
echo ** FUNCTION DESCRIPTIONS **
echo.
echo 1: Disable Bing/Internet Start Menu Search Results
echo By default, Windows 8 and over made it so that whenever you type something in the Windows Search bar, that it will search that term on the Internet using Bing, and return a preview of the results on the Start Menu. While there could be potential uses for this function, most of the time it makes Search slower and imprecise, as well as using more computer resources. This program disables that function, making search more precise and efficient.
echo.
echo Registry Keys:
echo  - HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer\DisableSearchBoxSuggestions
echo  - HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search\BingSearchEnabled
echo.
pause
echo.
echo 2: Enable Verbose Boot Messages
echo By default, Windows does not show "Verbose" (precise) boot messages. The user sees the following examples:
echo  - "Please wait"
echo  - "Restarting"
echo  - "Signing out"
echo However, by enabling Verbose Boot Messages, you replace the above imprecise messages with:
echo  - "Please wait for the User Profile Service"
echo  - "Stopping Service: Windows Update Optimisation"
echo  - "Preparing Windows"
echo If your computer is slower than usual on startup, sign-in, sign-out or shutdown, this allows you to see exactly which part of the process is slowing down the computer, and lets you better research your problem. Even on fast computers, it is useful as Windows Update is sometimes rather sneaky.
echo.
echo Registry Keys:
echo  - HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\VerboseStatus
pause
echo.
echo 3: Uninstall Edge
echo As its name implies, this uninstalls Edge. Why does this option need to be in REGCHG, can't I just use the Uninstaller? Well, Microsoft is greedy for Edge users, and thus is trying to force it down on users (keep in mind they tried something similar in the Windows 95 days by forcing Internet Explorer on install CD-ROMs and got sued). This means that they do not provide an uninstaller for this browser. To remove it, we have to manually force-stop it, and then force-remove its components, which also has the side effect of Windows thinking the application is still installed on the computer. Errors are expected from this function, as it force-removes the components even if they don't exist (which also has the benefit of clearing hidden Edge folders)
echo.
echo This option should only be used if you are certain that no applications that you are using use Microsoft Edge or Microsoft Edge WebView2, as WebView2 relies on Microsoft Edge core. REGCHG will warn you and require confirmation before the deletion can start.
echo.
echo Files Modified:
echo  - Takeown: C:\PROGRA~2\MICROSOFT
echo  - Kill processes: "msedge.exe", "MicrosoftEdgeUpdate.exe", "MSEdgeWebView2.exe"
echo  - Remove directory: C:\PROGRA~2\MICROSOFT
echo  - Delete: %PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk
echo  - Delete: C:\Users\Public\Desktop\Microsoft Edge.lnk
echo  - Delete: %USERPROFILE%\Desktop\Microsoft Edge.lnk
echo  - Delete: C:\Users\Public\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk
echo  - Delete: %USERPROFILE%\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk
echo.
pause
echo.
echo 4: Restore Windows 10 style Right-click menu in Windows 11
echo Windows 11 brought with it radical changes in the UI (User Interface), here being the Windows 11 Right-Click menu. In Windows 11, they simplify the options menu, however essential options such as renaming, deleting, etc are hidden away behing the "More Options" menu. Clicking that button brings the full right-click menu, however to get here requires one extra click which can be unsettling for age-old Windows Users. This programs removes the Windows 11 Right-Click menu and replaces is it with the traditional Windows 10 Right-Click Menu.
echo.
echo Registry Keys:
echo  - HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32
echo.
pause
echo.
echo 5 and 6: Everything Options
echo Both of these options will execute functions 1, 2, 4, 7 and 8, with option 5 only executing option 3. 
echo.
pause
echo.
echo 7: Disable Microsoft Copilot
echo Like Edge, Microsoft is heavily pushing for its "Copilot" AI into Windows. It is already integrated in many parts of the OS as well as the keyboard (the Menu/Right Windows key are replaced by the Copilot key which opens the Copilot app). AI can be useful, it is the entire reason services such as ChatGPT, Grok or whatever you want are so successful. The key difference is that people don't want it all the time, only when they want it which is something that Microsoft refuses to understand. Moreover, Microsoft uses your data to collect information, to feed it back into its AI to "improve" it, and is opt-out by default, meaning that if you don't explicitely refuse it, it will collect your data. This program disables Copilot and Data Analysis, speeding up your computer and giving you more control over your data.
echo.
echo This program only disables the main Copilot app and integrations into the main Windows system. Copilot in Edge, MSPaint and Notepad may still remain. If you want to have more advanced AI removal, Lan Internet Software recommends ZOICWARE's "RemoveWindowsAI" tool (https://github.com/zoicware/RemoveWindowsAI).
echo.
echo Registry Keys:
echo  - HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsCopilot /v TurnOffWindowsCopilot
echo  - HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI /v DisableAIDataAnalysis
echo.
pause
echo.
echo 8 and 9: Disable Password Expiry
echo While password expiry can be a useful feature, especially in the context of your computer containing sensitive data, on your home computer that doesn't contain any sensitive data, it can be annoying to have to change your password every 30 days. Option 8 removes that functionality to all users, while Option 9 lets you disable it for a specific user. Note that it is highly recommended to not use this function if your computer is owned by an organisation or your computer contains sensitive data.
echo.
echo Commands Run:
echo  - powershell /c Set-LocalUser -Name '%username%' -PasswordNeverExpires $true
echo  - powershell /c "Get-LocalUser | Set-LocalUser -PasswordNeverExpires $true"
pause
echo.
echo 0: Quit Program
echo This quits the program.
echo.
pause
echo.
echo M: MAS Windows Activator
echo This is a third party program made by "Massgravel" (https://github.com/massgravel/Microsoft-Activation-Scripts) and is a program that lets you activate Windows for free. It does however require an Internet Connection to function
echo.
echo Lan Internet is not affiliated to Massgravel in any way, shape or form, and therefore cannot provide support for any problems and is not liable for any damages that arise from the use of that third party program. If you encounter any problems with this program, report it to Massgravel's repository. 
echo.
echo If your computer is owned by an organisation and you have Windows Activation problems, avoid using this function and contact your system administrator for support.
echo.
echo Commands Run:
echo  - powershell /c "irm https://get.activated.win | iex"
pause
echo.
echo S: Configure Windows Shell
echo Windows has a registry key to configure the Shell. The Shell, is essentially the user interface, and what you interact with. It loads the desktop, desktop background and taskbar. However, you could change it if you wanted it. The default shell is set to C:\WINDOWS\EXPLORER.EXE. Such uses are:
echo  - Lighter Shell Alternative: for example replacing EXPLORER.EXE with FreeCommander
echo  - POS/Cash Register: for example, your local McDo self-ordering system is simply a Windows computer with a touchscreen and a custom shell
echo.
echo You do have to be careful, as it is a rather important system component. Therefore if you want to change the shell, make sure to specify the full file name path (BAD: "notepad.exe". Better: "C:\WINDOWS\Notepad.exe") and make sure that the file is USABLE (that it can be read and written by the computer and has no permission restrictions)
echo.
echo Registry Keys:
echo  - HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell
echo.
pause
echo.
echo F: Fix Blank Explorer Warning Pop-up on startup
echo Certain programs use a registry key to make it so that they start-up when you start your computer (known as a start-up file). However certain programs are rogue and do not implement their registry keys properly. Windows expects a file to be there but when there is an error, it will display a Warning pop-up with the title being the name of the current shell. This program fixes this behaviour by removing certain start-up registry keys. Note that since the name of this registry key has changed across Windows Versions and REGCHG is designed to operate on the widest range of Windows Versions, you may see errors.
echo.
echo Registry Keys:
echo  - HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load
echo  - HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\Run
pause
echo.
echo I: Informations Screen
echo Displays this screen.
echo.
pause
echo.
echo L: Last Updates/Changelog
echo This displays the latest updates and new features added to REGCHG, that way you can see new functions without having to compare it to an older version of the program.
echo.
pause
echo.
echo ** USAGE OF REGCHG **
echo.
echo For the best experience of REGCHG, simply read everything that is displayed on screen, and in doubt, view the Informations Screen.
echo.
echo To select an option, press any key that is marked in a bracket. For example, if you want to select the following option:
echo [I] View Information Screen
echo You simply press the "I" key on your keyboard. The program will go to its associated function.
echo.
echo If you see "Press any key to continue . . .", you simply press any alphanumerical key on your keyboard (1-9, A-Z) and you will move to the next menu.
echo.
pause
goto START
 

:FIX
echo.
echo NOTE: The fix for this involves deleting a registry key. However since the name of the registry key has changed across Windows Versions, and REGCHG is designed to operate on the widest range of computers, you may see errors. For this function of this program, as long as at least one command completed successfully (or you see "The operation has completed successfully" at least once), this means that the fix has succeeded.
echo If the system says "ERROR: The system was unable to find the specified registry key or value.", it can be safely ignored.
echo.
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows" /v Run /f 
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows" /v Load /f 
echo.
pause
goto END


:SHELL
cls
echo *** REGISTRY EDITOR IV - Revision D (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
echo.
echo [1] Set custom executable for Windows Shell
echo [2] Reset shell to C:\WINDOWS\EXPLORER.EXE
echo [3] Return to Main Menu
echo [4] Display Information Screen
choice /c:12 /m "Choose an option: "
IF ERRORLEVEL 4 GOTO INFO
IF ERRORLEVEL 3 GOTO START
IF ERRORLEVEL 2 GOTO RESETSHELL
IF ERRORLEVEL 1 GOTO SHCONFIG

:RESETSHELL
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\Windows\EXPLORER.EXE" /f
pause
goto END

:SHCONFIG
echo.
echo You may also specify command line arguments for your application when you will log on if your application supports it and if you want. Examples of valid applications and command line arguments:
echo 1: C:\Windows\py.exe C:\\WinAIO\\G-AIO.py
echo 2: C:\WINDOWS\SYSTEM32\CMD.EXE /C pause
echo 3: D:\downloads\idunno.exe --help
echo 4: C:\Windows\Notepad.exe
echo.
echo NOTE: You must specify the FULL FILE PATH to your application and make sure that the file is USABLE (not read/write protected). If you do not respect this rule, Windows will NOT be able to find your application and will display a black screen upon startup (you will have to start the Task Manager and start this program again, and reconfigure it which is doable but annoying so it is best to avoid these troubles now)
echo.
set /p shell=Enter the path to your executable name and any command line arguments: 
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "%shell%" /f
pause
goto END


:MAS
echo.
echo MAS is a third party program made by "Massgravel" (https://github.com/massgravel/Microsoft-Activation-Scripts). MAS will open in a seperate window. Any problems that arise from the use of that program should be reported on Massgravel's repository and not the T1taniumF0rge repository. 
echo.
echo If this program appears frozen after you've exited MAS, hold the CTRL key, then press C (CTRL-C). If it asks "Terminate batch job?", use N. If there is no red text or error messages, this means that the operation was successful!
pause
powershell /c "irm https://get.activated.win | iex"
goto END

:ALLUSERS
echo.
powershell /c "Get-LocalUser | Set-LocalUser -PasswordNeverExpires $true"
echo If there is no red text or error messages, this means that the operation was successful!
pause
goto END

:SINGLEUSER
echo.
set /p username="Enter the name of the user: "
powershell /c Set-LocalUser -Name '%username%' -PasswordNeverExpires $true
echo If there is no red text or error messages, this means that the operation was successful!
pause
goto END


:END
IF !RESTARTCOMPUTER!==1 GOTO ASKRESTART
echo.
choice /m "Exit program?"
IF ERRORLEVEL 2 GOTO START
IF ERRORLEVEL 1 GOTO REALEND

:REALEND
exit /b

:ASKRESTART
echo.            
echo The changes have successfully been made. Your computer must be restarted in order to apply the changes properly. Restart now?
echo If you do NOT want to restart your computer, use N at this prompt and restart explorer manually. This script cannot do that due to the limitations of the batch programming language. If you want to restart your computer, REGCHG will give you 10 seconds after you say "Yes" before the computer will restart, so it is recommended to save all work in any and all open programs.
choice
set RESTARTCOMPUTER=0
IF ERRORLEVEL 2 GOTO END
IF ERRORLEVEL 1 GOTO REBOOT

:REBOOT
shutdown /r /t 10 /c "This computer will reboot in 10 seconds. Make sure to save all of your work. Changes will be applied during the reboot - REGCHG.BAT"

:W10
echo.
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
set RESTARTCOMPUTER=1
pause
goto END

:EVERYTHING
echo.
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableSearchBoxSuggestions /t REG_DWORD /d 1 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /v BingSearchedEnabled /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI /v DisableAIDataAnalysis /d 1 /f
reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsCopilot /v TurnOffWindowsCopilot /d 1 /f
powershell /c "Get-LocalUser | Set-LocalUser -PasswordNeverExpires $true"
taskkill /f /im explorer.exe
timeout /t 2 /nobreak
set RESTARTCOMPUTER=1
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f
pause
goto END

:AIO
echo.
echo WARNING!!! Many applications rely on Microsoft Edge WebView 2 (and thus Microsoft Edge Core). Deleting Microsoft Edge will permanently destroy those functions until Edge is reinstalled. If you used option 5 by accident, use N at the next choice prompt, and then choose option 6.
echo.
echo The way this function works is that since Microsoft provides no uninstaller for Microsoft Edge, we have to manually force-stop it, and then force-remove its components, which also has the side effect of Windows thinking the application is still installed on the computer.
echo.
echo Continue with delete operation?
choice
IF ERRORLEVEL 2 GOTO START
IF ERRORLEVEL 1 GOTO REALAIO

:REALAIO
echo.
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableSearchBoxSuggestions /t REG_DWORD /d 1 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /v BingSearchedEnabled /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI /v DisableAIDataAnalysis /d 1 /f
reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsCopilot /v TurnOffWindowsCopilot /d 1 /f
powershell /c "Get-LocalUser | Set-LocalUser -PasswordNeverExpires $true"
taskkill /f /im explorer.exe
timeout /t 2 /nobreak
set RESTARTCOMPUTER=1
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f
taskkill /f /im msedge.exe
taskkill /f /im MicrosoftEdgeUpdate.exe
::taskkill /f /im msedgewebview2.exe
takeown /f C:\PROGRA~2\Microsoft
::takeown /f C:\PROGRA~2\MicroSoft\EdgeWebView
::takeown /f C:\PROGRA~2\MicroSoft\EdgeWebView\Application
::del /f C:\PROGRA~2\MicroSoft\EdgeWebView\Application
::rd /q /s C:\Progra~2\MicroSoft\EdgeWebView
:: NEVER DELETE WEBVIEW2, MANY APPLICATIONS RELY ON IT
rd /q /s C:\PROGRA~2\Microsoft
del /f "%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
del /f "C:\Users\Public\Desktop\Microsoft Edge.lnk"
del /f "%USERPROFILE%\Desktop\Microsoft Edge.lnk"
del /f "C:\Users\Public\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk"
del /f "%USERPROFILE%\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk"
pause
goto END

:EDGE
echo.
echo WARNING!!! Many applications rely on Microsoft Edge WebView 2 (and thus Microsoft Edge Core). Deleting Microsoft Edge will permanently destroy those functions until Edge is reinstalled.
echo.
echo The way this function works is that since Microsoft provides no uninstaller for Microsoft Edge, we have to manually force-stop it, and then force-remove its components, which also has the side effect of Windows thinking the application is still installed on the computer.
echo.
echo Continue with delete operation?
choice
IF ERRORLEVEL 2 GOTO START
IF ERRORLEVEL 1 GOTO REALEDGE
:REALEDGE
taskkill /f /im msedge.exe
taskkill /f /im MicrosoftEdgeUpdate.exe
taskkill /f /im msedgewebview2.exe
takeown /f C:\PROGRA~2\Microsoft
::takeown /f C:\PROGRA~2\MicroSoft\EdgeWebView
::takeown /f C:\PROGRA~2\MicroSoft\EdgeWebView\Application
::del /f C:\PROGRA~2\MicroSoft\EdgeWebView\Application
::rd /q /s C:\Progra~2\MicroSoft\EdgeWebView
rd /q /s C:\PROGRA~2\Microsoft
del /f "%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
del /f "C:\Users\Public\Desktop\Microsoft Edge.lnk"
del /f "%USERPROFILE%\Desktop\Microsoft Edge.lnk"
del /f "C:\Users\Public\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk"
del /f "%USERPROFILE%\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk"
pause
goto END

:VBM
echo.
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f
pause
goto END

:WINSEARCH
echo.
reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableSearchBoxSuggestions /t REG_DWORD /d 1 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /v BingSearchedEnabled /t REG_DWORD /d 0 /f
taskkill /f /im explorer.exe
timeout /t 2 /nobreak
set RESTARTCOMPUTER=1
pause
goto END

:WINDOWSAI
reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI /v DisableAIDataAnalysis /d 1 /f
reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsCopilot /v TurnOffWindowsCopilot /d 1 /f
pause
goto END



goto START
