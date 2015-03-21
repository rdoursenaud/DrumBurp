# Copyright 2011-12 Michael Thomas
#
# See www.whatang.org for more information.
#
# This file is part of DrumBurp.
#
# DrumBurp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DrumBurp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DrumBurp.  If not, see <http://www.gnu.org/licenses/>
"""
Created on 13 Feb 2011

@author: Mike Thomas
"""
from PyQt4.QtGui import QUndoCommand

import DBMidi
from Data import DBConstants
from Data.NotePosition import NotePosition
from Data.Measure import Measure
import DBVersion


class ScoreCommand(QUndoCommand):
    canReformat = True

    def __init__(self, qScore, note, description):
        super(ScoreCommand, self).__init__(description)
        self.description = description
        self._qScore = qScore
        if note is not None:
            self._np = note.makeCopy()
        else:
            self._np = note
        self._score = self._qScore.score

    def undo(self):
        self._undo()

    def _undo(self):
        raise NotImplementedError()

    def redo(self):
        self._redo()

    def _redo(self):
        raise NotImplementedError()


class CheckUndo(ScoreCommand):
    def __init__(self, qScore):
        super(CheckUndo, self).__init__(qScore, None, None)
        self._hash = None

    if DBVersion.FULL_RELEASE:
        def _undo(self):
            pass

        def _redo(self):
            pass
    else:
        def _undo(self):
            newHash = self._score.hashScore()
            print newHash.encode('hex'), self._hash.encode('hex')
            assert (newHash == self._hash)

        def _redo(self):
            self._hash = self._score.hashScore()


class DebugScoreCommand(ScoreCommand):  # pylint:disable-msg=W0223
    def __init__(self, qScore, note, description):
        super(DebugScoreCommand, self).__init__(qScore, note, description)
        self._hash = self._score.hashScore()

    def undo(self):
        super(DebugScoreCommand, self).undo()
        newHash = self._score.hashScore()
        print newHash.encode('hex'), self._hash.encode('hex')
        assert (newHash == self._hash)


class SaveFormatStateCommand(ScoreCommand):
    def __init__(self, qscore):
        super(SaveFormatStateCommand, self).__init__(qscore, None, None)

    def _undo(self):
        self._qScore.checkFormatting()

    def _redo(self):
        self._score.saveFormatState()


class CheckFormatStateCommand(ScoreCommand):
    def __init__(self, qscore):
        super(CheckFormatStateCommand, self).__init__(qscore, None, None)

    def _undo(self):
        self._score.saveFormatState()

    def _redo(self):
        self._qScore.checkFormatting()


class NoteCommand(ScoreCommand):  # pylint:disable-msg=W0223
    canReformat = False

    def __init__(self, qScore, notePosition, head=None):
        super(NoteCommand, self).__init__(qScore, notePosition,
                                          "set note")
        if head is None:
            head = self._score.drumKit.getDefaultHead(notePosition.drumIndex)
        self._oldHead = self._score.getItemAtPosition(notePosition)
        self._head = head

    def _undo(self):
        if self._oldHead == DBConstants.EMPTY_NOTE:
            self._score.deleteNote(self._np)
        else:
            self._score.addNote(self._np, self._oldHead)
            DBMidi.playNote(self._np.drumIndex, self._oldHead)


class SetNote(NoteCommand):
    def _redo(self):
        self._score.addNote(self._np, self._head)
        if self._head != DBConstants.EMPTY_NOTE:
            DBMidi.playNote(self._np.drumIndex, self._head)


class ToggleNote(NoteCommand):
    def _redo(self):
        self._score.toggleNote(self._np, self._head)
        newHead = self._score.getItemAtPosition(self._np)
        if (newHead != DBConstants.EMPTY_NOTE):
            DBMidi.playNote(self._np.drumIndex, self._head)


class MetaDataCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, varName, signal, value):
        super(MetaDataCommand, self).__init__(qScore, None,
                                              "edit metadata")
        self._oldValue = getattr(self._score.scoreData, varName)
        self._varname = varName
        self._signal = signal
        self._value = value

    def _redo(self):
        with self._qScore.metaChange():
            setattr(self._score.scoreData, self._varname, self._value)
            self._signal.emit(self._varname, self._value)


    def _undo(self):
        with self._qScore.metaChange():
            setattr(self._score.scoreData, self._varname, self._oldValue)
            self._signal.emit(self._varname, self._oldValue)


class SetLilypondSizeCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, size):
        super(SetLilypondSizeCommand, self).__init__(qScore, None,
                                                     "set Lilypond size")
        self._oldValue = self._score.lilysize
        self._newValue = size

    def _redo(self):
        if self._score.lilysize != self._newValue:
            self._score.lilysize = self._newValue
            self._qScore.lilysizeChanged.emit(self._newValue)

    def _undo(self):
        if self._score.lilysize != self._oldValue:
            self._score.lilysize = self._oldValue
            self._qScore.lilysizeChanged.emit(self._oldValue)


class SetLilypondPagesCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, numPages):
        super(SetLilypondPagesCommand, self).__init__(qScore, None,
                                                      "set Lilypond pages")
        self._oldValue = self._score.lilypages
        self._newValue = numPages

    def _redo(self):
        if self._score.lilypages != self._newValue:
            self._score.lilypages = self._newValue
            self._qScore.lilypagesChanged.emit(self._newValue)

    def _undo(self):
        if self._score.lilypages != self._oldValue:
            self._score.lilypages = self._oldValue
            self._qScore.lilypagesChanged.emit(self._oldValue)


class SetLilypondFillCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, lilyFill):
        super(SetLilypondFillCommand, self).__init__(qScore, None,
                                                     "set Lilypond fill")
        self._oldValue = self._score.lilyFill
        self._newValue = lilyFill

    def _redo(self):
        if self._score.lilyFill != self._newValue:
            self._score.lilyFill = self._newValue
            self._qScore.lilyFillChanged.emit(self._newValue)

    def _undo(self):
        if self._score.lilyFill != self._oldValue:
            self._score.lilyFill = self._oldValue
            self._qScore.lilyFillChanged.emit(self._oldValue)


class ScoreWidthCommand(ScoreCommand):
    def __init__(self, qScore, value):
        super(ScoreWidthCommand, self).__init__(qScore, None,
                                                "set width")
        self._oldValue = self._score.scoreData.width
        self._value = value

    def _redo(self):
        self._score.scoreData.width = self._value
        for view in self._qScore.views():
            view.setWidth(self._value)

    def _undo(self):
        self._score.scoreData.width = self._oldValue
        for view in self._qScore.views():
            view.setWidth(self._oldValue)


class InsertAndPasteMeasures(ScoreCommand):
    def __init__(self, qScore, startPosition, measureData):
        super(InsertAndPasteMeasures, self).__init__(qScore, startPosition,
                                                     "insert copied measures")
        self._startPosition = startPosition
        self._measureData = measureData

    def _redo(self):
        np = self._startPosition
        for measure in reversed(self._measureData):
            self._score.insertMeasureByPosition(len(measure), np,
                                                measure.counter)
            self._score.pasteMeasure(np, measure)

    def _undo(self):
        self._score.deleteMeasuresAtPosition(self._startPosition,
                                             len(self._measureData))


class PasteMeasuresCommand(ScoreCommand):
    def __init__(self, qScore, startPosition, measureData):
        super(PasteMeasuresCommand, self).__init__(qScore, startPosition,
                                                   "paste measures")
        self._startPosition = startPosition
        self._measureData = measureData

    def _exchange(self):
        oldData = []
        np = self._startPosition
        for measure in self._measureData:
            oldData.append(self._score.copyMeasure(np))
            self._score.pasteMeasure(np, measure)
            np = self._score.nextMeasure(np)
        return oldData

    def _redo(self):
        self._measureData = self._exchange()

    def _undo(self):
        self._measureData = self._exchange()


class RepeatNoteCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, firstNote, nRepeats, repInterval):
        super(RepeatNoteCommand, self).__init__(qScore, firstNote,
                                                "repeat note")
        self._head = self._score.getItemAtPosition(firstNote)
        note = firstNote.makeCopy()
        self._oldNotes = [(note, self._score.getItemAtPosition(note))]
        for dummyIndex in range(nRepeats):
            note = note.makeCopy()
            note = self._score.notePlus(note, repInterval)
            self._oldNotes.append((note, self._score.getItemAtPosition(note)))

    def _redo(self):
        for np, dummyHead in self._oldNotes:
            self._score.addNote(np, self._head)

    def _undo(self):
        for np, head in self._oldNotes:
            if head == DBConstants.EMPTY_NOTE:
                self._score.deleteNote(np)
            else:
                self._score.addNote(np, head)


class InsertMeasuresCommand(ScoreCommand):
    def __init__(self, qScore, notePosition, numMeasures,
                 counter, preserveSections=False):
        super(InsertMeasuresCommand, self).__init__(qScore, notePosition,
                                                    "insert measures")
        self._index = self._score.getMeasureIndex(self._np)
        self._numMeasures = numMeasures
        self._width = len(counter)
        self._counter = counter
        self._preserveSections = preserveSections

    def _redo(self):
        moveEnd = False
        if self._preserveSections and self._index > 0:
            measure = self._score.getMeasure(self._index - 1)
            moveEnd = measure.isSectionEnd()
            if moveEnd:
                measure.setSectionEnd(False)
        for dummyMeasureIndex in range(self._numMeasures):
            self._score.insertMeasureByIndex(self._width, self._index,
                                             counter=self._counter)
        if moveEnd:
            measure = self._score.getMeasure(self._index +
                                             self._numMeasures - 1)
            measure.setSectionEnd(True)

    def _undo(self):
        if self._preserveSections and self._index > 0:
            measure = self._score.getMeasure(self._index +
                                             self._numMeasures - 1)
            if measure.isSectionEnd():
                measure.setSectionEnd(False)
                measure = self._score.getMeasure(self._index - 1)
                measure.setSectionEnd(True)
        for dummyMeasureIndex in range(self._numMeasures):
            self._score.deleteMeasureByIndex(self._index)


class InsertSectionCommand(ScoreCommand):
    def __init__(self, qScore, note, sectionIndex):
        super(InsertSectionCommand, self).__init__(qScore, note,
                                                   "insert section copy")
        self._np.measureIndex = 0
        self._np = self._np.makeMeasurePosition()
        self._np.staffIndex = self._score.getSectionStartStaffIndex(note)
        self._index = sectionIndex

    def _redo(self):
        self._score.insertSectionCopy(self._np,
                                      self._index)
        self._qScore.sectionsChanged.emit()

    def _undo(self):
        self._score.deleteSection(self._np)
        self._qScore.sectionsChanged.emit()


class SetRepeatCountCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, notePosition, oldCount, newCount):
        super(SetRepeatCountCommand, self).__init__(qScore, notePosition,
                                                    "set repeat count")
        self._oldCount = oldCount
        self._newCount = newCount

    def _redo(self):
        measure = self._score.getItemAtPosition(self._np)
        measure.repeatCount = self._newCount
        if self._qScore.getQStaff(self._np).checkAlternate():
            self._qScore.reBuild()

    def _undo(self):
        measure = self._score.getItemAtPosition(self._np)
        measure.repeatCount = self._oldCount
        if self._qScore.getQStaff(self._np).checkAlternate():
            self._qScore.reBuild()


class EditMeasurePropertiesCommand(ScoreCommand):
    def __init__(self, qScore, note, newCounter):
        name = "edit measure properties"
        super(EditMeasurePropertiesCommand, self).__init__(qScore,
                                                           note,
                                                           name)
        self._measureIndex = self._score.getMeasureIndex(note)
        self._newCounter = newCounter
        self._oldMeasure = self._score.copyMeasure(note)

    def _redo(self):
        measure = self._score.getItemAtPosition(self._np)
        measure.setBeatCount(self._newCounter)

    def _undo(self):
        self._score.pasteMeasureByIndex(self._measureIndex, self._oldMeasure,
                                        True)


class SetMeasureLineCommand(ScoreCommand):
    def __init__(self, qScore, descr, note, onOff, method):
        super(SetMeasureLineCommand, self).__init__(qScore, note,
                                                    descr)
        self._onOff = onOff
        self._method = method
        self._np = self._np.makeMeasurePosition()

    def _getMeasure(self):
        return self._score.getItemAtPosition(self._np)

    def _redo(self):
        self._method(self._getMeasure(), self._onOff)
        self._qScore.reBuild()

    def _undo(self):
        self._method(self._getMeasure(), not self._onOff)
        self._qScore.reBuild()


class SetSectionEndCommand(SetMeasureLineCommand):
    def __init__(self, qScore, note, onOff):
        super(SetSectionEndCommand, self).__init__(qScore,
                                                   "set section end",
                                                   note, onOff,
                                                   None)
        if not onOff:
            self._index = self._score.getSectionIndex(note)
            self._title = self._score.getSectionTitle(self._index)

    def _undo(self):
        self._score.setSectionEnd(self._np, not self._onOff)
        self._qScore.reBuild()
        if not self._onOff:
            self._score.setSectionTitle(self._index, self._title)
        self._qScore.sectionsChanged.emit()

    def _redo(self):
        self._score.setSectionEnd(self._np, self._onOff)
        self._qScore.reBuild()
        self._qScore.sectionsChanged.emit()


class SetLineBreakCommand(SetMeasureLineCommand):
    def __init__(self, qScore, note, onOff):
        super(SetLineBreakCommand, self).__init__(qScore,
                                                  "set line break",
                                                  note, onOff,
                                                  Measure.setLineBreak)


class SetRepeatStartCommand(SetMeasureLineCommand):
    canReformat = False

    def __init__(self, qScore, note, onOff):
        super(SetRepeatStartCommand, self).__init__(qScore,
                                                    "set repeat start",
                                                    note, onOff,
                                                    Measure.setRepeatStart)


class SetRepeatEndCommand(SetMeasureLineCommand):
    canReformat = False

    def __init__(self, qScore, note, onOff):
        super(SetRepeatEndCommand, self).__init__(qScore,
                                                  "set repeat end",
                                                  note, onOff,
                                                  Measure.setRepeatEnd)
        self._repeatCount = self._getMeasure().repeatCount

    def _undo(self):
        super(SetRepeatEndCommand, self)._undo()
        if not self._onOff:
            self._getMeasure().repeatCount = self._repeatCount


class ClearMeasureCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, positions):
        super(ClearMeasureCommand, self).__init__(qScore, NotePosition(),
                                                  "clear measures")
        self._positions = [np.makeMeasurePosition() for np in positions]
        self._oldMeasures = [self._score.copyMeasure(note)
                             for note in positions]

    def _redo(self):
        for np in self._positions:
            self._score.getItemAtPosition(np).clear()

    def _undo(self):
        for np, data in zip(self._positions, self._oldMeasures):
            self._score.pasteMeasure(np, data)


class DeleteMeasureCommand(ScoreCommand):
    def __init__(self, qScore, note, measureIndex=None):
        if measureIndex is None:
            measureIndex = qScore.score.getMeasureIndex(note)
            note = note.makeMeasurePosition()
        else:
            note = qScore.score.getMeasurePosition(measureIndex)
        super(DeleteMeasureCommand, self).__init__(qScore, note,
                                                   "delete measure")
        self._index = measureIndex
        self._oldMeasure = self._score.copyMeasure(note)
        self._sectionIndex = None
        self._sectionTitle = None
        if self._oldMeasure.isSectionEnd():
            self._sectionIndex = self._score.getSectionIndex(note)
            self._sectionTitle = self._score.getSectionTitle(self._sectionIndex)

    def _redo(self):
        self._score.deleteMeasureByPosition(self._np)
        if self._sectionIndex:
            self._qScore.sectionsChanged.emit()

    def _undo(self):
        self._score.turnOffCallBacks()
        try:
            self._score.insertMeasureByIndex(len(self._oldMeasure), self._index)
            self._score.formatScore()
            if self._sectionIndex is not None:
                self._score.setSectionEnd(self._np, True)
                self._score.setSectionTitle(self._sectionIndex,
                                            self._sectionTitle)
                self._score.formatScore()
                self._qScore.sectionsChanged.emit()
            self._score.pasteMeasureByIndex(self._index, self._oldMeasure, True)
        finally:
            self._score.turnOnCallBacks()


class SetSectionTitleCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, sectionIndex, title):
        super(SetSectionTitleCommand, self).__init__(qScore,
                                                     None,
                                                     "set section title")
        self._index = sectionIndex
        self._oldTitle = self._score.getSectionTitle(sectionIndex)
        self._title = title

    def _redo(self):
        self._score.setSectionTitle(self._index,
                                    self._title)
        self._qScore.setSectionTitle(self._index,
                                     self._title)
        self._qScore.sectionsChanged.emit()

    def _undo(self):
        self._score.setSectionTitle(self._index,
                                    self._oldTitle)
        self._qScore.setSectionTitle(self._index,
                                     self._oldTitle)
        self._qScore.sectionsChanged.emit()


class SetAlternateCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, note, alternate):
        super(SetAlternateCommand, self).__init__(qScore,
                                                  note,
                                                  "set alternate text")
        self._alternate = alternate
        self._np.noteTime = None
        self._np.drumIndex = None
        measure = self._score.getItemAtPosition(self._np)
        self._oldAlternate = measure.alternateText

    def _redo(self):
        measure = self._score.getItemAtPosition(self._np)
        measure.alternateText = self._alternate
        self._qScore.dataChanged(self._np)
        if self._qScore.getQStaff(self._np).checkAlternate():
            self._qScore.reBuild()

    def _undo(self):
        measure = self._score.getItemAtPosition(self._np)
        measure.alternateText = self._oldAlternate
        self._qScore.dataChanged(self._np)
        if self._qScore.getQStaff(self._np).checkAlternate():
            self._qScore.reBuild()


class SetPaperSizeCommand(ScoreCommand):
    def __init__(self, qScore, newPaperSize):
        super(SetPaperSizeCommand, self).__init__(qScore,
                                                  NotePosition(),
                                                  "set page size")
        self._new = newPaperSize
        self._old = self._score.paperSize

    def _redo(self):
        self._score.paperSize = self._new
        self._qScore.paperSizeChanged.emit(self._new)

    def _undo(self):
        self._score.paperSize = self._old
        self._qScore.paperSizeChanged.emit(self._old)


class SetDefaultCountCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, newCount):
        super(SetDefaultCountCommand, self).__init__(qScore,
                                                     NotePosition(),
                                                     "set default count")
        self._new = newCount
        self._old = self._score.defaultCount

    def _redo(self):
        self._score.defaultCount = self._new
        self._qScore.defaultCountChanged.emit(self._new)

    def _undo(self):
        self._score.defaultCount = self._old
        self._qScore.defaultCountChanged.emit(self._old)


class SetSystemSpacingCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, newSpacing):
        super(SetSystemSpacingCommand, self).__init__(qScore,
                                                      NotePosition(),
                                                      "set system spacing")
        self._new = newSpacing
        self._old = self._score.systemSpacing

    def _redo(self):
        self._score.systemSpacing = self._new
        self._qScore.displayProperties.lineSpacing = self._new - 101
        self._qScore.spacingChanged.emit(self._new)

    def _undo(self):
        self._score.systemSpacing = self._old
        self._qScore.displayProperties.lineSpacing = self._old - 101
        self._qScore.spacingChanged.emit(self._old)


class SetFontSizeCommand(ScoreCommand):
    def __init__(self, qScore, newSize, fontType):
        super(SetFontSizeCommand, self).__init__(qScore,
                                                 NotePosition(),
                                                 "set " + fontType +
                                                 " font size")
        self._fontName = fontType + "FontSize"
        self._newSize = newSize
        self._oldSize = getattr(self._qScore.displayProperties,
                                self._fontName)

    def _redo(self):
        setattr(self._qScore.displayProperties, self._fontName, self._newSize)

    def _undo(self):
        setattr(self._qScore.displayProperties, self._fontName, self._oldSize)


class SetFontCommand(ScoreCommand):
    def __init__(self, qScore, font, fontType):
        super(SetFontCommand, self).__init__(qScore,
                                             NotePosition(),
                                             "set " + fontType + " font")
        self._newFont = font
        self._fontName = fontType + "Font"
        self._oldFont = getattr(self._qScore.displayProperties,
                                self._fontName)

    def _redo(self):
        setattr(self._qScore.displayProperties, self._fontName, self._newFont)

    def _undo(self):
        setattr(self._qScore.displayProperties, self._fontName, self._oldFont)


class SetVisibilityCommand(ScoreCommand):
    canReformat = False

    def __init__(self, qScore, onOff, elementName, text):
        super(SetVisibilityCommand, self).__init__(qScore,
                                                   NotePosition(),
                                                   "change " + text +
                                                   " visibility")
        self._name = elementName + "Visible"
        self._new = onOff

    def _redo(self):
        setattr(self._qScore.displayProperties, self._name, self._new)

    def _undo(self):
        setattr(self._qScore.displayProperties, self._name, not self._new)
