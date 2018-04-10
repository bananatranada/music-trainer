from interval import Interval

#TODO: refactor to include octave in a note. then multiply by 12 and add its position
NOTES = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11,
}

# NOTE_AT[1] => ['C#','Db']
NOTES_AT = {}
for note, pos in NOTES.items():
    if pos not in NOTES_AT:
        NOTES_AT[pos] = []
    NOTES_AT[pos].append(note)

def to_sharp(name):
    if 'b' not in name:
        name 
    alts = NOTES_AT[NOTES[name]]
    for alt in alts:
        if alt is not name:
            return alt
    return name

def to_flat(name):
    if '#' not in name:
        name 
    alts = NOTES_AT[NOTES[name]]
    for alt in alts:
        if alt is not name:
            return alt
    return name


class Note:
    def __init__(self, name):
        if name not in NOTES:
            raise Exception(name, 'is not a valid note!')
        self.name = name
        self.name_sharp = to_sharp(self.name)
        self.name_flat = to_flat(self.name)
        self.position = NOTES[self.name]

    def add_interval(self, interval):
        return self.add(interval.semis)

    def add(self, semis):
        i = (self.position + semis) % 12
        return Note(NOTES_AT[i][0])

# note1 = Note('A')
# print(note1.add_interval(Interval('M3')).name)
    

    # def add_interval(self, interval):
    #     curr_pos = NOTES_TO_POSITION[self.name]
    #     semis = interval.semis
    #     return Note(POSITION_TO_NOTES[curr_pos+semis])

    # def sub_note(self, note):
    #     to_pos = NOTES_TO_POSITION[self.name]
    #     from_pos = NOTES_TO_POSITION[note.name]
    #     # print(to_pos-from_pos)
    #     interval = Interval.semis_to_interval(to_pos - from_pos)
    #     return interval

    # def equals(self, note):
    #     return NOTES_TO_POSITION[self.name] == NOTES_TO_POSITION[note.name]


# n = Note('Bb')
# print(n.name_sharp)
    