# Copyright 2012 Michael Thomas
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
Created on 7 Oct 2012

@author: Mike Thomas
"""

import DBErrors


class dbFileIterator(object):
    class _Section(object):
        def __init__(self, iterator, startLine, endLine, convertNone=None, readLines=None):
            self._iterator = iterator
            self._startLine = startLine
            self._endLine = endLine
            self._convertNone = convertNone
            self._lines = {}
            self._readLines = readLines
            self.lineNumber = 0
            self.currentLine = ""

        def __enter__(self):
            return self

        def _process(self):
            linesRead = 0
            for lineType, lineData in self._iterator:
                if lineData is None:
                    lineData = self._convertNone
                if lineType == self._startLine:
                    pass
                elif lineType == self._endLine:
                    break
                elif lineType in self._lines:
                    self._lines[lineType](lineData)
                else:
                    raise DBErrors.UnrecognisedLine(self._iterator)
                if self._readLines is not None:
                    linesRead += 1
                    if linesRead == self._readLines:
                        break


        def _parseInteger(self, data, lineName):
            try:
                data = int(data)
            except (TypeError, ValueError):
                raise DBErrors.InvalidInteger(self._iterator)
            return data

        def _parsePositiveInteger(self, data, lineName):
            data = self._parseInteger(data, lineName)
            if data <= 0:
                raise DBErrors.InvalidPositiveInteger(self._iterator)
            return data

        def _parseNonNegativeInteger(self, data, lineName):
            data = self._parseInteger(data, lineName)
            if data < 0:
                raise DBErrors.InvalidNonNegativeInteger(self._iterator)
            return data

        @staticmethod
        def _parseBoolean(data, unusedLineName):
            return (data == "True" or data.upper() == "YES")


        @staticmethod
        def _parseString(data, unusedLineName):
            return data

        @staticmethod
        def _updateDict(target, key, value):
            target[key] = value

        def _storeReader(self, lineType, target, attrName, parser):
            if isinstance(target, dict):
                setter = self._updateDict
            else:
                setter = setattr
            self._lines[lineType] = lambda data: setter(target, attrName,
                                                        parser(data, lineType))

        def readInteger(self, lineType, target, attrName):
            self._storeReader(lineType, target, attrName, self._parseInteger)

        def readPositiveInteger(self, lineType, target, attrName):
            self._storeReader(lineType, target, attrName,
                              self._parsePositiveInteger)

        def readNonNegativeInteger(self, lineType, target, attrName):
            self._storeReader(lineType, target, attrName,
                              self._parseNonNegativeInteger)

        def readBoolean(self, lineType, target, attrName):
            self._storeReader(lineType, target, attrName,
                              self._parseBoolean)

        def readString(self, lineType, target, attrName):
            self._storeReader(lineType, target, attrName,
                              self._parseString)

        def readSubsection(self, lineType, callback):
            self._lines[lineType] = lambda unused: callback(self._iterator)

        def readCallback(self, lineType, callback):
            self._lines[lineType] = callback

        def __exit__(self, excType, excValue, excTraceback):
            if excType is None:
                self._process()
            return False

    def __init__(self, handle):
        self._handle = handle

    def __iter__(self):
        for line_number, line in enumerate(self._handle):
            self.lineNumber = line_number
            line = line.strip()
            self.currentLine = line
            fields = line.split(None, 1)
            if len(fields) == 1:
                fields.append(None)
            elif len(fields) == 0:
                # Blank line
                continue
            lineType, lineData = fields
            lineType = lineType.upper()
            yield lineType, lineData

    def section(self, startLine, endLine, convertNone=None, readLines=None):
        return self._Section(self, startLine, endLine, convertNone, readLines)


class Indenter(object):
    class Section(object):
        def __init__(self, indenter, sectionStart, sectionEnd):
            self.indenter = indenter
            self.start = sectionStart
            self.end = sectionEnd

        def __enter__(self):
            self.indenter(self.start)
            self.indenter.increase()
            return self

        def __exit__(self, excType, excValue, excTraceback):
            self.indenter.decrease()
            self.indenter(self.end)
            return False

    def __init__(self, handle, indent="  "):
        self._indent = indent
        self._handle = handle
        self._level = 0

    def increase(self):
        self._level += 1

    def decrease(self):
        self._level -= 1
        self._level = max(0, self._level)

    def __call__(self, *args):
        argString = " ".join(str(ar) for ar in args)
        if self._level != 0:
            argString = (self._indent * self._level) + argString
        print >> self._handle, argString

    def __enter__(self):
        self.increase()
        return self

    def __exit__(self, excType, excValue, excTraceback):
        self.decrease()
        return False

    def section(self, sectionStart, sectionEnd):
        return self.Section(self, sectionStart, sectionEnd)
