from random import *
from note import *
from notes import *
from interval import *

class FretboardIntervals:
    def __init__(self, name):
        self.name = name

    def add_arguments(self, parser):
        parser.add_argument('--range',
            nargs=2,
            default=['E3', 'G6'],
            help='Choose the range of notes')
        parser.add_argument('-d', '--directions',
            nargs='+',
            default=['asc', 'desc'],
            help='Choose the directions of the interval (asc,desc).')
        parser.add_argument('-r', '--roots',
            nargs='+',
            default=[
                'C',
                'C#',
                'Db',
                'D',
                'D#',
                'Eb',
                'E',
                'F',
                'F#',
                'Gb',
                'G',
                'G#',
                'Ab',
                'A',
                'A#',
                'Bb',
            ],
            choices=[
                'C',
                'C#',
                'Db',
                'D',
                'D#',
                'Eb',
                'E',
                'F',
                'F#',
                'Gb',
                'G',
                'G#',
                'Ab',
                'A',
                'A#',
                'Bb',
            ],
            help='Choose the root notes.')
        parser.add_argument('-i', '--intervals',
            nargs='+',
            default=[
                'U',
                'm2',
                'M2',
                'm3',
                'M3',
                'P4',
                'T',
                'P5',
                'm6',
                'M6',
                'm7',
                'M7',
                'O',
            ],
            choices=[
                'U',
                'm2',
                'M2',
                'm3',
                'M3',
                'P4',
                'T',
                'P5',
                'm6',
                'M6',
                'm7',
                'M7',
                'O',
            ],
            help='Choose the intervals to work with.')

    def start(self, args):
        print(args.roots)
        print('Identify the intervals on the fretboard.')

        # need to create a new dictionary with C3, C#3, etc
        notes = []
        for root in args.roots:
            # notes.append(Note(root))
            notes.append(root)
        # notes = sorted(notes, key=lambda x: x.position)
        notes = sorted(notes)


        all_notes = {}
        ns = NaturalNotes + FlatNotes + SharpNotes
        x = 0
        for i in range(0, 10):
            for note in ns:
                all_notes[note.name+str(i)] = x
                x = x + 1

        lower_note_pos = all_notes[args.range[0]]
        upper_note_pos = all_notes[args.range[1]]
        ex_notes = []
        for note, pos in all_notes.items():
            if pos < lower_note_pos or pos > upper_note_pos:
                continue
            ex_notes.append(note)

        # filter out the upper notes by the max interval
        intervals = []
        for interval in args.intervals:
            intervals.append(Interval(interval))

        max_semis = 0
        for interval in intervals:
            if interval.semis > max_semis:
                max_semis = interval.semis
        
        ex_notes = ex_notes[0:len(ex_notes)-max_semis]

        # filter out the non roots
        random_notes = []
        for n in ex_notes:
            if n[:-1] in notes:
                random_notes.append(n)

        for note in ex_notes:
            print(note, end=' ')
        print(max_semis)

        while(True):
            seed()

            random_direction = choice(args.directions)
            random_interval = choice(args.intervals)
            random_note = choice(random_notes)

            print('{} + {}{}'.format(random_note, random_interval, random_direction[0]), end='')
            input()

