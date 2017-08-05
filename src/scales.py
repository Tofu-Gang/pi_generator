__author__ = 'Tofu Gang'



################################################################################

NOTES_SHARP = 'A A# B C C# D D# E F F# G G#'
NOTES_FLAT = 'A Bb B C Db D Eb E F Gb G Ab'

SCALE_MAJOR = 'Major'
SCALE_PENTATONIC_MINOR = 'Pentatonic Minor'
SCALE_BLUES = 'Blues'
SCALE_PENTATONIC_MAJOR = 'Pentatonic Major'
SCALE_NATURAL_MINOR = 'Natural Minor'
SCALE_HARMONIC_MINOR = 'Harmonic Minor'
SCALE_MELODIC_MINOR_ASC = 'Melodic Minor (asc)'
SCALE_MELODIC_MINOR_DESC = 'Melodic Minor (desc)'
SCALE_DORIAN = 'Dorian'
SCALE_PHRYGIAN = 'Phrygian'
SCALE_LYDIAN = 'Lydian'
SCALE_MIXOLYDIAN = 'Mixolydian'
SCALE_LOCRIAN = 'Locrian'
SCALE_ARABIC = 'Arabic'
SCALE_HUNGARIAN_GYPSY = 'Hungarian Gypsy'
SCALE_WHOLE_TONE = 'Whole Tone'
SCALE_AUGMENTED = 'Augmented'
SCALE_PHRYGIAN_DOMINANT = 'Phrygian Dominant'

SCALE_TYPES = (SCALE_MAJOR,
               SCALE_PENTATONIC_MINOR,
               SCALE_BLUES,
               SCALE_PENTATONIC_MAJOR,
               SCALE_NATURAL_MINOR,
               SCALE_HARMONIC_MINOR,
               SCALE_MELODIC_MINOR_ASC,
               SCALE_MELODIC_MINOR_DESC,
               SCALE_DORIAN,
               SCALE_PHRYGIAN,
               SCALE_LYDIAN,
               SCALE_MIXOLYDIAN,
               SCALE_LOCRIAN,
               SCALE_ARABIC,
               SCALE_HUNGARIAN_GYPSY,
               SCALE_WHOLE_TONE,
               SCALE_AUGMENTED,
               SCALE_PHRYGIAN_DOMINANT)

ROOT_NOTE_A = 'A'
ROOT_NOTE_AshBb = 'A#/Bb'
ROOT_NOTE_B = 'B'
ROOT_NOTE_C = 'C'
ROOT_NOTE_CshDb = 'C#/Db'
ROOT_NOTE_D = 'D'
ROOT_NOTE_DshEb = 'D#/Eb'
ROOT_NOTE_E = 'E'
ROOT_NOTE_F = 'F'
ROOT_NOTE_FshGb = 'F#/Gb'
ROOT_NOTE_G = 'G'
ROOT_NOTE_GshAb = 'G#/Ab'

ROOT_NOTES = (ROOT_NOTE_A,
              ROOT_NOTE_AshBb,
              ROOT_NOTE_B,
              ROOT_NOTE_C,
              ROOT_NOTE_CshDb,
              ROOT_NOTE_D,
              ROOT_NOTE_DshEb,
              ROOT_NOTE_E,
              ROOT_NOTE_F,
              ROOT_NOTE_FshGb,
              ROOT_NOTE_G,
              ROOT_NOTE_GshAb)

SCALES = (('A B C# D E F# G# A', # major
           'Bb C D Eb F G A Bb',
           'B C# D# E F# G# A# B',
           'C D E F G A B C',
           'Db Eb F Gb Ab Bb C Db',
           'D E F# G A B C# D',
           'Eb F G Ab Bb C D Eb',
           'E F# G# A B C# D# E',
           'F G A Bb C D E F',
           'F# G# A# B C# F F#',
           'G A B C D E F# G',
           'Ab Bb C Db Eb F G Ab'),
          ('A C D E G A', # pentatonic minor
           'Bb Db Eb F Ab Bb',
           'B D E F# A B',
           'C Eb F G Bb C',
           'C# E F# G# B C#',
           'D F G A C D',
           'D# F# G# A# C# D#',
           'E G A B D E',
           'F Ab Bb C Eb F',
           'F# A B C# E F#',
           'G Bb C D F G',
           'G# B C# D# F# G#'),
          ('A C D D# E G A', # blues
           'A# C# D# E F G# A#',
           'B D E F F# A B',
           'C Eb F Gb G Bb C',
           'C# E F# G G# B C#',
           'D F G G# A C D',
           'D# F# G# A A# C# D#',
           'E G A A# B D E',
           'F G# A# B C D# F',
           'F# A B C C# E F#',
           'G Bb C Db D F G',
           'G# B C# D D# F# G#'),
          ('A B C# E F# A', # pentatonic major
           'Bb C D F G Bb',
           'B C# D# F# G# B',
           'C D E G A C',
           'Db Eb F Ab Bb Db',
           'D E F# A B D',
           'Eb F G Bb C Eb',
           'E F# G# B C# E',
           'F G A C D F',
           'F# G# A# C# D# F#',
           'G A B D E G',
           'Ab Bb C Eb F Ab'),
          ('A B C D E F G A', # natural minor
           'Bb C Db Eb F Gb Ab Bb',
           'B C# D E F# G A B',
           'C D Eb F G Ab Bb C',
           'C# D# E F# G# A B C#',
           'D E F G A Bb C D',
           'D# F F# G# A# B C# D#',
           'E F# G A B C D E',
           'F G Ab Bb C Db Eb F',
           'F# G# A B C# D E F#',
           'G A Bb C D Eb F G',
           'G# A# B C# D# E F# G#'),
          ('A B C D E F G# A', # harmonic minor
           'Bb C Db Eb F Gb A Bb',
           'B C# D E F# G A# B',
           'C D Eb F G Ab B C',
           'C# D# E F# G# A C C#',
           'D E F G A A# C# D',
           'Eb F Gb Ab Bb B D Eb',
           'E F# G A B C D# E',
           'F G Ab Bb C Db E F',
           'F# G# A B C# D F F#',
           'G A Bb C D Eb Gb G',
           'G# A# B C# D# E G G#'),
          ('A B C D E F# G# A', # melodic minor (asc)
           'Bb C Db Eb F G A Bb',
           'B C# D E F# G# A# B',
           'C D Eb F G A B C',
           'C# D# E F# G# A# C C#',
           'D E F G A B C# D',
           'Eb F Gb Ab Bb C D Eb',
           'E F# G A B C# D# E',
           'F G Ab Bb C D E F',
           'F# G# A B C# D# F F#',
           'G A A# C D E F# G',
           'G# A# B C# D# F G G#'),
          ('A B C D E F G A', # melodic minor (desc)
           'Bb C Db Eb F Gb Ab Bb',
           'B C# D E F# G A B',
           'C D Eb F G Ab Bb C',
           'C# D# E F# G# A B C#',
           'D E F G A Bb C D',
           'D# F F# G# A# B C# D#',
           'E F# G A B C D E',
           'F G Ab Bb C Db Eb F',
           'F# G# A B C# D E F#',
           'G A Bb C D Eb F G',
           'G# A# B C# D# E F# G#'),
          ('A B C D E F# G A', # dorian
           'Bb C Db Eb F G Ab Bb',
           'B C# D E F# G# A B',
           'C D Eb F G A Bb C',
           'C# D# E F# G# A# B C#',
           'D E F G A B C D',
           'Eb F Gb Ab Bb C Db Eb',
           'E F# G A B C# D E',
           'F G Ab Bb C D Eb F',
           'F# G# A B C# D# E F#',
           'G A Bb C D E F G',
           'G# A# B C# D# F F# G#'),
          ('A Bb C D E F G A', # phrygian
           'A# B C# D# F F# G# A#',
           'B C D E F# G A B',
           'C Db Eb F G Ab Bb C',
           'C# D E F# G# A B C#',
           'D Eb F G A Bb C D',
           'D# E F# G# A# B C# D#',
           'E F G A B C D E',
           'F Gb Ab Bb C Db Eb F',
           'F# G A B C# D E F#',
           'G Ab Bb C D Eb F G',
           'G# A B C# D# E F# G#'),
          ('A B C# D# E F# G# A', # lydian
           'Bb C D E F G A Bb',
           'B C# D# F F# G# A# B',
           'C D E F# G A B C',
           'Db Eb F G Ab Bb C Db',
           'D E F# G# A B C# D',
           'Eb F G A Bb C D Eb',
           'E F# G# A# B C# D# E',
           'F G A B C D E F',
           'Gb Ab Bb C Db Eb F Gb',
           'G A B C# D E F# G',
           'Ab Bb C D Eb F G Ab'),
          ('A B C# D E F# G A', # mixolydian
           'Bb C D Eb F G Ab Bb',
           'B C# D# E F# G# A B',
           'C D E F G A Bb C',
           'C# D# F F# G# A# B C#',
           'D E F# G A B C D',
           'Eb F G Ab Bb C Db Eb',
           'E F# G# A B C# D E',
           'F G A Bb C D Eb F',
           'F# G# A# B C# D# E F#',
           'G A B C D E F G',
           'Ab Bb C Db Eb F Gb Ab'),
          ('A Bb C D Eb F G A', # locrian
           'A# B C# D# E F# G# A#',
           'B C D E F G A B',
           'C Db Eb F Gb Ab Bb C',
           'C# D E F# G A B C#',
           'D Eb F G Ab Bb C D',
           'D# E F# G# A B C# D#',
           'E F G A Bb C D E',
           'F F# G# A# B C# D# F',
           'F# G A B C D E F#',
           'G Ab Bb C Db Eb F G',
           'G# A B C# D E F# G#'),
          ('A A# C# D E F G# A', # arabic
           'Bb B D Eb F Gb A Bb',
           'B C D# E F# G A# B',
           'C Db E F G Ab B C',
           'C# D F F# G# A C C#',
           'D D# F# G A A# C# D',
           'D# E G G# A# B D D#',
           'E F G# A B C D# E',
           'F Gb A Bb C Db E F',
           'F# G A# B C# D F F#',
           'G G# B C D D# F# G',
           'G# A C C# D# E G G#'),
          ('A B C D# E F G# A', # hungarian gypsy
           'Bb C Db E F Gb A Bb',
           'B C# D F F# G A# B',
           'C D D# F# G G# B C',
           'C# D# E G G# A C C#',
           'D E F G# A A# C# D',
           'Eb F Gb A Bb B D Eb',
           'E F# G A# B C D# E',
           'F G Ab B C Db E F',
           'F# G# A C D# D F F#',
           'G A A# C# D D# F# G',
           'G# A# B D D# E G G#'),
          ('A B C# D# F G A', # whole tone
           'A# C D E F# G# A#',
           'B C# D# F G A B',
           'C D E F# G# A# C',
           'C# D# F G A B C#',
           'D E F# G# A# C D',
           'D# F G A B C# D#',
           'E F# G# A# C D E',
           'F G A B C# D# F',
           'F# G# A# C D E F#',
           'G A B C# D# F G',
           'G# A# C D E F# G#'),
          ('A C Db E F Ab A', # augmented
           'A# C# D F F# A A#',
           'B D D# F# G A# B',
           'C D# E G G# B C',
           'Db E F Ab A C Db',
           'D F F# A A# C# D',
           'D# F# G A# B D D#',
           'E G G# B C D# E',
           'F Ab A C Db E F',
           'F# A A# C# D F F#',
           'G A# B D D# F# G',
           'G# B C D# E G G#'),
          ('A A# C# D E F G A', # phrygian dominant
           'Bb B D Eb F Gb Ab Bb',
           'B C D# E F# G A B',
           'C Db E F G Ab Bb C',
           'C# D F F# G# A B C#',
           'D Eb Gb G A Bb C D',
           'D# E G G# A# B C# D#',
           'E F G# A B C D E',
           'F Gb A Bb C Db Eb F',
           'F# G A# B C# D E F#',
           'G Ab B C D Eb F G',
           'G# A C C# D# E F# G#'))

################################################################################