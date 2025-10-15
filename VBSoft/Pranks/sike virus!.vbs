Msgbox "Your computer has been infected by a virus",16,"Critical Warning!"
dim x,yes,no
x=Msgbox("The virus has infected drive (C:). Deletion of the virus will require full formatting of drive (C:). Would you like to format drive (C:) ?",52,"Critical Warning!")
if x=6 then
dim box
box=Msgbox("Hard drive (C:) formatting complete. In order to function correctly your computer must restart, would you like to restart now ?",36,"Success!")
if box=6 then
Msgbox "Fatal error, code 08x48631643.B-7",16,"Error"
Msgbox "Just kidding, this was all a joke, but i did scare you didn't I ? Héhé...",64,"Sike!"
end if
if box=7 then
Msgbox "Fatal error, code 08x48631643.B-7",16,"Error"
Msgbox "Just kidding, this was all a joke, but i did scare you didn't I ? Héhé...",64,"Sike!"
end if
end if
if x=7 then
Msgbox "Fatal error, code 08x48631643.B-7",16,"Error"
Msgbox "Just kidding, this was all a joke, but i did scare you didn't I ? Héhé...",64,"Sike!"
end if
