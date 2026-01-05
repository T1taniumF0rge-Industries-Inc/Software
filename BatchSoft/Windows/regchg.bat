@echo off
:: This project will probably turn into a giant (but useful) monolith batch file
set RESTARTCOMPUTER=
set WINVER= *** PLEASE CONFIGURE YOUR WINDOWS VERSION USING OPTION 5 ***
set CONFIGURED=0
setlocal enabledelayedexpansion
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Please wait for admin privileges to be authorised. Admin privileges must be present in order for regchg to run properly.
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit /b
)
:START
cls
title REGISTRY EDITOR V (regchg.bat) - (c) Lan Internet Software
echo *** REGISTRY EDITOR V (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
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
echo [7] Disable Microsoft Copilot (Main Copilot and Data Analysis, read extra informations for clarification)
echo [8] Disable password expiry for all users
echo [9] Disable password expiry for a user
echo [0] Quit Program
echo [M] MAS Windows Activator (Third-party program not made by Lan Internet Software, requires Internet Connection!)
echo [S] Configure Windows Shell
echo [F] Fix Blank Explorer Warning Pop-up on startup
echo [I] Informations about this program and its functions
echo [L] Last Updates/Changelog
echo [E] Explorer Utilities
echo.
echo Lan Internet Software is NOT responsible for ANY damages that arise from the use of any functions of this program. 
echo If you have any concerns of system instability, you should backup the registry.
echo If you have any doubts, questions or problems, consult the informations screen first. For example, errors in option 3 may be normal.
echo.
choice /c:1234567890MSFILE /m "Choose an option : "
IF ERRORLEVEL 16 GOTO UTILS
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

:UTILS
cls 
set RESTARTCOMPUTER=1
echo *** REGISTRY EDITOR V (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
echo.
echo Windows Explorer Utilities
echo.
echo Current Windows Version: %WINVER%
echo.
echo [1] Add all folders (Documents, Pictures, etc) to Navigation Pane (left sidebar)
echo [2] Remove all folders (Documents, Pictures, etc) to Navigation Pane (left sidebar)
echo [3] Add individual folders (Documents, Pictures, etc) to Navigation Pane (left sidebar)
echo [4] Remove individual folders (Documents, Pictures, etc) to Navigation Pane (left sidebar)
echo [5] Set Windows Version ( *** IMPORTANT *** )
echo [6] Exit Windows Explorer Utilities
echo [7] Display Explorer Utilities Information Screen (Troubleshooting Steps Here)
choice /c:1234567 /m "Choose an option. Remember to use Option 5 to configure your Windows Version: "
IF ERRORLEVEL 7 GOTO UTILINFO
IF ERRORLEVEL 6 GOTO END
IF ERRORLEVEL 5 GOTO WINCONFIG
IF ERRORLEVEL 4 GOTO INDRMV
IF ERRORLEVEL 3 GOTO INDADD
IF ERRORLEVEL 2 GOTO ALLRMV
IF ERRORLEVEL 1 GOTO ALLADD

:INDRMV
IF %CONFIGURED% EQU 0 goto WINCONFIG
echo.
echo [1] 3D Objects
echo [2] Desktop
echo [3] Documents
echo [4] Music
echo [5] Pictures
echo [6] Videos
echo [7] Downloads
echo [8] Return to Utilities Menu
choice /c:12345678 /m "Choose a folder to remove: "
IF ERRORLEVEL 8 GOTO UTILS
IF ERRORLEVEL 7 IF %WINVER% GEQ 11 GOTO W11RMVDOWN
IF ERRORLEVEL 7 IF %WINVER% LEQ 10 GOTO W10RMVDOWN
IF ERRORLEVEL 6 IF %WINVER% GEQ 11 GOTO W11RMVVIDS
IF ERRORLEVEL 6 IF %WINVER% LEQ 10 GOTO W10RMVVIDS
IF ERRORLEVEL 5 IF %WINVER% GEQ 11 GOTO W11RMVPICS
IF ERRORLEVEL 5 IF %WINVER% LEQ 10 GOTO W10RMVPICS
IF ERRORLEVEL 4 IF %WINVER% GEQ 11 GOTO W11RMVMUS
IF ERRORLEVEL 4 IF %WINVER% LEQ 10 GOTO W10RMVMUS
IF ERRORLEVEL 3 IF %WINVER% GEQ 11 GOTO W11RMVDOCS
IF ERRORLEVEL 3 IF %WINVER% LEQ 10 GOTO W10RMVDOCS
IF ERRORLEVEL 2 IF %WINVER% GEQ 11 GOTO W11RMVMUS
IF ERRORLEVEL 2 IF %WINVER% LEQ 10 GOTO W10RMVMUS
IF ERRORLEVEL 1 IF %WINVER% GEQ 11 GOTO W11RMV3DOBJ
IF ERRORLEVEL 1 IF %WINVER% LEQ 10 GOTO W10RMV3DOBJ

:INDADD
IF %CONFIGURED% EQU 0 goto WINCONFIG
echo.
echo [1] 3D Objects
echo [2] Desktop
echo [3] Documents
echo [4] Music
echo [5] Pictures
echo [6] Videos
echo [7] Downloads
echo [8] Return to Utilities Menu
choice /c:12345678 /m "Choose a folder to add: "
IF ERRORLEVEL 8 GOTO UTILS
IF ERRORLEVEL 7 IF %WINVER% GEQ 11 GOTO W11ADDDOWN
IF ERRORLEVEL 7 IF %WINVER% LEQ 10 GOTO W10ADDDOWN
IF ERRORLEVEL 6 IF %WINVER% GEQ 11 GOTO W11ADDVIDS
IF ERRORLEVEL 6 IF %WINVER% LEQ 10 GOTO W10ADDVIDS
IF ERRORLEVEL 5 IF %WINVER% GEQ 11 GOTO W11ADDPICS
IF ERRORLEVEL 5 IF %WINVER% LEQ 10 GOTO W10ADDPICS
IF ERRORLEVEL 4 IF %WINVER% GEQ 11 GOTO W11ADDMUS
IF ERRORLEVEL 4 IF %WINVER% LEQ 10 GOTO W10ADDMUS
IF ERRORLEVEL 3 IF %WINVER% GEQ 11 GOTO W11ADDDOCS
IF ERRORLEVEL 3 IF %WINVER% LEQ 10 GOTO W10ADDDOCS
IF ERRORLEVEL 2 IF %WINVER% GEQ 11 GOTO W11ADDMUS
IF ERRORLEVEL 2 IF %WINVER% LEQ 10 GOTO W10ADDMUS
IF ERRORLEVEL 1 IF %WINVER% GEQ 11 GOTO W11ADD3DOBJ
IF ERRORLEVEL 1 IF %WINVER% LEQ 10 GOTO W10ADD3DOBJ


:ALLADD
IF %CONFIGURED% EQU 0 goto WINCONFIG
IF %WINVER% GEQ 11 GOTO ADDALL11
IF %WINVER% LEQ 10 GOTO ADDALL10

:ADDALL11
::W11ADD3DOBJ
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
::W11ADDDKST
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HideIfEnabled /t REG_NONE /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
::W11ADDDOCS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HideIfEnabled /t REG_NONE /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
::W11ADDDOWN
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HideIfEnabled /t REG_NONE /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
::W11ADDMUS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HideIfEnabled /t REG_NONE /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
::W11ADDPICS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HideIfEnabled /t REG_NONE /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
::W11ADDVIDS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HideIfEnabled /t REG_NONE /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HiddenByDefault /t REG_DWORD /d 0x00000000 /f
pause
goto UTILS 

:ADDALL10
::W10ADD3DOBJ
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
::W10ADDDKST
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
::W10ADDDOCS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
::W10ADDDOWN
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
::W10ADDMUS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
::W10ADDPICS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
::W10ADDVIDS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
pause
goto UTILS 

:ALLRMV
IF %CONFIGURED% EQU 0 goto WINCONFIG
IF %WINVER% GEQ 11 GOTO RMVALL11
IF %WINVER% LEQ 10 GOTO RMVALL10

:RMVALL11
::W11RMV3DOBJ
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
::W11RMVDKST
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HideIfEnabled /t REG_DWORD /d 0x022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
::W11RMVDOCS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HideIfEnabled /t REG_DWORD /d 0x022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
::W11RMVDOWN
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HideIfEnabled /t REG_DWORD /d 0x022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
::W11RMVMUS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HideIfEnabled /t REG_DWORD /d 0x022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
::W11RMVPICS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HideIfEnabled /t REG_DWORD /d 0x022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
::W11RMVVIDS
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HideIfEnabled /t REG_DWORD /d 0x022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HiddenByDefault /t REG_DWORD /d 0x00000001 /f
pause
goto UTILS 

:RMVALL10
::W10RMV3DOBJ
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
::W10RMVDKST
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
::W10RMVDOCS
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
::W10RMVDOWN
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
::W10RMVMUS
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
::W10RMVPICS
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
::W10RMVVIDS
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
pause
goto UTILS 

:: WIN10 Folder Removals

:W10RMV3DOBJ
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
echo.
pause
goto INDRMV
:W10RMVDKST
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
echo.
pause
goto INDRMV
:W10RMVDOCS
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
echo.
pause
goto INDRMV
:W10RMVDOWN
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
echo.
pause
goto INDRMV
:W10RMVMUS
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
echo.
pause
goto INDRMV
:W10RMVPICS
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
echo.
pause
goto INDRMV
:W10RMVVIDS
echo Using the WindowsStd Version
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
echo.
pause
goto INDRMV

::Win10 Folder Adds

:W10ADD3DOBJ
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
echo.
pause
goto INDADD
:W10ADDDKST
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /f
echo.
pause
goto INDADD
:W10ADDDOCS
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /f
echo.
pause
goto INDADD
:W10ADDDOWN
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /f
echo.
pause
goto INDADD
:W10ADDMUS
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /f
echo.
pause
goto INDADD
:W10ADDPICS
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /f
echo.
pause
goto INDADD
:W10ADDVIDS
echo Using the WindowsStd Version
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /f
echo.
pause
goto INDADD

:: Win11 Folder remove

:W11RMV3DOBJ
echo Using the Windows 11+ Version...
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
echo.
pause
goto INDRMV
:W11RMVDKST
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HideIfEnabled /t REG_DWORD /v 022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
echo.
pause
goto INDRMV
:W11RMVDOCS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HideIfEnabled /t REG_DWORD /v 022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
echo.
pause
goto INDRMV
:W11RMVDOWN
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HideIfEnabled /t REG_DWORD /v 022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
echo.
pause
goto INDRMV
:W11RMVMUS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HideIfEnabled /t REG_DWORD /v 022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
echo.
pause
goto INDRMV
:W11RMVPICS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HideIfEnabled /t REG_DWORD /v 022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
echo.
pause
goto INDRMV
:W11RMVVIDS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HideIfEnabled /t REG_DWORD /v 022ab9b9 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HiddenByDefault /t REG_DWORD /v 00000001 /f
echo.
pause
goto INDRMV

:: Win11 Folder add
:W11ADD3DOBJ
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}" /f
echo.
pause
goto INDADD
:W11ADDDKST
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HideIfEnabled /t REG_DWORD /ve /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
echo.
pause
goto INDADD
:W11ADDDOCS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HideIfEnabled /t REG_DWORD /ve /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
echo.
pause
goto INDADD
:W11ADDDOWN
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HideIfEnabled /t REG_DWORD /ve /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
echo.
pause
goto INDADD
:W11ADDMUS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HideIfEnabled /t REG_DWORD /ve /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
echo.
pause
goto INDADD
:W11ADDPICS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HideIfEnabled /t REG_DWORD /ve /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
echo.
pause
goto INDADD
:W11ADDVIDS
echo Using the Windows 11+ Version...
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HideIfEnabled /t REG_DWORD /ve /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}" /v HiddenByDefault /t REG_DWORD /v 00000000 /f
echo.
pause
goto INDADD


:UTILINFO
echo.
echo The "Windows Explorer Utilities" allow you to configure Windows Explorer in the way you want, as most of the options either require you digging through option menus or editing the registry.
echo IMPORTANT: It is important that you use Option 5 to set your Windows version correctly (7, 8, 10, 11, etc)
echo Options 1-4 (add/remove folder) rely on the following registry keys:
echo HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{CORRESPONDING_FOLDER_GUID}
echo HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{CORRESPONDING_FOLDER_GUID}
echo "HideIfEnabled"=dword:{corresponding values} in the same registry keys (if using Windows 11)
echo.
echo ** TROUBLESHOOTING **
echo Functions 1-4: If they do not appear to change anything, firstly make sure your Windows Version is set correctly as this tells REGCHG which registry keys are being used. Secondly you may try different Windows versions: some old Windows 11 builds use the old Windows 10 registry keys (may be more common on NTDEV Tiny builds). Lastly other settings may be conflicting with REGCHG, not allowing it to do the proper changes
echo.
echo ** NOTES**
echo For some reason, even though the code is all correct, options 3 and options 4 are swapped however I'm not changing the UI because it may be correct on other builds. My test was using a Tiny10 build but they're kind of horrible for hacks like these. Options 1 and 2 are confirmed working.
pause
goto UTILS

:WINCONFIG
echo.
IF %CONFIGURED% EQU 0 echo Please configure your Windows Version to proceed.
echo IMPORTANT: It is important that the version number you enter is corresponding to your current Windows version, as different registry keys are used on different Windows versions. Entering the wrong version will cause the wrong registry keys to be applied, which could cause serious system errors!
echo.
set /p WINVER="Enter your simple Windows version (10, 11, 7, etc): "
set CONFIGURED=1 
echo.
pause
goto UTILS



:CHGLOG
cls
echo *** REGISTRY EDITOR V (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
echo.
echo ** CHANGELOG **
echo The changelog is a feature added in REGCHG IV Revision G.
echo.
echo Revision F: Add detailed information screen, add the changelog and polish the UI even more to make it super clear to the user.
echo.
echo Revision G: Fix small documentation mistakes and add mention to more advanced Windows AI Remover.
echo.
echo REGCHG V: Explorer Features addition.
pause
goto START

:INFO
cls
echo *** REGISTRY EDITOR V (regchg.bat, running w/Admin Permissions) - (c) Lan Internet Software ***
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
echo E: Explorer Utilities
echo Refer to the information screen in that menu for more information as it contains many utilities.
echo.
pause
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
echo Windows Shell Utilities
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
echo MAS is a third party program made by "Massgravel" (https://github.com/massgravel/Microsoft-Activation-Scripts). MAS will open in a seperate window. Any problems that arise from the use of that program should be reported on Massgravel's repository and not the T1taniumF0rge-Industries or Lan Internet repository. 
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
