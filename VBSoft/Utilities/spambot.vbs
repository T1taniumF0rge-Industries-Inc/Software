strtext = inputbox ("Write down your message you like to spam") 
strtimes = inputbox ("How many times do you like to spam?") 
strspeed = inputbox ("How fast do you like to spam? (1000 = 1000 per sec, 100 = 10 per secs, etc...)") 
strtimeneed = inputbox ("How many SECONDS do you need to get to your victim's input box?") 
returnvalue=MsgBox ("You agree to the terms of conditions, warranty and liability informations and/or disclaimers of the T1taniumF0rge-Industries-Inc/Software repository as well as acknowledging that the T1taniumF0rge Industries Inc. will NOT be liable for any damages caused by this program?",36) 
If returnvalue=6 Then  
End If 
If not isnumeric (strtimes & strspeed & strtimeneed) then 
msgbox "You entered something else then a number on Times, Speed and/or Time need. shutting down" 
wscript.quit 
End If 
strtimeneed2 = strtimeneed * 1000 
do 
msgbox "You have " & strtimeneed & " seconds to get to your input area where you are going to spam after you click OK." 
wscript.sleep strtimeneed2 
shell.sendkeys ("Spambot activated" & "{enter}") 
for i=0 to strtimes 
shell.sendkeys (strtext & "{enter}") 
wscript.sleep strspeed 
Next 
shell.sendkeys ("Spambot deactivated" & "{enter}") 
wscript.sleep strspeed * strtimes / 10 
returnvalue=MsgBox ("Want to spam again with the same info?",36) 
If returnvalue=6 Then 
Msgbox "Ok Spambot will activate again" 
End If 
If returnvalue=7 Then 
msgbox "Shutting down" 
wscript.quit 
End IF 
loop 
