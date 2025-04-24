 Set objShell = CreateObject("Wscript.Shell")
dim password
password=InputBox("Please Enter password:3 attempts left:","Log on to Windows")
if password = ("acerm") then
	dim correct
	correct =MsgBox("Correct,logging in...",64,"Log on to Windows")
	objShell.Run("C:\Windows\system32\winver.")
Else
	dim again
	again =MsgBox("The password you entered is not valid",21,"Error")
	If again = 4 Then
	dim password2
	password2=InputBox("Please Enter user name:2 attempts left:","Log on to Windows")
	if password2 = ("acerm") then
		dim correct2
		correct2 =MsgBox("Correct,logging in...",64,"Log on to Windows")
		objShell.Run("C:\Windows\system32\winver.")
	Else
		dim again2
		again2 =MsgBox("The password you entered is not valid",21,"Error")
		If again2 = 4 Then
		dim password3
		password3=InputBox("Please Enter user name:1 attempt left:","Log on to Windows")
		if password3 = ("acerm") then
			dim correct3
			correct3 =MsgBox("Correct,logging in...",64,"Log on to Windows")
			objShell.Run("C:\Windows\system32\winver.")
		Else
			dim again3
			again3 =MsgBox("The password you entered is not valid",21,"Error")
			If again3 = 4 Then
				dim incorect
				incorect =MsgBox("You have done too many attemps.The computer will now turn off",16,"System message")
				objShell.Run("C:\Windows\system32\shutdown.exe /s /t 5")
					end if
				end if
			end if
		end if
	end if
end if
