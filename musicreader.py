"""Takes series of notes from markov chain and plays it"""

import atexit
import os
from random import choice

from psonic import *


class Note:
    def __init__(self, tone = 60, duration = 1, volume = 60):
        self.tone = tone
        self.duration = duration
        self.volume = volume

# The sample directory is relative to this source file's directory.
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "samples")

SAMPLE_FILE = os.path.join(SAMPLES_DIR, "bass_G2.wav")
SAMPLE_NOTE = D2  # the sample file plays at this pitch


def play_note(current_note,bpm = 120):
    # note, beats=1, bpm=300, amp=100):
    """Plays note for `beats` beats. Returns when done."""
    # `note` is this many half-steps higher than the sampled note
    note = current_note.tone
    beats = current_note.duration
    amp = current_note.volume
    half_steps = note - SAMPLE_NOTE

# Here is where you change synths (different sounding notes)
    use_synth(PIANO)
    assert os.path.exists(SAMPLE_FILE)
    # Turn sample into an absolute path, since Sonic Pi is executing from a different working directory.
    play(note, amp=amp)
    sleep(beats * 60 / bpm) #sleep(0.5) #


def stop():
    """Stops all tracks."""
    msg = osc_message_builder.OscMessageBuilder(address='/stop-all-jobs')
    msg.add_arg('SONIC_PI_PYTHON')
    msg = msg.build()
    synthServer.client.send(msg)


atexit.register(stop)  # stop all tracks when the program exits normally or is interrupted
beats_per_minute = 45

# curr_note = 60
# major_intro = [2,2,1,2,2,2,1]
# minor_intro = [-1 -1 -1 -1 -1 -2 -2]
# major_intro_fancy = [(2,1),(2,2),(1,3),(2,0.5),(2,1),(2,1),(1,2)]
# test_midi_notes = [64 65 66 67 68 69 70]
def play_music(list_of_notes):
    # print(list_of_notes)
    # curr_note = list_of_notes[0]
    # curr_note.beats = 1
    # curr_note.bpm = 100
    # curr_note.amp = 100
    for current_note in list_of_notes:
        play_note(current_note)
        # try:
        #     curr_note +=note
        #     print('note: ', note)
        #     if 0 <= curr_note:
        #         play_note(curr_note, beats, bpm, amp)
        #     else:
        #         curr_note = 0
        #         play_note(curr_note, beats, bpm, amp)
        # except:
        #     curr_note += note[0]
        #     print('except note: ', note)
        #     if 0 <= curr_note:
        #         play_note(curr_note, note[1], bpm, amp)
        #     else:
        #         curr_note = 0
        #         play_note(curr_note, note[1], bpm, amp)

if __name__ == "__main__":
    # import random
    # random.seed(1)
    list_of_notes = []
    test_midi_notes = [64, 65, 66, 67, 68, 69, 70]

    for i in range(5):
        random_note = Note(tone = test_midi_notes[i])
        list_of_notes.append(random_note)
    play_music(list_of_notes)
