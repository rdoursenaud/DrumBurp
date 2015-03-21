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
Created on 12 Dec 2010

@author: Mike Thomas
"""
import unittest
from Data.Staff import Staff
from Data.Measure import Measure
from Data.DBConstants import EMPTY_NOTE
from Data.DBErrors import BadTimeError
from Data.NotePosition import NotePosition

# pylint: disable-msg=R0904

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff()

    def testEmptyStaff(self):
        self.assertEqual(self.staff.numMeasures(), 0)
        self.assertEqual(len(self.staff), 0)

    def testAddMeasure(self):
        self.staff.addMeasure(Measure(1))
        self.assertEqual(self.staff.numMeasures(), 1)
        self.assertEqual(len(self.staff), 1)
        self.staff.addMeasure(Measure(2))
        self.assertEqual(self.staff.numMeasures(), 2)
        self.assertEqual(len(self.staff), 3)

    def testIterateOverMeasures(self):
        for i in range(1, 16):
            self.staff.addMeasure(Measure(i))
        for i, measure in enumerate(self.staff):
            self.assertEqual(len(measure), i + 1)

    def testGetMeasureByIndex(self):
        for i in range(1, 16):
            self.staff.addMeasure(Measure(i))
        for i in range(1, 16):
            self.assertEqual(len(self.staff[i - 1]), i)

    def testDeleteLastMeasure(self):
        self.staff.addMeasure(Measure(1))
        self.staff.addMeasure(Measure(2))
        self.staff.addMeasure(Measure(3))
        self.staff.addMeasure(Measure(4))
        self.assertEqual(self.staff.numMeasures(), 4)
        self.staff.deleteLastMeasure()
        self.assertEqual(self.staff.numMeasures(), 3)
        for index in range(1, 4):
            self.assertEqual(len(self.staff[index - 1]), index)


    def testDeleteMeasure(self):
        self.staff.addMeasure(Measure(1))
        self.staff.addMeasure(Measure(2))
        self.staff.deleteMeasure(NotePosition(measureIndex = 0))
        self.assertEqual(self.staff.numMeasures(), 1)
        self.assertEqual(len(self.staff), 2)

    def testDeleteMeasure_BadIndex(self):
        self.staff.addMeasure(Measure(1))
        self.staff.addMeasure(Measure(2))
        self.assertRaises(BadTimeError, self.staff.deleteMeasure,
                          NotePosition(measureIndex = -1))
        self.assertRaises(BadTimeError, self.staff.deleteMeasure,
                          NotePosition(measureIndex = 2))

    def testInsertMeasure(self):
        self.staff.addMeasure(Measure(1))
        self.staff.addMeasure(Measure(3))
        self.staff.insertMeasure(NotePosition(measureIndex = 1), Measure(2))
        for i, measure in enumerate(self.staff):
            self.assertEqual(len(measure), i + 1)

    def testInsertMeasureAtStart(self):
        self.staff.addMeasure(Measure(2))
        self.staff.insertMeasure(NotePosition(measureIndex = 0), Measure(1))
        for i, measure in enumerate(self.staff):
            self.assertEqual(len(measure), i + 1)

    def testInsertMeasureAtEnd(self):
        self.staff.addMeasure(Measure(1))
        self.staff.insertMeasure(NotePosition(measureIndex = 1), Measure(2))
        for i, measure in enumerate(self.staff):
            self.assertEqual(len(measure), i + 1)

    def testInsertMeasure_BadIndex(self):
        self.staff.addMeasure(Measure(1))
        self.staff.addMeasure(Measure(2))
        m = Measure(3)
        self.assertRaises(BadTimeError,
                          self.staff.insertMeasure,
                          NotePosition(measureIndex = -1), m)
        self.assertRaises(BadTimeError,
                          self.staff.insertMeasure,
                          NotePosition(measureIndex = 3), m)

    def testClearStaff(self):
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.staff.clear()
        self.assertEqual(len(self.staff), 0)
        self.assertEqual(self.staff.numMeasures(), 0)

    def testGridWidth_EmptyStaff(self):
        self.assertEqual(self.staff.gridWidth(), 0)

    def testGridWidth(self):
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.assertEqual(self.staff.gridWidth(), 52)
        endMeasure = Measure(16)
        endMeasure.setSectionEnd(True)
        self.staff.addMeasure(endMeasure)
        self.assertEqual(self.staff.gridWidth(), 69)


class TestNoteControl(unittest.TestCase):
    def setUp(self):
        self.staff = Staff()
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))

    def testgetItemAtPosition(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.assertEqual(self.staff.getItemAtPosition(np),
                         EMPTY_NOTE)

    def testGetItemAtPosition(self):
        np = NotePosition(measureIndex = 0,
                          noteTime = 0,
                          drumIndex = 0)
        self.assertEqual(self.staff.getItemAtPosition(np),
                         EMPTY_NOTE)

    def testgetItemAtPosition_BadTime(self):
        self.assertRaises(BadTimeError, self.staff.getItemAtPosition,
                          NotePosition(measureIndex = -1,
                                       noteTime = 0, drumIndex = 0))
        self.assertRaises(BadTimeError, self.staff.getItemAtPosition,
                          NotePosition(measureIndex = 20,
                                       noteTime = 0, drumIndex = 0))
        self.assertRaises(BadTimeError, self.staff.getItemAtPosition,
                          NotePosition(measureIndex = 0,
                                       noteTime = -1, drumIndex = 0))
        self.assertRaises(BadTimeError, self.staff.getItemAtPosition,
                          NotePosition(measureIndex = 0,
                                       noteTime = 20, drumIndex = 0))

    def testAddNote(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.staff.addNote(np, "o")
        self.assertEqual(self.staff.getItemAtPosition(np), "o")

    def testAddNote_BadTime(self):
        self.assertRaises(BadTimeError, self.staff.addNote,
                          NotePosition(measureIndex = -1,
                                       noteTime = 0, drumIndex = 0), "x")
        self.assertRaises(BadTimeError, self.staff.addNote,
                          NotePosition(measureIndex = 4,
                                       noteTime = 0, drumIndex = 0), "x")
        self.assertRaises(BadTimeError, self.staff.addNote,
                          NotePosition(measureIndex = 0,
                                       noteTime = -1, drumIndex = 0), "x")
        self.assertRaises(BadTimeError, self.staff.addNote,
                          NotePosition(measureIndex = 0,
                                       noteTime = 20, drumIndex = 0), "x")

    def testDeleteNote(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.staff.addNote(np, "o")
        self.staff.deleteNote(np)
        self.assertEqual(self.staff.getItemAtPosition(np), EMPTY_NOTE)

    def testDeleteNote_BadTime(self):
        self.assertRaises(BadTimeError, self.staff.deleteNote,
                          NotePosition(measureIndex = -1,
                                       noteTime = 0, drumIndex = 0))
        self.assertRaises(BadTimeError, self.staff.deleteNote,
                          NotePosition(measureIndex = 20,
                                       noteTime = 0, drumIndex = 0))
        self.assertRaises(BadTimeError, self.staff.deleteNote,
                          NotePosition(measureIndex = 0,
                                       noteTime = -1, drumIndex = 0))
        self.assertRaises(BadTimeError, self.staff.deleteNote,
                          NotePosition(measureIndex = 0,
                                       noteTime = 20, drumIndex = 0))

    def testToggleNote(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.staff.toggleNote(np, "o")
        self.assertEqual(self.staff.getItemAtPosition(np), "o")
        self.staff.toggleNote(np, "o")
        self.assertEqual(self.staff.getItemAtPosition(np), EMPTY_NOTE)

    def testToggleNote_BadTime(self):
        self.assertRaises(BadTimeError, self.staff.toggleNote,
                          NotePosition(measureIndex = -1,
                                       noteTime = 0, drumIndex = 0), "x")
        self.assertRaises(BadTimeError, self.staff.toggleNote,
                          NotePosition(measureIndex = 20,
                                       noteTime = 0, drumIndex = 0), "x")
        self.assertRaises(BadTimeError, self.staff.toggleNote,
                          NotePosition(measureIndex = 0,
                                       noteTime = -1, drumIndex = 0), "x")
        self.assertRaises(BadTimeError, self.staff.toggleNote,
                          NotePosition(measureIndex = 0,
                                       noteTime = 20, drumIndex = 0), "x")

class TestMeasureControl(unittest.TestCase):
    def setUp(self):
        self.staff = Staff()
        self.staff.addMeasure(Measure(1))
        self.staff.addMeasure(Measure(2))
        self.staff.addMeasure(Measure(3))
        self.staff.addMeasure(Measure(4))
        self.np = NotePosition(measureIndex = 2)

    def testGetItemAtPosition(self):
        measure = self.staff.getItemAtPosition(self.np)
        self.assertEqual(len(measure), 3)

    def testSetSectionEnd(self):
        measure = self.staff.getItemAtPosition(self.np)
        self.assertFalse(measure.isSectionEnd())
        self.staff.setSectionEnd(self.np, True)
        self.assertTrue(measure.isSectionEnd())
        self.staff.setSectionEnd(self.np, False)
        self.assertFalse(measure.isSectionEnd())

    def testIsSectionEnd(self):
        self.assertFalse(self.staff.isSectionEnd())
        self.staff.setSectionEnd(self.np, True)
        self.assertFalse(self.staff.isSectionEnd())
        self.staff.setSectionEnd(self.np, False)
        self.assertFalse(self.staff.isSectionEnd())
        endPos = NotePosition(measureIndex = 3)
        self.staff.setSectionEnd(endPos, True)
        self.assertTrue(self.staff.isSectionEnd())
        self.staff.setSectionEnd(endPos, False)
        self.assertFalse(self.staff.isSectionEnd())

    def testIsConsistent(self):
        self.assertTrue(self.staff.isConsistent())
        self.staff.setSectionEnd(self.np, True)
        self.assertFalse(self.staff.isConsistent())
        self.staff.setSectionEnd(self.np, False)
        self.assertTrue(self.staff.isConsistent())
        endPos = NotePosition(measureIndex = 3)
        self.staff.setSectionEnd(endPos, True)
        self.assertTrue(self.staff.isConsistent())
        self.staff.setSectionEnd(endPos, False)
        self.assertTrue(self.staff.isConsistent())

    def testCopyPasteWithoutDecoration(self):
        measure = self.staff.getItemAtPosition(self.np)
        measure.setRepeatStart(True)
        copied = self.staff.copyMeasure(self.np)
        newPos = NotePosition(measureIndex = 0)
        self.assertFalse(self.staff[0].isRepeatStart())
        self.assertEqual(len(self.staff[0]), 1)
        self.staff.pasteMeasure(newPos, copied, False)
        self.assertFalse(self.staff[0].isRepeatStart())
        self.assertEqual(len(self.staff[0]), 3)

    def testCopyPasteWithDecoration(self):
        measure = self.staff.getItemAtPosition(self.np)
        measure.setRepeatStart(True)
        copied = self.staff.copyMeasure(self.np)
        newPos = NotePosition(measureIndex = 0)
        self.assertFalse(self.staff[0].isRepeatStart())
        self.assertEqual(len(self.staff[0]), 1)
        self.staff.pasteMeasure(newPos, copied, True)
        self.assertTrue(self.staff[0].isRepeatStart())
        self.assertEqual(len(self.staff[0]), 3)

    def testLineIsVisible(self):
        self.staff.addNote(NotePosition(measureIndex = 0, noteTime = 0,
                                        drumIndex = 0), "x")
        self.staff.addNote(NotePosition(measureIndex = 1, noteTime = 0,
                                        drumIndex = 2), "x")
        self.staff.addNote(NotePosition(measureIndex = 2, noteTime = 0,
                                        drumIndex = 4), "x")
        self.assertTrue(self.staff.lineIsVisible(0))
        self.assertFalse(self.staff.lineIsVisible(1))
        self.assertTrue(self.staff.lineIsVisible(2))
        self.assertFalse(self.staff.lineIsVisible(3))
        self.assertTrue(self.staff.lineIsVisible(4))
        self.assertFalse(self.staff.lineIsVisible(5))


class TestCallBack(unittest.TestCase):
    def setUp(self):
        self.staff = Staff()
        self.staff.addMeasure(Measure(16))
        self.calls = []
        def myCallBack(position):
            self.calls.append((position.measureIndex,
                               position.noteTime,
                               position.drumIndex))
        self.staff.setCallBack(myCallBack)

    def testAddNoteCallBack(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.staff.addNote(np, "x")
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(self.calls[0], (0, 0, 0))
        self.staff.addNote(np, "x")
        self.assertEqual(len(self.calls), 1)
        self.staff.addNote(np, "o")
        self.assertEqual(len(self.calls), 2)
        self.assertEqual(self.calls[1], (0, 0, 0))

    def testDeleteNoteCallBack(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.staff.deleteNote(np)
        self.assertEqual(len(self.calls), 0)
        self.staff.addNote(np, "x")
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(self.calls[0], (0, 0, 0))
        self.staff.deleteNote(np)
        self.assertEqual(len(self.calls), 2)
        self.assertEqual(self.calls[1], (0, 0, 0))

    def testToggleNoteCallBack(self):
        np = NotePosition(measureIndex = 0, noteTime = 0, drumIndex = 0)
        self.staff.toggleNote(np, "x")
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(self.calls[0], (0, 0, 0))
        self.staff.toggleNote(np, "x")
        self.assertEqual(len(self.calls), 2)
        self.assertEqual(self.calls[1], (0, 0, 0))
        self.staff.toggleNote(np, "x")
        self.assertEqual(len(self.calls), 3)
        self.assertEqual(self.calls[2], (0, 0, 0))
        self.staff.toggleNote(np, "o")
        self.assertEqual(len(self.calls), 4)
        self.assertEqual(self.calls[2], (0, 0, 0))

    def testClearCallBack(self):
        self.staff.clearCallBack()
        self.staff.addNote(NotePosition(measureIndex = 0,
                                        noteTime = 0,
                                        drumIndex = 0), "x")
        self.assertEqual(len(self.calls), 0)

    def testAddMeasureCallBack(self):
        np = NotePosition(measureIndex = 1, noteTime = 0, drumIndex = 0)
        self.staff.addMeasure(Measure(16))
        self.staff.addNote(np, "x")
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(self.calls[0], (1, 0, 0))

    def testDeleteMeasureCallBack(self):
        self.staff.addMeasure(Measure(16))
        self.staff.addMeasure(Measure(16))
        np = NotePosition(measureIndex = 1,
                          noteTime = 0,
                          drumIndex = 0)
        self.staff.addNote(np, "x")
        self.staff.deleteMeasure(NotePosition(measureIndex = 0))
        self.staff.deleteNote(NotePosition(measureIndex = 0,
                                           noteTime = 0,
                                           drumIndex = 0))
        self.staff.addNote(np, "x")
        self.assertEqual(len(self.calls), 3)
        self.assertEqual(self.calls[0], (1, 0, 0))
        self.assertEqual(self.calls[1], (0, 0, 0))
        self.assertEqual(self.calls[2], (1, 0, 0))

    def testInsertMeasureCallBack(self):
        np0 = NotePosition(measureIndex = 0,
                          noteTime = 0,
                          drumIndex = 0)
        np1 = NotePosition(measureIndex = 1,
                          noteTime = 0,
                          drumIndex = 0)
        self.staff.addNote(np0, "x")
        self.staff.insertMeasure(np0, Measure(8))
        self.staff.addNote(np0, "x")
        self.staff.deleteNote(np1)
        self.assertEqual(len(self.calls), 3)
        self.assertEqual(self.calls[0], (0, 0, 0))
        self.assertEqual(self.calls[1], (0, 0, 0))
        self.assertEqual(self.calls[2], (1, 0, 0))



if __name__ == "__main__":
    unittest.main()
