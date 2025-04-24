@echo off
goto start
title WinBatch360 AIO Software
:START
cls
echo WinBatch360 AIO Software 
echo Made by GamerSoftware Corp. and Okmeque1 Computers. (c) All rights reserved.
echo Software360 All-in-1 Software at https://github.com/GamerSoft24/Software/tree/main/BatchSoft/Software360.bat
echo V0.86 Final stages. If action returns to main menu, that means the option is not implemented.
echo [1] UAC Bypass
echo [2] Old Browser Loader
echo [3] Make Elevated task
echo [4] Start PROGRAM w/flags (e.g : using --user-data-dir and --disable-certificate-errors when starting BrStd1 Browser)
echo [5] Goto CMD.EXE (Non Elevated)
echo [6] New Browser Loader(Supermium 118 settings.)
echo [7] Change color of Text and Background
echo [8] Quit
choice /c:12345678 /m "Choose an option : "
IF ERRORLEVEL 8 GOTO END
IF ERRORLEVEL 7 GOTO CHANGECOLOR
IF ERRORLEVEL 6 GOTO 360UDATA1
IF ERRORLEVEL 5 GOTO STARTCMD
IF ERRORLEVEL 4 GOTO BRSTD1
IF ERRORLEVEL 3 GOTO SETADMIN
IF ERRORLEVEL 2 GOTO UACBYPASSENCRYPT
IF ERRORLEVEL 1 GOTO UACBYPASS
:UACBYPASS
cls
set /p input="Enter FILE PATH : "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%input%"
echo.
goto START
:UACBYPASSENCRYPT
cls
:Old 360UData1 version
set /p setpath="Enter BROWSER EXE path : "
set /p userdir="Enter USERDATA DIR : "
start "" "%setpath%" --user-data-dir=%userdir% --disable-infobars  --no-sandbox  --ignore-certificate-errors --disable-logging --no-default-browser-check --disable-component-update --disable-background-networking --allow-outdated-plugins --cipher-suite-blacklist=0xe013 --disable-webgl  --js-flags=--noexpose_wasm
echo.
goto START
:SETADMIN
cls
echo.
goto START
:BRSTD1
cls
set /p BR="Enter program with or with no parameters. : "
echo %BR%
start "" %BR%
echo.
goto START
:360UDATA1
cls
set /p setpath="Enter BROWSER EXE path : "
set /p userdir="Enter USERDATA DIR : "
set /p crver="Enter CHROME version(any number from 1-current release) : "
start "" "%setpath%" --user-data-dir="%userdir%" --disable-infobars  --no-sandbox --disable-logging --no-default-browser-check --disable-component-update --disable-background-networking --allow-outdated-plugins --cipher-suite-blacklist=0xcc14,0xe013 --ignore-certificate-errors --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%crver%.0.0.0 Safari/537.36"
echo.
goto start
:STARTCMD
start
goto END
:CHANGECOLOR
cls
color /?
set /p param1="Enter text/background color from the list above(PARAMETER REQUIRED. If you only specify this parameter, the text will change, but if you specify the next parameter, you will change the background) : "
set /p param2="Enter text color from the list above(PARAMETER OPTIONAL, leave blank to not change background. If you specify this parameter, the first parameter will change the background and this parameter will change the color of the text) : "
color %param1%%param2%
goto START
:END
exit /b
