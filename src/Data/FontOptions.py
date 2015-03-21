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
Created on 5 Sep 2011

@author: Mike Thomas

"""


class FontOptions(object):
    def __init__(self):
        self.noteFontSize = 10
        self.noteFont = "MS Shell Dlg 2"
        self.sectionFontSize = 14
        self.sectionFont = "MS Shell Dlg 2"
        self.metadataFontSize = 16
        self.metadataFont = "MS Shell Dlg 2"

    def write(self, indenter):
        with indenter.section("FONT_OPTIONS_START", "FONT_OPTIONS_END"):
            indenter("NOTEFONT", self.noteFont)
            indenter("NOTEFONTSIZE %d" % self.noteFontSize)
            indenter("SECTIONFONT", self.sectionFont)
            indenter("SECTIONFONTSIZE %d" % self.sectionFontSize)
            indenter("METADATAFONT", self.metadataFont)
            indenter("METADATAFONTSIZE %d" % self.metadataFontSize)

    def read(self, scoreIterator):
        with scoreIterator.section("FONT_OPTIONS_START",
                                   "FONT_OPTIONS_END") as section:
            section.readString("NOTEFONT", self, "noteFont")
            section.readPositiveInteger("NOTEFONTSIZE", self, "noteFontSize")
            section.readString("SECTIONFONT", self, "sectionFont")
            section.readPositiveInteger("SECTIONFONTSIZE", self,
                                        "sectionFontSize")
            section.readString("METADATAFONT", self, "metadataFont")
            section.readPositiveInteger("METADATAFONTSIZE", self,
                                        "metadataFontSize")
