from random import *
from notes import *

class FretboardNotes:
    def __init__(self, name):
        self.name = name

    def add_arguments(self, parser):
        parser.add_argument('-s', '--strings',
            type=int,
            default=6,
            help='Choose the number of strings.')
        parser.add_argument('-a', '--accidentals',
            nargs='+',
            default=['naturals','flats','sharps'],
            help='Choose which accidentals to work on.')

    def start(self, args):
        print('Identify the notes on the fretboard in the \
order of the strings specified (1=highest string).')

        notes = []
        for accidental in args.accidentals:
            if accidental == 'naturals':
                notes.extend(NaturalNotes)
            if accidental == 'flats':
                notes.extend(FlatNotes)
            if accidental == 'sharps':
                notes.extend(SharpNotes)
        
        strings = list(range(1, args.strings+1))

        while(True):
            seed()
            shuffle(strings)
            note = choice(notes)
            print('{}:\t'.format(note.name), end='')
            print('-'.join('{}'.format(x) for _, x in enumerate(strings)), end='')
            while(True):
                user_input = input()
                break


    