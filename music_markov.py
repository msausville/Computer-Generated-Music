'''
music_markov.py

Purpose: takes a list of notes from the music analysis, do some markov
analysis, and return a list of notes to be played.

Author:Hannah Kolano
hannah.kolano@students.olin.edu

Next step: fix the markov function
'''


# All the imports
import random


# global variables
m_dict = dict()                 # markov dictionary
pre_len = 1                     # prefix length
d_dict = dict()           # markov dict of measures
# num_measures = 8                # number of desired measures, in 4/4, not implemented yet


# Important Classes
class Note:
    def __init__(self, tone=60, duration=1, volume=60):
        """initializes a note object"""
        self.tone = tone
        self.duration = duration
        self.volume = volume

    def __str__(self):
        """prints the attributes of a note object"""
        return "'tone = %s', 'duration = %s', 'volume = %s'" % (str(self.tone), str(self.duration), str(self.volume))

class Song:
    def __init__(self, notes_list):
        """creates a song object from a list of notes"""
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)
        self.process_durations()

    def add_to_analysis(self, an_dict, duration_dict, pre_len=1):
        """hey Song, add yourself to the markov dictionary"""
        intervals = self.intervals
        for i in range(len(intervals) - pre_len):
            prefix = tuple(intervals[i:i + pre_len])
            suffix = intervals[i + pre_len]
            an_dict[prefix] = an_dict.get(prefix, tuple()) + (suffix,)
        durations = self.durations
        for i in range(len(durations)-pre_len):
            prefix = durations[i]
            suffix = durations[i+pre_len]
            duration_dict[prefix] = duration_dict.get(prefix, tuple()) + (suffix,)

    def process_durations(self):
        self.durations = []
        for note in self.concrete:
            self.durations.append(note.duration)


# Functions
def con_to_int(note_list):
    """takes a list of note objects and returns a list of note intervals"""
    int_list = []
    for i in range(len(note_list)-1):
        int_list.append(note_list[i+1].tone - note_list[i].tone)
    return int_list

def create_markov_chain(mark_dict, dur_dict, start_note=60, len_in_beats=32, pre_len=1):
    """takes a markov dict; returns a markov'd list of note objects"""
    # initialize some variables
    possible_notes = poss_notes(start_note, 'major')
    new_intervals = [0]
    first_duration = random.choice(dur_dict.keys())
    new_durations = [first_duration]
    new_melody = [Note(start_note, new_durations[0])]
    num_beats = first_duration
    # do this for as many beats as we want
    for i in range(len_in_beats - pre_len):
        next_note = -1
        tone_options = mark_dict[new_intervals[i],]
        dur_options = dur_dict[new_durations[i]]
        # tone is right when it's in the possible notes list
        while next_note not in possible_notes:
            next_interval = random.choice(tone_options)
            next_note = new_melody[i].tone + next_interval
        next_duration = random.choice(dur_options)
        # makes sure the next duration would finish a measure
        while num_beats + float(next_duration) > 4:
            next_duration = random.choice(dur_options)
        # reset number of beats in current measure
        num_beats = float(num_beats) + float(next_duration)
        if num_beats == 4:
            num_beats = 0
        # append everything
        new_melody.append(Note(next_note, next_duration))
        new_intervals.append(next_interval)
        new_durations.append(next_duration)
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

# options = prefixes_dict[tuple(prefix)]
#         next_word = random.choice(options)

# Initialize some songs
baa_baa_concrete = [Note(0, 1), Note(0, 1), Note(7, 1), Note(7, 1),                 # baa baa black sheep
                    Note(9, .5), Note(9, .5), Note(9, .5), Note(9, .5), Note(7, 2), # have you any wool
                    Note(5, 1), Note(5, 1), Note(4, 0), Note(4, 0),                 # yes sir yes sir
                    Note(2, 1), Note(2, 1), Note(0, 2),                             # three bags full
                    Note(7, 1), Note(7, 0.5), Note(7, 0.5), Note(5, 1), Note(5, 1), # one for the doctor
                    Note(4, 1), Note(4, 0.5), Note(4, 0.5), Note(2, 2),             # one for the dame
                    Note(7, 1), Note(7, 0.5), Note(7, 0.5),                         # one for the
                    Note(5, .5), Note(5, .5), Note(5, .5), Note(5, .5),             # little boy who
                    Note(4, 1), Note(4, 0.5), Note(4, 0.5), Note(2, 2),             # lives down the lane
                    Note(0, 1), Note(0, 1), Note(7, 1), Note(7, 1),                 # baa baa black sheep
                    Note(9, .5), Note(9, .5), Note(9, .5), Note(9, .5), Note(7, 2), # have you any wool
                    Note(5, 1), Note(5, 1), Note(4, 0), Note(4, 0),                 # yes sir yes sir
                    Note(2, 1), Note(2, 1), Note(0, 2)]                             # three bags full
BaaBaa = Song(baa_baa_concrete)
hot_cross_concrete = [Note(4, 1), Note(2, 1), Note(0, 2),                   # hot cross buns
                      Note(4, 1), Note(2, 1), Note(0, 2),                   # hot cross buns
                      Note(0, .5), Note(0, .5), Note(0, .5), Note(0, .5),   # one a penny
                      Note(2, .5), Note(2, .5), Note(2, .5), Note(2, .5),   # two a penny
                      Note(4, 1), Note(2, 1), Note(0, 2)]                   # hot cross buns
HotCross = Song(baa_baa_concrete)
mary_had_concrete = [Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # Mary had a
                     Note(4, 1), Note(4, 1), Note(4, 2),                # Little lamb
                     Note(2, 1), Note(2, 1), Note(2, 2),                # little lamb
                     Note(4, 1), Note(7, 1), Note(7, 2),                # little lamb
                     Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # Mary had a
                     Note(4, 1), Note(4, 1), Note(4, 1), Note(4, 1),    # little lamb whose
                     Note(2, 1), Note(2, 1), Note(4, 1), Note(2, 1),    # fleece was white as
                     Note(0, 4),                                        # snow
                     Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # every where that
                     Note(4, 1), Note(4, 1), Note(4, 2),                # mary went
                     Note(2, 1), Note(2, 1), Note(2, 2),                # mary went
                     Note(4, 1), Note(7, 1), Note(7, 2),                # mary went
                     Note(4, 1), Note(2, 1), Note(0, 1), Note(2, 1),    # every where that
                     Note(4, 1), Note(4, 1), Note(4, 1), Note(4, 1),    # mary went that
                     Note(2, 1), Note(2, 1), Note(4, 1), Note(2, 1),    # lamb was sure to
                     Note(0, 4)]                                        # go
MaryHad = Song(mary_had_concrete)
this_old_concrete = [Note(7, 1), Note(4, 1), Note(7, 2),                # this old man
                     Note(7, 1), Note(4, 1), Note(7, 2),                # he played one
                     Note(9, 1), Note(7, 1), Note(5, 1), Note(4, 1),    # he played knick-knack
                     Note(2, 1), Note(4, 1), Note(5, 1),                # on my thumb
                     Note(4, .5), Note(5, .5), Note(7, 1), Note(0, 1),  # with a nick nack
                     Note(0, .5), Note(0, .5), Note(0, 1),              # paddy whack
                     Note(0, .5), Note(2, .5), Note(4, .5), Note(5, .5), Note(7, 2), # give the dog a bone
                     Note(7, 1), Note(2, 1), Note(2, 1), Note(5, 1),    # this old man came
                     Note(4, 1), Note(2, 1), Note(0, 2)]                # rolling home
ThisOld = Song(this_old_concrete)


# Actually run stuff
ThisOld.add_to_analysis(m_dict, d_dict)
MaryHad.add_to_analysis(m_dict, d_dict)
BaaBaa.add_to_analysis(m_dict, d_dict)
HotCross.add_to_analysis(m_dict, d_dict)

chain = create_markov_chain(m_dict, d_dict)
for note in chain:
    print(note)
