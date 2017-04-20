"""Main File for Music Generation
Purpose: Create computer-generated music
Authors: Tatiana Anthony, Allison Basore, Ilya Besancon,
Hannah Kolano, Meaghen Sausville"""
# from tkinter import *
# from tkinter import messagebox
# from tkinter import font
import mido
from musicreader import play_music, Note
import random

# class Note:
#     def __init__(self, tone = 60, volume = 60, duration = 0):
#         self.tone = tone
#         self.duration = duration
#         self.volume = volume

# class Note:
#     def __init__(self, tone=60, duration=1, volume=60):
#         """initializes a note object"""
#         self.tone = tone
#         self.duration = duration
#         self.volume = volume



class Song:
    def __init__(self, notes_list):
        """creates a song object from a list of notes"""
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)

    def add_to_analysis(self, an_dict, pre_len=1):
        """hey Song, add yourself to the markov dictionary"""
        intervals = self.intervals
        for i in range(len(intervals) - pre_len):
            prefix = tuple(intervals[i:i + pre_len])
            suffix = intervals[i + pre_len]
            an_dict[prefix] = an_dict.get(prefix, tuple()) + (suffix,)


def check_for_lyrics(single_track):
    num_chnl = {}
    maxItemCount = 0
    lyric_channel = -1
    for j in range(len(single_track)-1):
        msg = single_track[j]
        nextmsg = single_track[j+1]
        if msg.type == 'lyrics' :
            if nextmsg.type == 'note_on':
                num_chnl[nextmsg.channel] =1+ num_chnl.get(nextmsg.channel, 0)
                if num_chnl[nextmsg.channel] > maxItemCount:
                    maxItemCount = num_chnl[nextmsg.channel]
                    lyric_channel = nextmsg.channel
                    print(lyric_channel)
    return lyric_channel

def track_to_list(track):
    list_of_notes = []
    open_notes = []
    melody_channel = check_for_lyrics(track)
    for j in range(len(track)):
        msg = track[j]
        if msg.type in ['lyrics'] :
            print(msg)
        # print(msg.type)
        is_new_note = True
        may_be_note = False
        if msg.type == 'note_on' or msg.type == 'note_off':
            if msg.channel == melody_channel or melody_channel == -1:
                may_be_note = True
                print(msg)
        for old_note in open_notes:
            # print(is_new_note)
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
    return list_of_notes
    
def read_midi(filename):
    mid = mido.MidiFile(filename)
    # print(mid)
    
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        melody_channel = check_for_lyrics(track)
        # test_track = track[350]
        # print(track[350])
        list_of_notes = track_to_list(track)
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
    """takes a list of note objects and returns a list of note intervals"""
    int_list = []
    for i in range(len(note_list)-1):
        int_list.append(note_list[i+1].tone - note_list[i].tone)
    return int_list


def bassline(startnote, b_length):
    """
    input: startnote, length of each note
    Creates a bassline and outputs as list of note objects.
    """
    # list of possible notes
    use_scale = poss_notes(startnote, 'minor')
    # drops it down an octave
    octave_scale = [note - 12 for note in use_scale]
    print('octaved scale: ', octave_scale)
    total_notes = len(octave_scale)
    bassline_notes = [Note(startnote, b_length)]
    for i in range(total_notes//b_length):
        bassline_notes.append(Note(
            random.choice(octave_scale[0:16]), b_length))
    return bassline_notes
    # a = bassline(57, 4)
    # b = [note.tone for note in a]
    # print('notes in bassline: ', b)


def harmony_analysis(notes, startnote):
    """
    Sections and produces better sounding song
    input: list of notes
    output: new list of notes
    """
    pass


def create_markov_chain(mark_dict, start_note=60, len_in_beats=32, pre_len=1):
    """takes a markov dict; returns a markov'd list of note objects"""
    possible_notes = poss_notes(start_note, 'major')
    new_melody = [Note(start_note)]
    new_intervals = [0]
    for i in range(len_in_beats - pre_len):
        next_note = -1
        options = mark_dict[new_intervals[i], ]
        while next_note not in possible_notes:
            next_interval = random.choice(options)
            next_note = new_melody[i].tone + next_interval
        new_melody.append(Note(next_note))
        new_intervals.append(next_interval)
    return new_melody


def poss_notes(start_note, key_in='major'):
    '''takes a starting note; returns list of possible notes in major or minor key of that note'''
    if key_in == 'major':
        intervals = [2, 2, 1, 2, 2, 2, 1]
    elif key_in == 'minor':
        intervals = [2, 1, 2, 2, 1, 2, 2]
    while start_note >= 36:
        start_note += -12
    possible_notes = [start_note]
    counter = 0
    for i in range(6):
        for interval in intervals:
            new_note = possible_notes[counter] + interval
            possible_notes.append(new_note)
            counter += 1
    return possible_notes


def main(filename):

    """
    Performs Markov analysis on many songs and
    input: takes an input of all file names
    output: plays a song
    """

    if type(filename) == 'list':
        list_of_songs = filename
    else:
        list_of_songs = [filename]
        m_dict = dict()
    for song in list_of_songs:
        # cleaned = MIDI_clean(song)
        # new_song_con = MIDI_to_song(cleaned)
        new_song_con = read_midi(filename)
        NewSong = Song(new_song_con)
        NewSong.add_to_analysis(m_dict)

        new_intervals = create_markov_chain(m_dict, 60)
        # new_intervals = NewSong.intervals
        print(type(new_intervals))
        print(new_intervals)
    play_music(new_intervals)

if __name__ == "__main__":

    # play_music()
    
    # mid = mido.MidiFile('UpAllNight.mid')
    # for i, track in enumerate(mid.tracks):
    #     print('Track {}: {}'.format(i, track.name))
    #     check_for_lyrics(track)

    main('TwinkleTwinkleLittleStar.mid')
    # main('TwinkleTwinkleLittleStar.mid, WhatMakesYouBeautiful.mid')
    # play_music()


#The GUI draft (COMMENT OUT FOR NOW)
#fonts
#Times10 = (family="Times",size=10,weight="bold")

# top = Tk()
# top.geometry("400x400")

# #Function for Commands
# def printchoice(e):
# 	output = E.curselection()
# 	print(output)
