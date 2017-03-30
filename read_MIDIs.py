import mido

def read_midi(filename):
    mid = mido.MidiFile(filename)
    print(mid)
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        # test_track = track[350]
        # 
        # print(track[350])
        for i in range(len(track)):
            msg = track[i]
            print(msg)
            print(msg.type)
            try:
                nextmsg = track[i+1]
                print(nextmsg.time)
            except:
                pass


if __name__ == "__main__":
    read_midi('Untitled_441406.mid')