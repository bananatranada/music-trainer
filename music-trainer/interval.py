INTERVALS = {
    'U': 0,
    'm2': 1,
    'M2': 2,
    'm3': 3,
    'M3': 4,
    'P4': 5,
    'T': 6,
    'P5': 7,
    'm6': 8,
    'M6': 9,
    'm7': 10,
    'M7': 11,
    'O': 12,
}

SEMIS_TO_INTERVALS = {}
for interval, semis in INTERVALS.items():
    SEMIS_TO_INTERVALS[semis] = interval

class Interval:
    def __init__(self, name):
        if name not in INTERVALS:
            raise Exception(name + ' is not a valid interval!')
        self.name = name
        self.semis = INTERVALS[name]

    @staticmethod
    def semis_to_interval(semis):
        return SEMIS_TO_INTERVALS[semis]
