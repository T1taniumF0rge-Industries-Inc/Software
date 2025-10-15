@echo off
color 02

:loop
set /p comp=What's the computer called? You will be punished if you get it wrong!
if /I NOT "%comp%"=="computer" (
    start www.google.com
    goto loop
) else (
    echo Correct answer!
    pause
)
