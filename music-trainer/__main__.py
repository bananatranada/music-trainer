import argparse
import sys
from random import *

from ex_fretboard_notes import FretboardNotes
from ex_fretboard_intervals import FretboardIntervals
from ex_intervals import Intervals

exercises = [
    FretboardNotes('fretboard-notes'),
    FretboardIntervals('fretboard-intervals'),
    Intervals('intervals'),
]

parser = argparse.ArgumentParser(description='Collection of music training scripts.')
subparsers = parser.add_subparsers(dest='exercise', help='Choose an exercise')
subparsers.required = True

for ex in exercises:
    ex.add_arguments(subparsers.add_parser(ex.name))

args = parser.parse_args()

for ex in exercises:
    if ex.name == args.exercise:
        ex.start(args)
        break

# parser.add_argument('-t', '--type', 
#                     default='all',
#                     choices=['all', 'interval', 'note'],
#                     help='Choose the type of training (interval=Guess the interval, note=Guess the note).')
# parser.add_argument('-r', '--root', 
#                     default='all', 
#                     help='Specify the root note (Use quotes around sharp notes).')
# parser.add_argument('-i', '--intervals', 
#                     nargs='+',
#                     default=['m2','M2','m3','M3','P4','T','P5','m6','M6','m7','M7'], 
#                     help='Specify the intervals to work on.')
# parser.add_argument('-a', '--accidentals', 
#                     default='all', 
#                     choices=['all', 'sharp', 'flat'],
#                     help='Choose what type of notes to generate.')
# args = parser.parse_args()


# while(True):
#     seed()

#     note_type = args.type
#     if note_type == 'all':
#         note_type = choice(['interval', 'note'])

#     interval = Interval(choice(args.intervals))
    
#     if args.root is not 'all':
#         from_note = Note(args.root)
#     else:
#         from_note = Note(choice(POSITION_TO_NOTES[:-14]))

#     to_note = from_note.add_interval(interval)
#     # print(from_note.name, to_note.name)

#     # print('{0}->{1}').format(note1.name(), note2.name())
#     # semis = note1.semis_up(note2)
#     if note_type == 'interval':
#         print('[Q] {}->{}=?'.format(from_note.name, to_note.name))
#         answer = interval
#     else:
#         print('[Q] {}+{}=?'.format(from_note.name, interval.name))
#         answer = to_note


#     while(True):
#         user_input = input()
#         if user_input == 'q':
#             sys.exit()
#         try:
#             if note_type is 'note':
#                 if Note(user_input).equals(answer):
#                     break
#             else:
#                 if user_input == answer.name:
#                     break

#         except:
#             continue
