import tkinter as tk
import random
def shift():
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
	canvas.after(1000//fps,shift)
app=tk.Tk()
app.title('Gliding Text!')
canvas=tk.Canvas(app,bg='black')
canvas.pack(fill=tk.BOTH,expand=1)
colors=('red','orange','yellow','green','blue','magenta','pink','purple')
text_var="Happy New Year 2024! Wish you all happy coding!!"
text=canvas.create_text(0,-2000,text=text_var,font=('Handwriting',20,'bold'),fill='white',tags="marquee",anchor='nw')
x1,y1,x2,y2=canvas.bbox("marquee")
width=x2-x1
height=y2-y1
canvas['width']=width-300
canvas['height']=height+5
canvas.moveto(text,width-300,2)
fps=30
change_color=0
shift()
app.mainloop()
