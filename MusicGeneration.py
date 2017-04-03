"""Main File for Music Gerneation"""
from tkinter import *
from tkinter import messagebox
from tkinter import font




def MIDI_clean(filename):
	"""
	Cleans up the MIDI files
	input: MIDI file name
	output: MIDI information
	"""
	pass

def MIDI_to_song(MIDI_info):
	"""
	Gets the important information from the MIDI file
	input:  MIDI information from function, list of notes
	output: list of notes (and other impmortant parts to make the song?)
	"""
	pass

def concrete_to_intraval(notes):
	"""
	Builds song intervals
	input: list of notes
	output: list of intervals
	"""
	pass

def harmony_analysis(notes):
	"""
	Completes a harmony, arragemnet, sectioning analysis and give better sounding song
	input: list of notes
	output: new list of notes
	"""
	pass


def Markov_dict(multi_song_intervals):
	"""
	Creates markov analysis of many song's intervals
	input: list of intervals
	output: new list of intervals
	"""
	pass

def play_song(song_intervals):
	"""
	Plays the song
	input: list of notes/intervals
	output: *speaker output*
	"""
	pass

def main(filename):
	"""
	Performs Markov analysis on many songs and 
	input: takes an input of all file names 
	output: plays a song 
	"""
	all_intervals = []
	list_of_songs = filename
	for song in list_of_songs:
		cleaned = MIDI_clean(filename)
		new_song = MIDI_to_song(cleaned)
		list_of_intervals = concrete_to_intraval(new_song)
		all_intervals.append(list_of_intervals)
	new_intervals =Markov_dict(all_intervals)
	play_song(new_intervals)

if __name__ == "__main__":
    main('filename')


#The GUI draft (COMMENT OUT FOR NOW)
#fonts
#Times10 = (family="Times",size=10,weight="bold")

# top = Tk()
# top.geometry("400x400")

# #Function for Commands
# def printchoice(e):
# 	output = E.curselection()
# 	print(output)

# def PlaySong():
# 	msg = messagebox.showinfo("Song Box", "Playing Song")

# #Widgits 
# E = Listbox(top, selectmode = SINGLE, height = 5, width = 10)
# P = Button(top, text = "Play", command = PlaySong, activebackground = "green", height = 5, width = 10)
# W = Text(top, width = 60, height = 1, bg = "yellow")
# W.insert(INSERT, 'Welcome! Ready to make some music?')

# listofsongs = ["Song1", "Song2", "Song3"]
# for song in listofsongs:
# 	E.insert(END, song)

# #Packing and Placements
# E.place(x=100, y = 100)
# E.bind('<<ListboxSelect>>', printchoice)
# W.place(x=0, y=10)
# P.place(x=100, y = 200)



# top.mainloop()



