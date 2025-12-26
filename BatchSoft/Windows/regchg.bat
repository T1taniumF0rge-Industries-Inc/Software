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
echo *** REGISTRY EDITOR IV - Revision E (regchg.bat, running w/Admin Permissions) - © Lan Internet Software ***
echo.
echo.
echo This program will make it easy for you to disable certain annoying Windows Features by changing certain registry keys (basically small parameters that tell Windows how to function)
echo.
echo. NOTE: It is required to restart your computer so that the changes are applied properly after using any option of this script
echo.
echo In the Everything options, all users will have their password expiry disabled.
echo [1] Disable Start Menu Search Results - Will make it easier to find what you want
echo [2] Enable Verbose Boot Messages - This will make the messages upon startup, login and shutdown. Useful for slow PC
echo [3] Uninstall Edge
echo [4] Restore Windows 10 style Right-click menu - Useful for long-time Windows users.
echo [5] Everything 
echo [6] Everything except Edge Uninstall 
echo [7] Disable Microsoft Copilot
echo [8] Disable password expiry for all users
echo [9] Disable password expiry for a user
echo [0] Quit Program
echo [M] MAS Windows Activator (requires Internet Connection!)
echo [S] Configure Windows Shell
echo [F] Fix Blank Explorer Warning Pop-up on startup
echo.
echo Lan Internet Software is NOT responsible for ANY damages that arise from the use of any functions of this program.
echo.
choice /c:1234567890MSF /m "Choose an option : "
IF ERRORLEVEL 13 GOTO FIX
IF ERRORLEVEL 12 GOTO SHELL
IF ERRORLEVEL 11 GOTO MAS
IF ERRORLEVEL 10 GOTO END
IF ERRORLEVEL 9 GOTO SINGLEUSER
IF ERRORLEVEL 8 GOTO ALLUSERS
IF ERRORLEVEL 7 GOTO WINDOWSAI
IF ERRORLEVEL 6 GOTO EVERYTHING
IF ERRORLEVEL 5 GOTO AIO
IF ERRORLEVEL 4 GOTO W10
IF ERRORLEVEL 3 GOTO EDGE
IF ERRORLEVEL 2 GOTO VBM
IF ERRORLEVEL 1 GOTO WINSEARCH

:FIX
echo.
echo The way this function of this program works is that certain programs add a rogue registry key that causes Windows to think it has to load a startup file when it does not, however since the program in question didn't implement their files correctly, it causes Wwindows to display a blank error box on startup. This program will fix this annoying behaviour.
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
echo *** REGISTRY EDITOR IV - Revision D (regchg.bat, running w/Admin Permissions) - © Lan Internet Software ***
echo.
echo The method in which this part of this program functions is that when your Windows PC starts up, it checks a registry key to determine what will be the default shell (in this case EXPLORER.EXE). The shell is what you'll interact with after you've logged on. Some people replace the shell with more lightweight options (such as FreeCommander) or replace it with a completely different thing (such as a cash register/POS program. If you go to your local McDo, it's just regular Windows computers but with a custom shell)
echo.
echo [1] Set custom executable for Windows Shell
echo [2] Reset shell to C:\WINDOWS\EXPLORER.EXE
choice /c:12 /m "Choose an option: "
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
powershell /c "Get-LocalUser | Set-LocalUser -PasswordNeverExpires $true"
echo If there is no red text or error messages, this means that the operation was successful!
pause
goto END

:SINGLEUSER
set /p username="Enter the name of the user: "
powershell /c Set-LocalUser -Name '%username%' -PasswordNeverExpires $true
echo If there is no red text or error messages, this means that the operation was successful!
pause
goto END


:END
IF !RESTARTCOMPUTER!==1 GOTO ASKRESTART
echo.
echo Exit?
choice
IF ERRORLEVEL 2 GOTO START
IF ERRORLEVEL 1 GOTO REALEND

:REALEND
exit /b

:ASKRESTART
echo.
echo The changes have successfully been made. Your computer must be restarted in order to apply the changes properly. Restart?
echo If you do NOT want to restart your computer, use N at this prompt and restart explorer manually. This script cannot do that due to the limitations of the batch programming language.
choice
set RESTARTCOMPUTER=0
IF ERRORLEVEL 2 GOTO END
IF ERRORLEVEL 1 GOTO REBOOT

:REBOOT
shutdown /r /t 10 /c "This computer will reboot in 10 seconds. Make sure to save all of your work. Changes will be applied during the reboot - REGCHG.BAT"

:W10
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
set RESTARTCOMPUTER=1
pause
goto END

:EVERYTHING
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
:READLEDGE
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
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f
pause
goto END

:WINSEARCH
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
