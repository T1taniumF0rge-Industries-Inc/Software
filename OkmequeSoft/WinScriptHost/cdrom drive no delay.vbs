x = msgbox("Program only works on SlimLine optical drives.",0+0,"Note")
Set TI = CreateObject("WMPlayer.OCX.7" )
Set CDROMCOL = TI.cdromCollection
if CDROMCOL.Count >= 1 then
do
For i = 0 to CDROMCOL.Count - 1
CDROMCOL.Item(i).Eject
Next ' CDTRAY
For i = 0 to CDROMCOL.Count - 1
CDROMCOL.Item(i).Eject
Next ' CDTRAY
loop
End If
