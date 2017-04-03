import mido

class Note:
    def __init__(self,value = 60, volume = 60, duration = 0):
        self.value = value
        self.duration = duration
        self.volume = volume

def read_midi(filename):
    mid = mido.MidiFile(filename)
    print(mid)
    list_of_notes = []
    open_notes = []
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        # test_track = track[350]
        # 
        # print(track[350])
        for j in range(len(track)):
            msg = track[j]
            print(msg)
            print(msg.type)
            is_new_note = True
            for old_note in open_notes:
                old_note.duration += msg.time
                
                if old_note.note == msg.note:
                    is_new_note = False
                    if msg.type == 'note_on':
                        if msg.note.velocity == 0:
                            list_of_notes.append(old_note)
                            open_notes.remove(old_note)
                    elif msg.type == 'note_off':
                        list_of_notes.append(old_note)
                        open_notes.remove(old_note)
            if is_new_note:
                new_note = Note(msg.note, msg.velocity)
                open_notes.append(new_note)

                
            try:
                nextmsg = track[j+1]
                print(nextmsg.time)
            except:
                pass
    return list_of_notes

if __name__ == "__main__":
    read_midi('Untitled_441406.mid')
