import random
from midiutil import MIDIFile

notes = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11
}

# Returns the MIDI note number for the given note name and octave
# Letter options are C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# Octaves range from 0 to 10
def note(Letter, Octave):
    return notes.get(Letter) + (Octave * 12)

def random_root():
    # return random.randint(0, 127-11)
    return random.randint(36, 79)

def note_names():
    return notes.keys()

def add_notes(midi, track, channel, notes, time, duration, volume):
    for note in notes:
        midi.addNote(track, channel, note, time, duration, volume)

#we don't need this function tho
def random_note():
    #lst = list(notes.items())
    #return (random.choice(lst)[1] + 60)
    return (random_root())

def random_common_chord(root):
    return random.choice(common_chords)(root)

def major_triad(root):
    return [root, root + 4, root + 7]

def modified_major_triad1(root):
    return [root-3, root, root + 4, root + 7]

def modified_major_triad2(root):
    return [root-3, root, root + 4, root + 7, root+10]
    
def minor_triad(root):
    return [root, root + 3, root + 7]

def major_seventh(root):
    return [root, root + 4, root + 7, root + 11]

def minor_seventh(root):
    return [root, root + 3, root + 7, root + 10]

def major_sixth(root):
    return [root, root + 4, root + 7, root + 9]

def minor_sixth(root):
    return [root, root + 3, root + 7, root + 9]

def dominant_seventh(root):
    return [root, root + 4, root + 7, root + 10]

def diminished_seventh(root):
    return [root, root + 3, root + 6, root + 10]

def augmented_seventh(root):
    return [root, root + 4, root + 8, root + 10]

def suspended_fourth(root):
    return [root, root + 5, root + 7]

def suspended_second(root):
    return [root, root + 1, root + 7]

common_chords = [major_triad, minor_triad, major_seventh, minor_seventh, major_sixth, minor_sixth, dominant_seventh, diminished_seventh, augmented_seventh, suspended_fourth, suspended_second]

def major_seventh_suspended(root):
    return [root, root + 7, root + 11]

def dominant_seventh_flat_five(root):
    return [root, root + 4, root + 6, root + 10]

def dominant_seventh_sharp_five(root):
    return [root, root + 4, root + 8, root + 10]

def dominant_seventh_flat_nine(root):
    return [root, root + 4, root + 6, root + 10, root + 2]

def dominant_seventh_sharp_nine(root):
    return [root, root + 4, root + 8, root + 10, root + 2]

def major_triad_flat_nine(root):
    return [root, root + 4, root + 6, root + 10]

def major_triad_sharp_nine(root):
    return [root, root + 4, root + 8, root + 10]

def minor_triad_flat_nine(root):
    return [root, root + 3, root + 6, root + 10]

def minor_triad_sharp_nine(root):
    return [root, root + 3, root + 8, root + 10]

def dominant_seventh_flat_two(root):
    return [root, root + 4, root + 6, root + 9]

def dominant_seventh_sharp_two(root):
    return [root, root + 4, root + 8, root + 9]

def diminished_seventh_flat_two(root):
    return [root, root + 3, root + 6, root + 9]

def diminished_seventh_sharp_two(root):
    return [root, root + 3, root + 8, root + 9]

def augmented_seventh_flat_two(root):
    return [root, root + 4, root + 6, root + 9]

def augmented_seventh_sharp_two(root):
    return [root, root + 4, root + 8, root + 9]

def suspended_fourth_flat_two(root):
    return [root, root + 5, root + 6]

def suspended_fourth_sharp_two(root):
    return [root, root + 5, root + 8]

def suspended_second_flat_two(root):
    return [root, root + 1, root + 6]

def suspended_second_sharp_two(root):
    return [root, root + 1, root + 8]

def dominant_seventh_flat_three(root):
    return [root, root + 4, root + 6, root + 9, root + 1]

def dominant_seventh_sharp_three(root):
    return [root, root + 4, root + 8, root + 9, root + 1]

def diminished_seventh_flat_three(root):
    return [root, root + 3, root + 6, root + 9, root + 1]

def diminished_seventh_sharp_three(root):
    return [root, root + 3, root + 8, root + 9, root + 1]

def augmented_seventh_flat_three(root):
    return [root, root + 4, root + 6, root + 9, root + 1]

def augmented_seventh_sharp_three(root):
    return [root, root + 4, root + 8, root + 9, root + 1]

def suspended_fourth_flat_three(root):
    return [root, root + 5, root + 6, root + 1]

def suspended_fourth_sharp_three(root):
    return [root, root + 5, root + 8, root + 1]

#returns true if there is overlap, false if there isn't OR there are 2 notes in a row
#n1 and n2 represent lists of notes (can be only 1 note)
def checkingOverlap(n1, n2):
    first = n1
    second = n2
    if len(n1) == 1 and len(n2) == 1:
        return False
    if len(n2) == 1:
        first = n2
        second = n1
    for n in first:
        for i in range(0,2):
            if n >= second[i] and n <= second[i+1]:
                return True
    return False