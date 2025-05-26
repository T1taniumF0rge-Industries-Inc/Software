@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Please wait for admin privileges to be authorized
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit /b
)

echo *** REGISTRY EDITOR (regchg.bat, running w/Admin Permissions) - © Lan Internet Software***
echo This program will make it easy for you to disable certain annoying Windows Features.
echo WARNING! The uninstall Edge feature is completely functional but may throw errors due to the way the program deletes it. This program deletes Edge by forcibly removing all Edge-related functions, even if they don't exist.
echo For users that use applications that rely on Microsoft Edge WebView2, it is highly recommended that you do not uninstall Microsoft Edge as applications that rely on WebView2 also rely on core functions of Microsoft Edge.
echo [1] Disable Start Menu Search Results - Will make it easier to find what you want
echo [2] Enable Verbose Boot Messages - This will make the messages upon startup, login and shutdown. Useful for slow PC
echo [3] Uninstall Edge
echo [4] Restore Windows 10 style Right-click menu - Useful for long-time Windows users.
echo [5] Everything
echo [6] Quit to Windows
choice /c:123456 /m "Choose an option : "
IF ERRORLEVEL 6 GOTO END
IF ERRORLEVEL 5 GOTO AIO
IF ERRORLEVEL 4 GOTO W10
IF ERRORLEVEL 3 GOTO EDGE
IF ERRORLEVEL 2 GOTO VBM
IF ERRORLEVEL 1 GOTO WINSEARCH
:END
exit
:W10
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
pause
goto END
:AIO
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableSearchBoxSuggestions /t REG_DWORD /d 1 /f
taskkill /f /im explorer.exe
timeout /t 2 /nobreak
explorer
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
taskkill /f /im explorer.exe
timeout /t 2 /nobreak
explorer
pause
goto END
