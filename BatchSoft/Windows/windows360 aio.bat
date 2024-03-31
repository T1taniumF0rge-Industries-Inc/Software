@echo off
goto START
:START
cls
color a
title Windows360 AIO
echo Windows360 AIO/All-In-One:
echo V1.26-beta. If action returns to main menu, that means the option is not implemented.
echo (c) GamerSoftware Corporation. All rights reserved.
echo [1] System Infomation.
echo [2] Website Pinger.
echo [3] Quit program.
choice /c:123 /m "Choose an option: "
IF ERRORLEVEL 3 GOTO QUIT
IF ERRORLEVEL 2 GOTO WEBPING
IF ERRORLEVEL 1 GOTO SYSTEMINFO
:SYSTEMINFOS
cls
color a
echo System Informations:
echo.
echo Running whoami...
whoami
pause
echo.
echo Running systeminfo...
systeminfo
pause
echo.
echo Running ipconfig...
ipconfig
pause
echo.
echo Listing directories of %~dp0\...
dir
echo.
echo Displaying user information...
net user
pause
echo.
echo Listing currently running tasks...
tasklist
pause
goto START
:WEBPING
cls
color a
echo Website Pinger:
set input=
set /p input= Enter your website to ping here: 
if %input%==goto A if NOT B
echo Processing your request...
ping %input%
goto START
:QUIT
exit /b
