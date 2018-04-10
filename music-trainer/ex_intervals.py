from random import *
from notes import *
from interval import *

class Intervals:
    def __init__(self, name):
        self.name = name

    def add_arguments(self, parser):
        parser.add_argument('-t', '--type',
            nargs='+',
            default=['interval','note'],
            help='Choose the type of training (interval=Guess the interval, note=Guess the note).')
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
        print('Identify the note or interval.')

        

        while(True):
            seed()
            ex_type = choice(args.type)
            interval = Interval(choice(args.intervals))
            note_from = Note(choice(args.roots))
            note_to = note_from.add_interval(interval)

            if ex_type == 'interval':
                print('{}+?->{}'.format(note_from.name, note_to.name),end=' ')
                answer = interval.name
            else:
                print('{}+{}->?'.format(note_from.name, interval.name),end=' ')
                answer = note_to.name

            while(True):
                user_input = input()
                if user_input == answer:
                    break


    