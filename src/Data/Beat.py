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
Created on 16 Apr 2011

@author: Mike Thomas

"""

import itertools

from Counter import CounterRegistry
from DBConstants import BEAT_COUNT
import DBErrors


class Beat(object):
    """A Beat is a measured instance of a Counter.

    A Beat may be less than the full length of the corresponding Counter to
    reflect partial beats at the end of a Measure. A sequence of Beats makes
    up a MeasureCount.
    """

    def __init__(self, counter, numTicks=None):
        self.counter = counter
        if numTicks is None:
            numTicks = self.ticksPerBeat
        self._numTicks = numTicks
        self._beatLength = float(self.numTicks) / self.ticksPerBeat

    def __iter__(self):
        for unusedTickNum, count in itertools.izip(self.iterTicks(),
                                                   self.counter):
            yield count

    def count(self, beatNum):
        for count in self:
            if count == BEAT_COUNT:
                yield str(beatNum)
            else:
                yield count

    def __str__(self):
        return str(self.counter)

    def iterTicks(self):
        return xrange(self.numTicks)

    def numBeats(self):
        return self._beatLength

    @property
    def ticksPerBeat(self):
        return len(self.counter)

    @property
    def numTicks(self):
        return self._numTicks

    def write(self, indenter):
        with indenter.section("BEAT_START", "BEAT_END"):
            if self.numTicks != self.ticksPerBeat:
                indenter("NUM_TICKS", self.numTicks)
            self.counter.write(indenter)

    @staticmethod
    def read(scoreIterator):
        targetValues = {"numTicks": None, "counter": None}
        registry = CounterRegistry()

        def readCount(lineData):
            if lineData[0] == "|" and lineData[-1] == "|":
                lineData = lineData[1:-1]
            lineData = BEAT_COUNT + lineData[1:]
            try:
                targetValues["counter"] = registry.findMaster(lineData)
            except KeyError:
                raise DBErrors.BadCount(scoreIterator)

        with scoreIterator.section("BEAT_START", "BEAT_END") as section:
            section.readPositiveInteger("NUM_TICKS", targetValues, "numTicks")
            section.readCallback("COUNT", readCount)
        return Beat(targetValues["counter"], targetValues["numTicks"])

