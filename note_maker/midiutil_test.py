from midiutil import MIDIFile
import random
from _util import *

def write_song(name, song, MyMIDI):
    i = 0
    for val in song:    #so we don't forget to add the very first val in song
        add_notes(MyMIDI, track, channel, val, time + i, duration, volume)
        i = i + 1

    with open(name, "wb") as output_file:
        MyMIDI.writeFile(output_file)

def make_song(note_count):
    # song = []
    # notes_so_far = 0
    
    while notes_so_far != note_count:
        note_gen = []     #list of notes and chords
        for i in range(note_count*10): # loop note_count * 10 times producing random chords/notes
            rando = random.randint(0,10)
            if rando: # if rando != 0, add a chord
                note_gen.append(random_common_chord(random_root()))
            else: # otherwise, add a single note
                note_gen.append([random_root()])

        if not notes_so_far:
            song.append(random.choice(note_gen))
            note_gen.remove(song[0])
            notes_so_far += 1

        for vals in note_gen:
            if checkingOverlap(song[-1], vals):
                song.append(vals)
                notes_so_far += 1
            if notes_so_far == note_count:
                break
                
    return song

# degrees  = [60, 62, 64, 65, 67, 69, 71] # MIDI note number in the 5th octave
track    = 0
channel  = 0
time     = 0   # In beats (used to control when to play the next note)
tracks   = 1
duration = 1
tempo    = 60
volume   = 100

MyMIDI1 = MIDIFile(tracks) # One track, defaults to format 1 (tempo track automatically created)
MyMIDI1.addTempo(track, time, tempo)
s1 = make_song(15) # will return a list of notes/chords for adding to the song

MyMIDI2 = MIDIFile(tracks) # One track, defaults to format 1 (tempo track automatically created)
MyMIDI2.addTempo(track, time, tempo)
s2 = make_song(15)

split_gamut = 5
split_variance = int(len(s1)/split_gamut) #in the example, this is 3
split_pt = split_variance * int(split_gamut/2)
split_pt += random.randint(1,split_variance+1)

MyMIDI3 = MIDIFile(tracks) # One track, defaults to format 1 (tempo track automatically created)
MyMIDI3.addTempo(track, time, tempo)
s3 = s1[:split_pt] + s2[split_pt:]

MyMIDI4 = MIDIFile(tracks) # One track, defaults to format 1 (tempo track automatically created)
MyMIDI4.addTempo(track, time, tempo)
s4 = s2[:split_pt] + s1[split_pt:]

write_song('song1.mid', s1, MyMIDI1)
write_song('song2.mid', s2, MyMIDI2)
write_song('song3.mid', s3, MyMIDI3)
write_song('song4.mid', s4, MyMIDI4)

'''
for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    #MyMIDI.addNote(track, channel, degrees[random.randint(0,len(degrees)-1)], time, duration, volume)
    time = time + 1
'''

'''
Fitness stuff:
    generally only use 8 out the 12 notes
    chords are made by skipping notes
    theres 3 notes that you play almost all the time (called chords), note 1, note 3, and note 5
        Notes 2,4,6 sounds really good together (8 is an octive higher than 1, higher pitch)
        3 5 7
        4 6 8
        G B D (in note form) this would be a good closer (another would be F A C)
        basically, skipping notes sounds good
    C-C is called an octive (8 notes in total)
    2 4 6 goes really nice into G B C
    sometimes we want G chord to go to A chord (less frequently)
    chords that overlap sounds good together
    major cadency sounds good 5-1 or 4-1
    6 and 3 are substitution chords for 1 (but don't start or end with them)
    try to not use the B chord (if the chord is B D F, pick a different chord) it sounds cool, but needs lots of rules around it
    chords 4 and 5 can substitute for each other
    chord 2 can sometimes be used instead of chord 4 or 5 (rarely)
    Never want to have more than 4 notes happen at one time (snare drum is included in that 4)

    We also want to limit repititon of stuff too
'''