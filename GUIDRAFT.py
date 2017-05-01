#The GUI draft (COMMENT OUT FOR NOW)
#fonts
from tkinter import *
from tkinter import messagebox
from tkinter import font
#hTimes10 = (family="Times",size=10,weight="bold")

top = Tk()
top.geometry("400x400")

#Function for Commands
def printchoice(e):
	output = E.curselection()
	print(output)

def PlaySong():
	msg = messagebox.showinfo("Song Box", "Playing Song")

#Widgits
E = Listbox(top, selectmode = SINGLE, height = 5, width = 10)
P = Button(top, text = "Play", command = PlaySong, activebackground = "green", height = 5, width = 10)
W = Text(top, width = 60, height = 1, bg = "yellow")
W.insert(INSERT, 'Welcome! Ready to make some music?')

listofsongs = ["Song1", "Song2", "Song3"]
for song in listofsongs:
	E.insert(END, song)

#Packing and Placements
E.place(x=100, y = 100)
E.bind('<<ListboxSelect>>', printchoice)
W.place(x=0, y=10)
P.place(x=100, y = 200)



top.mainloop()
