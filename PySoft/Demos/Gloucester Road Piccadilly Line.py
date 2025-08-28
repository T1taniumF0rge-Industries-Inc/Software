import tkinter as tk
import random
import time
global destination
def shift():
	global destination
	global change_color
	x1,y1,x2,y2=canvas.bbox("marquee")
	if(x2<0):
		x1=canvas.winfo_width()
		y1=canvas.winfo_height()//2
		canvas.coords(text,x1,2)
	else:
		canvas.move(text,-2,0)
		canvas.color=(change_color+1)%25
		if change_color==0:
			canvas.itemconfig(text,fill=random.choice(colors))
	destination = random.choice(destinations)
	#if canvas['width'] != 650-300 or canvas['height'] != height +5:
	canvas.configure(width=650-300, height=height+5)
	canvas.after(1000//fps,shift)
app=tk.Tk()
app.title('Text may take time to appear.')
app.resizable(width=False,height=False)
canvas=tk.Canvas(app,bg='black')
canvas.pack(fill=tk.BOTH,expand=1)
colors=('orange','orange')
destinations = ['Rayners Lane', 'Heathrow Terminal 4 & Terminals 2 and 3', 'Heathrow Terminals 2 and 3 & Terminal 5', "Northfields", "Uxbridge", "Cockfosters", "Arnos Grove"]
destination = random.choice(destinations)
text_var=f"This is Gloucester Road  		   	   Change here for the Circle Line  			    This is a Piccadilly Line service to {random.choice(destinations)}"
text=canvas.create_text(0,-2000,text=text_var,font=('Handwriting',20,'bold', 'italic'),fill='white',tags="marquee",anchor='nw')
x1,y1,x2,y2=canvas.bbox("marquee")
width=x2-x1
height=y2-y1
canvas['width']=620-300
canvas['height']=height+5
canvas.moveto(text,width-300,2)
fps=30
change_color=0
shift()
app.mainloop()
