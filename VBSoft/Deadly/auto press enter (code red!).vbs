msgbox "It's time to enter, shall we..."
Set wshShell = wscript.CreateObject("WScript.Shell")
do
wscript.sleep 50
wshshell.sendkeys "~(enter)"
loop
