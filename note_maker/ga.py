from midiutil import MIDIFile
import random
from _util import *

NOTES_PER_SONG = 60
C,CS,D,DS,E,F,FS,G,GS,A,AS,B = 0,1,2,3,4,5,6,7,8,9,10,11
# add_song_to_MIDI does the legwork of adding a list of notes/chords to the MIDIFile object.
def add_song_to_MIDI(MyMIDI, song, track, channel, time, duration, volume):
    i = 0
    for val in song:    #so we don't forget to add the very first val in song
        add_notes(MyMIDI, track, channel, val, time + i, duration, volume)
        i = i + 1
    return MyMIDI

# write_song_to_file, provided a MIDIFile and file name, will write a MIDIFile to a file
def write_song_to_file(MyMIDI, filename):
    if '.mid' not in filename:
        filename += '.mid'
    with open(filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)

# make_song, provided a number of notes, will produce a random set of overlapping notes as a list
def make_song(note_count):
    song = []
    notes_so_far = 0
    
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

# generate_MIDI must be provided a __list__ of songs. 
# It will add each song to an additional track of a MIDIFile object, and return that MIDIFile.
def generate_MIDI(songs, channel=0, tracks=1, duration=1, times=[0], tempos=[60], volume=100):
    # degrees  = [60, 62, 64, 65, 67, 69, 71] # MIDI note number in the 5th octave

    MyMIDI = MIDIFile(tracks)

    for i in range(0,len(songs)):
        track = i
        MyMIDI.addTempo(track, times[i], tempos[i])
        add_song_to_MIDI(MyMIDI, songs[i], track, channel, times[i], duration, volume)

    return MyMIDI

# combine_songs takes in two song lists (and optionally a point in which to split them)
# it returns both songs with one half of song 'a' transplanted into song 'b'
def combine_songs(song1, song2, split_pt=-1):
    split_gamut = 5
    # if we were not provided a split point, we will find our own based on the middle 1/5 of the song
    if split_pt == -1:
        split_variance = int(len(s1)/split_gamut)
        split_pt = split_variance * int(split_gamut/2)
        split_pt += random.randint(1,split_variance+1)

    song1_split = song1[:split_pt] + song2[split_pt:]
    song2_split = song2[:split_pt] + song1[split_pt:]
    return song1_split, song2_split


# def combine_multitempo_songs(song1, song2, tempo1, tempo2, start1, start2, split_pt=-1)
# TODO, if you want: 
# takes two note lists and their respective tempos, and combines them into a single MIDIFile object
# did we wanna combine them by alternating notes? Or just by putting in on the end
# there is a note limit (of three) with midi, so we might already be at the max before starting
def combine_multitempo_songs(song1, song2, tempo1, tempo2, start1, start2, split_pt=-1):
    pass

# TODO 
# initial: create X songs using make_song

# in a loop:
    # check the fitness of each one, sort them in order of fitness (highest to lowest?)
    # for each song, combine it with the song next to it (until we have X/2 children)
    # create a new genome with all the new children songs and most fit parents

#   attempt at fitness function
def checkFitness(song):
    #song is a 2D array of chords
    #checking for good closer chords
    if len(song[-1])==3:
        if song[-1][0] % 12 == G and song[-1][1] % 12 == B and song[-1][2] % 12 == D:
            pass
        if song[-1][0] % 12 == F and song[-1][1] % 12 == A and song[-1][2] % 12 == C:
            pass


# TODO: pattern matching for songs, and repetition of the same pattern
# Music sounds good when it's not 50 different chords/notes pulled from a hat
# take the first 2/4/8/16 notes, and repeat them a second time. If it's a fit result, add more of those notes 

# possible structure:
# chorus is a group of repeating notes/chords in a multiple of 2/4/8/16 that's repeated 2+ times in the song
# everything else should generally sound similar, but it can totally have its own flair
# e.g first non-chorus part (I am not a music theory guy) would sound like XXXX
#    second non-chorus part (I am not a music theory guy) would sound like XYXY 
#    but all chorus sounds like LMNO LMNO LMNO LMNO

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
song = [major_triad(50),modified_major_triad1(50),modified_major_triad2(50)]
myMidi = generate_MIDI([song])
write_song_to_file(myMidi,"test.mid")
#song = make_song(NOTES_PER_SONG)    #creates song
#checkFitness(song)


