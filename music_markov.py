'''
music_markov.py

Purpose: takes a list of notes from the music analysis, do some markov
analysis, and return a list of notes to be played.

Author:Hannah Kolano
hannah.kolano@students.olin.edu

Next step: fix the markov function
'''

# Important Classes
class Song:
    def __init__(self, notes_list):
        self.concrete = notes_list
        self.intervals = con_to_int(self.concrete)


class Note:
    def __init__(self, note, duration):
        self.tone = note
        self.duration = duration


# Functions
def con_to_int(song):
    '''takes a list of concrete notes and returns a list of note intervals'''
    int_list = [0]
    for i in range(len(song)-1):
        int_list.append(song[i+1].tone - song[i].tone)
    return int_list


def create_markov_dict(song):
    '''takes a song object and returns a markov dictionary'''
    for interval in song.intervals:
        m_dict.get[interval] = m_dict.get(interval) + PREVIOUSINTERVAL


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
m_dict = dict()
pre_len = 1
print(MaryHad.intervals)
