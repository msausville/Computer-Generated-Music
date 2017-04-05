"""Main File for Music Generation
Purpose: Create computer-generated music
Authors: Tatiana Anthony, Allison Basore, Ilya Bescanson,
Hannah Kolano, Meaghen Sausville"""
from tkinter import *
from tkinter import messagebox
from tkinter import font
import mido
from musicreader import play_music

class Note:
    def __init__(self, tone = 60, volume = 60, duration = 0):
        self.tone = tone
        self.duration = duration
        self.volume = volume

class Song:
    def __init__(self, notes_list):
        """creates a song object from a list of notes"""
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)

    def add_to_analysis(self):
        """hey Song, add yourself to the markov dictionary"""
        intervals = self.intervals
        for i in range(len(intervals) - pre_len):
            prefix = tuple(intervals[i:i + pre_len])
            suffix = intervals[i + pre_len]
            m_dict[prefix] = m_dict.get(prefix, tuple()) + (suffix,)


def read_midi(filename):
    mid = mido.MidiFile(filename)
    print(mid)
    list_of_notes = []
    open_notes = []
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        # test_track = track[350]
        # print(track[350])
        for j in range(len(track)):
            msg = track[j]
            print(msg)
            # print(msg.type)
            is_new_note = True
            may_be_note = False
            if msg.type == 'note_on' or msg.type == 'note_off':
                may_be_note = True
            for old_note in open_notes:
                print(is_new_note)
                old_note.duration += msg.time
                if may_be_note:
                    if old_note.tone == msg.note:
                        is_new_note = False
                        if msg.type == 'note_on':
                            if msg.velocity == 0:
                                list_of_notes.append(old_note)
                                open_notes.remove(old_note)
                        elif msg.type == 'note_off':
                            list_of_notes.append(old_note)
                            open_notes.remove(old_note)

            if is_new_note and may_be_note:
                new_note = Note(msg.note, msg.velocity)
                open_notes.append(new_note);
            # try:
            #     nextmsg = track[j+1]
            #     # print(nextmsg.time)
            # except:
            #     pass
    return list_of_notes

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


def con_to_int(note_list):
    """takes a song object and returns a list of note intervals"""
    int_list = [0]
    for i in range(len(note_list)-1):
        int_list.append(note_list[i+1].tone - note_list[i].tone)
    return int_list


def harmony_analysis(notes):
	"""
	Completes a harmony, arragemnet, sectioning analysis and give better sounding song
	input: list of notes
	output: new list of notes
	"""
	pass

def create_markov_chain(mark_dict, len_in_measures=32, pre_len=1):
    """takes a markov dictionary and returns a generated list of note intervals"""
    new_melody = list(random.choice(list(mark_dict.keys())))
    for i in range(len_in_measures - pre_len):
        options = m_dict[tuple(new_melody[i:i+pre_len])]
        next_note = random.choice(options)
        new_melody.append(next_note)
    return new_melody

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
	list_of_songs = filename
    m_dict = dict()
	for song in list_of_songs:
		cleaned = MIDI_clean(filename)
		new_song_con = MIDI_to_song(cleaned)
		NewSong = Song(new_song_con)
		NewSong.add_to_analysis()
        new_intervals = create_markov_chain(m_dict)
	play_song(new_intervals)

if __name__ == "__main__":
    # main('filename')
    play_music()

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
