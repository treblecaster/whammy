#!/usr/bin/env python

"""
    Use bars and beats instead of milliseconds
"""

import sys
import os

class TimeSig():
    measure = 1
    wholeNote = 1
    halfNote = float(1)/2
    quarterNote = float(1)/4
    eighthNote = float(1)/8
    a16thNote = float(1)/16
    a32thNote = float(1)/32
    
    # time signature upper numeral indicates how many such beats there are in
    # a bar.
    _beats = None
    
    # time signature lower numeral indicates the note value which represents
    # one beat.
    _noteVal = None

    # Beats per minute
    _bpm = None

    # Not sure exactly how this is supposed to work
    _stdNoteVal = 4
    
    def __init__(self, beats, noteVal, bpm):
        self._beats = beats
        self._noteVal = noteVal
        self._bpm = bpm

    def getBeats(self):
        return self._beats

    def getNoteVal(self):
        return self._noteVal

    def getBPM(self):
        return self._bpm

    def _beatLength(self):
        return (60 * 1000 / self._bpm)

    def bar(self, bar):
        return bar * self._beatLength() * self._beats * self._stdNoteVal / self._noteVal

    def note(self, note):
        return note * self._beatLength() * self._stdNoteVal

    def time(self, bar, note):
        return self.bar(bar) + self.note(note)

