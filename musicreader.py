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

    def __str__(self):
        """prints the attributes of a note object"""
        return "'tone = %s', 'duration = %s', 'volume = %s'" % (str(self.tone), str(self.duration), str(self.volume))


# The sample directory is relative to this source file's directory.
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "samples")

SAMPLE_FILE = os.path.join(SAMPLES_DIR, "bass_G2.wav")
SAMPLE_NOTE = D2  # the sample file plays at this pitch


def play_note(current_note,bpm = 300):
    """Plays note for `beats` beats. Returns when done."""
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

def play_music(list_of_notes, list_of_notes_2):

    for current_note in list_of_notes:
        for current_note_2 in list_of_notes_2:
            play_note(current_note)
            play_note(current_note_2)

if __name__ == "__main__":
    list_of_notes = []
    test_midi_notes = [64, 65, 66, 67, 68, 69, 70]
    list_of_notes_2 = []
    test_2_midi_notes = [40, 41, 43, 44, 45, 46, 47]

    for i in range(5):
        random_note = Note(tone = test_midi_notes[i])
        list_of_notes.append(random_note)
    for j in range(5):
        random_note_2 = Note(tone = test_2_midi_notes[j])
        list_of_notes_2.append(random_note_2)
    play_music(list_of_notes, list_of_notes_2)
    # play_music(list_of_notes) and play_music(list_of_notes_2)
