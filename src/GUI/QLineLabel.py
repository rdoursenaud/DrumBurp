'''
Created on 19 Jan 2011

@author: Mike Thomas
'''

from QEditKitDialog import QEditKitDialog
from PyQt4 import QtGui, QtCore

class QLineLabel(QtGui.QGraphicsItem):
    def __init__(self, drum, qScore, parent):
        super(QLineLabel, self).__init__(parent = None,
                                          scene = qScore)
        self._text = ""
        self._props = qScore.displayProperties
        self._rect = QtCore.QRectF(0, 0,
                                   self.cellWidth(),
                                   self.cellHeight())
        self._highlighted = False
        self.setText(drum.abbr)
        self.setToolTip(drum.name)
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def cellHeight(self):
        return self._props.ySpacing

    def cellWidth(self):
        return 2 * self._props.xSpacing

    def mouseDoubleClickEvent(self, event_):
        editDialog = QEditKitDialog(self.scene().score.drumKit,
                                    self.scene().parent())
        if editDialog.exec_():
            newKit, changes = editDialog.getNewKit()
            self.scene().score.changeKit(newKit, changes)
            self.scene().reBuild()
            self.scene().dirty = True

    def setText(self, text):
        self._text = text
        self.update()

    def setDimensions(self):
        self.prepareGeometryChange()
        self._rect.setBottomRight(QtCore.QPointF(self.cellWidth(),
                                                 self.cellHeight()))

    def xSpacingChanged(self):
        self.setDimensions()

    def ySpacingChanged(self):
        self.setDimensions()

    def boundingRect(self):
        return self._rect

    def paint(self, painter, dummyOption, dummyWidget = None):
        painter.save()
        painter.setPen(QtCore.Qt.NoPen)
        if len(self._text) > 0:
            painter.setPen(QtCore.Qt.SolidLine)
            font = self._props.noteFont
            if font is None:
                font = painter.font()
            else:
                painter.setFont(font)
            br = QtGui.QFontMetrics(font).tightBoundingRect(self._text)
            w = br.width()
            h = br.height()
            textLocation = QtCore.QPointF((self.cellWidth() - w + 2) / 2,
                                          (self.cellHeight() + h) / 2)
            painter.drawText(textLocation, self._text)
        if self._highlighted:
            painter.setPen(QtCore.Qt.SolidLine)
            painter.setPen(self.scene().palette().highlight().color())
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.drawRect(0, 0, self.cellWidth() - 1, self.cellHeight())
        painter.restore()

    def setHighlight(self, onOff):
        if onOff != self._highlighted:
            self._highlighted = onOff
            self.update()

