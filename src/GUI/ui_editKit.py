# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\editKit.ui'
#
# Created: Sat Oct 13 21:00:08 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_editKitDialog(object):
    def setupUi(self, editKitDialog):
        editKitDialog.setObjectName(_fromUtf8("editKitDialog"))
        editKitDialog.resize(848, 592)
        self.verticalLayout_10 = QtGui.QVBoxLayout(editKitDialog)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_5 = QtGui.QGroupBox(editKitDialog)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.deleteEmptyButton = QtGui.QPushButton(self.groupBox_5)
        self.deleteEmptyButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteEmptyButton.sizePolicy().hasHeightForWidth())
        self.deleteEmptyButton.setSizePolicy(sizePolicy)
        self.deleteEmptyButton.setMinimumSize(QtCore.QSize(24, 24))
        self.deleteEmptyButton.setMaximumSize(QtCore.QSize(24, 24))
        self.deleteEmptyButton.setStatusTip(_fromUtf8(""))
        self.deleteEmptyButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/process-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEmptyButton.setIcon(icon)
        self.deleteEmptyButton.setObjectName(_fromUtf8("deleteEmptyButton"))
        self.horizontalLayout_4.addWidget(self.deleteEmptyButton)
        self.clearButton = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(24, 24))
        self.clearButton.setMaximumSize(QtCore.QSize(24, 24))
        self.clearButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_4.addWidget(self.clearButton)
        self.resetButton = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setMinimumSize(QtCore.QSize(24, 24))
        self.resetButton.setMaximumSize(QtCore.QSize(24, 24))
        self.resetButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/edit-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon2)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout_4.addWidget(self.resetButton)
        self.defaultKitButton = QtGui.QPushButton(self.groupBox_5)
        self.defaultKitButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/go-home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defaultKitButton.setIcon(icon3)
        self.defaultKitButton.setObjectName(_fromUtf8("defaultKitButton"))
        self.horizontalLayout_4.addWidget(self.defaultKitButton)
        self.loadButton = QtGui.QPushButton(self.groupBox_5)
        self.loadButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMinimumSize(QtCore.QSize(24, 24))
        self.loadButton.setMaximumSize(QtCore.QSize(24, 24))
        self.loadButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadButton.setIcon(icon4)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.horizontalLayout_4.addWidget(self.loadButton)
        self.saveButton = QtGui.QPushButton(self.groupBox_5)
        self.saveButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(24, 24))
        self.saveButton.setMaximumSize(QtCore.QSize(24, 24))
        self.saveButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/document-save.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.saveButton.setIcon(icon5)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.kitTable = QtGui.QListWidget(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kitTable.sizePolicy().hasHeightForWidth())
        self.kitTable.setSizePolicy(sizePolicy)
        self.kitTable.setMinimumSize(QtCore.QSize(256, 0))
        self.kitTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.kitTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.kitTable.setObjectName(_fromUtf8("kitTable"))
        self.verticalLayout_2.addWidget(self.kitTable)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.addButton = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(24, 24))
        self.addButton.setMaximumSize(QtCore.QSize(24, 24))
        self.addButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/GUI/Icons/list-add.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.addButton.setIcon(icon6)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout_5.addWidget(self.addButton)
        self.upButton = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMinimumSize(QtCore.QSize(24, 24))
        self.upButton.setMaximumSize(QtCore.QSize(24, 24))
        self.upButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/GUI/Icons/go-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upButton.setIcon(icon7)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.horizontalLayout_5.addWidget(self.upButton)
        self.downButton = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setMinimumSize(QtCore.QSize(24, 24))
        self.downButton.setMaximumSize(QtCore.QSize(24, 24))
        self.downButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/GUI/Icons/go-down.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.downButton.setIcon(icon8)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.horizontalLayout_5.addWidget(self.downButton)
        self.deleteButton = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(24, 24))
        self.deleteButton.setMaximumSize(QtCore.QSize(24, 24))
        self.deleteButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/GUI/Icons/list-remove.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon9)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_5.addWidget(self.deleteButton)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(editKitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.drumName = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drumName.sizePolicy().hasHeightForWidth())
        self.drumName.setSizePolicy(sizePolicy)
        self.drumName.setMinimumSize(QtCore.QSize(143, 0))
        self.drumName.setObjectName(_fromUtf8("drumName"))
        self.gridLayout_2.addWidget(self.drumName, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.drumAbbr = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drumAbbr.sizePolicy().hasHeightForWidth())
        self.drumAbbr.setSizePolicy(sizePolicy)
        self.drumAbbr.setMinimumSize(QtCore.QSize(143, 0))
        self.drumAbbr.setText(_fromUtf8(""))
        self.drumAbbr.setMaxLength(2)
        self.drumAbbr.setObjectName(_fromUtf8("drumAbbr"))
        self.gridLayout_2.addWidget(self.drumAbbr, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.oldDrum = QtGui.QComboBox(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldDrum.sizePolicy().hasHeightForWidth())
        self.oldDrum.setSizePolicy(sizePolicy)
        self.oldDrum.setMinimumSize(QtCore.QSize(143, 0))
        self.oldDrum.setObjectName(_fromUtf8("oldDrum"))
        self.gridLayout_2.addWidget(self.oldDrum, 2, 1, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.line_2 = QtGui.QFrame(editKitDialog)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        spacerItem3 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox = QtGui.QGroupBox(editKitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.currentNoteHead = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentNoteHead.sizePolicy().hasHeightForWidth())
        self.currentNoteHead.setSizePolicy(sizePolicy)
        self.currentNoteHead.setObjectName(_fromUtf8("currentNoteHead"))
        self.gridLayout_3.addWidget(self.currentNoteHead, 0, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 1, 1, 1, 1)
        self.shortcutCombo = QtGui.QComboBox(self.groupBox)
        self.shortcutCombo.setObjectName(_fromUtf8("shortcutCombo"))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.shortcutCombo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.shortcutCombo, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.noteHeadTable = QtGui.QListWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteHeadTable.sizePolicy().hasHeightForWidth())
        self.noteHeadTable.setSizePolicy(sizePolicy)
        self.noteHeadTable.setMinimumSize(QtCore.QSize(214, 100))
        self.noteHeadTable.setMaximumSize(QtCore.QSize(16777215, 150))
        self.noteHeadTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.noteHeadTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.noteHeadTable.setProperty("showDropIndicator", False)
        self.noteHeadTable.setObjectName(_fromUtf8("noteHeadTable"))
        self.verticalLayout.addWidget(self.noteHeadTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.addHeadButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addHeadButton.sizePolicy().hasHeightForWidth())
        self.addHeadButton.setSizePolicy(sizePolicy)
        self.addHeadButton.setMinimumSize(QtCore.QSize(28, 24))
        self.addHeadButton.setMaximumSize(QtCore.QSize(28, 24))
        self.addHeadButton.setText(_fromUtf8(""))
        self.addHeadButton.setIcon(icon6)
        self.addHeadButton.setObjectName(_fromUtf8("addHeadButton"))
        self.horizontalLayout.addWidget(self.addHeadButton)
        self.headUpButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headUpButton.sizePolicy().hasHeightForWidth())
        self.headUpButton.setSizePolicy(sizePolicy)
        self.headUpButton.setMinimumSize(QtCore.QSize(28, 24))
        self.headUpButton.setMaximumSize(QtCore.QSize(28, 24))
        self.headUpButton.setIcon(icon7)
        self.headUpButton.setObjectName(_fromUtf8("headUpButton"))
        self.horizontalLayout.addWidget(self.headUpButton)
        self.setDefaultHeadButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setDefaultHeadButton.sizePolicy().hasHeightForWidth())
        self.setDefaultHeadButton.setSizePolicy(sizePolicy)
        self.setDefaultHeadButton.setMinimumSize(QtCore.QSize(75, 23))
        self.setDefaultHeadButton.setMaximumSize(QtCore.QSize(75, 23))
        self.setDefaultHeadButton.setObjectName(_fromUtf8("setDefaultHeadButton"))
        self.horizontalLayout.addWidget(self.setDefaultHeadButton)
        self.headDownButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headDownButton.sizePolicy().hasHeightForWidth())
        self.headDownButton.setSizePolicy(sizePolicy)
        self.headDownButton.setMinimumSize(QtCore.QSize(28, 24))
        self.headDownButton.setMaximumSize(QtCore.QSize(28, 24))
        self.headDownButton.setText(_fromUtf8(""))
        self.headDownButton.setIcon(icon8)
        self.headDownButton.setObjectName(_fromUtf8("headDownButton"))
        self.horizontalLayout.addWidget(self.headDownButton)
        self.deleteHeadButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteHeadButton.sizePolicy().hasHeightForWidth())
        self.deleteHeadButton.setSizePolicy(sizePolicy)
        self.deleteHeadButton.setMinimumSize(QtCore.QSize(28, 24))
        self.deleteHeadButton.setMaximumSize(QtCore.QSize(28, 24))
        self.deleteHeadButton.setText(_fromUtf8(""))
        self.deleteHeadButton.setIcon(icon9)
        self.deleteHeadButton.setObjectName(_fromUtf8("deleteHeadButton"))
        self.horizontalLayout.addWidget(self.deleteHeadButton)
        spacerItem7 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_7 = QtGui.QGroupBox(editKitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.noteView = QtGui.QGraphicsView(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteView.sizePolicy().hasHeightForWidth())
        self.noteView.setSizePolicy(sizePolicy)
        self.noteView.setMinimumSize(QtCore.QSize(0, 150))
        self.noteView.setMaximumSize(QtCore.QSize(16777215, 150))
        self.noteView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.noteView.setObjectName(_fromUtf8("noteView"))
        self.horizontalLayout_8.addWidget(self.noteView)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.noteUpButton = QtGui.QPushButton(self.frame_2)
        self.noteUpButton.setText(_fromUtf8(""))
        self.noteUpButton.setIcon(icon7)
        self.noteUpButton.setObjectName(_fromUtf8("noteUpButton"))
        self.verticalLayout_11.addWidget(self.noteUpButton)
        self.noteDownButton = QtGui.QPushButton(self.frame_2)
        self.noteDownButton.setText(_fromUtf8(""))
        self.noteDownButton.setIcon(icon8)
        self.noteDownButton.setObjectName(_fromUtf8("noteDownButton"))
        self.verticalLayout_11.addWidget(self.noteDownButton)
        self.horizontalLayout_8.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_3 = QtGui.QFrame(self.groupBox_7)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.stemUpDownBox = QtGui.QCheckBox(self.frame_3)
        self.stemUpDownBox.setObjectName(_fromUtf8("stemUpDownBox"))
        self.horizontalLayout_9.addWidget(self.stemUpDownBox)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.effectBox = QtGui.QComboBox(self.groupBox_7)
        self.effectBox.setObjectName(_fromUtf8("effectBox"))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.effectBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.effectBox)
        self.label_8 = QtGui.QLabel(self.groupBox_7)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.noteHeadBox = QtGui.QComboBox(self.groupBox_7)
        self.noteHeadBox.setObjectName(_fromUtf8("noteHeadBox"))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.noteHeadBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.noteHeadBox)
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        spacerItem8 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(editKitDialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.muteButton = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.muteButton.sizePolicy().hasHeightForWidth())
        self.muteButton.setSizePolicy(sizePolicy)
        self.muteButton.setMaximumSize(QtCore.QSize(28, 24))
        self.muteButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/audio-volume-medium.png")), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/audio-volume-muted.png")), QtGui.QIcon.Normal,
                         QtGui.QIcon.On)
        self.muteButton.setIcon(icon10)
        self.muteButton.setCheckable(True)
        self.muteButton.setObjectName(_fromUtf8("muteButton"))
        self.horizontalLayout_6.addWidget(self.muteButton)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(editKitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.midiNoteCombo = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midiNoteCombo.sizePolicy().hasHeightForWidth())
        self.midiNoteCombo.setSizePolicy(sizePolicy)
        self.midiNoteCombo.setMinimumSize(QtCore.QSize(201, 0))
        self.midiNoteCombo.setObjectName(_fromUtf8("midiNoteCombo"))
        self.verticalLayout_5.addWidget(self.midiNoteCombo)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.volumeIndicator = QtGui.QLabel(self.groupBox_3)
        self.volumeIndicator.setObjectName(_fromUtf8("volumeIndicator"))
        self.horizontalLayout_7.addWidget(self.volumeIndicator)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.volumeSlider = QtGui.QSlider(self.groupBox_3)
        self.volumeSlider.setMaximum(127)
        self.volumeSlider.setSliderPosition(63)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.verticalLayout_4.addWidget(self.volumeSlider)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.effectsGroup = QtGui.QGroupBox(editKitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.effectsGroup.sizePolicy().hasHeightForWidth())
        self.effectsGroup.setSizePolicy(sizePolicy)
        self.effectsGroup.setMinimumSize(QtCore.QSize(221, 99))
        self.effectsGroup.setMaximumSize(QtCore.QSize(221, 99))
        self.effectsGroup.setObjectName(_fromUtf8("effectsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.effectsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.normalEffect = QtGui.QRadioButton(self.effectsGroup)
        self.normalEffect.setChecked(True)
        self.normalEffect.setObjectName(_fromUtf8("normalEffect"))
        self.gridLayout.addWidget(self.normalEffect, 0, 1, 1, 1)
        self.accentEffect = QtGui.QRadioButton(self.effectsGroup)
        self.accentEffect.setObjectName(_fromUtf8("accentEffect"))
        self.gridLayout.addWidget(self.accentEffect, 0, 3, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 19, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 4, 1, 1)
        self.ghostEffect = QtGui.QRadioButton(self.effectsGroup)
        self.ghostEffect.setObjectName(_fromUtf8("ghostEffect"))
        self.gridLayout.addWidget(self.ghostEffect, 1, 1, 1, 1)
        self.chokeEffect = QtGui.QRadioButton(self.effectsGroup)
        self.chokeEffect.setObjectName(_fromUtf8("chokeEffect"))
        self.gridLayout.addWidget(self.chokeEffect, 1, 3, 1, 1)
        self.flamEffect = QtGui.QRadioButton(self.effectsGroup)
        self.flamEffect.setObjectName(_fromUtf8("flamEffect"))
        self.gridLayout.addWidget(self.flamEffect, 2, 1, 1, 1)
        self.dragEffect = QtGui.QRadioButton(self.effectsGroup)
        self.dragEffect.setObjectName(_fromUtf8("dragEffect"))
        self.gridLayout.addWidget(self.dragEffect, 2, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.effectsGroup)
        self.groupBox_2 = QtGui.QGroupBox(editKitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lockedCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.lockedCheckBox.setText(_fromUtf8(""))
        self.lockedCheckBox.setObjectName(_fromUtf8("lockedCheckBox"))
        self.horizontalLayout_3.addWidget(self.lockedCheckBox)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(182, 48))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(editKitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_10.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.drumName)
        self.label_4.setBuddy(self.drumAbbr)
        self.label_5.setBuddy(self.oldDrum)
        self.label_6.setBuddy(self.currentNoteHead)
        self.label_10.setBuddy(self.shortcutCombo)
        self.label_8.setBuddy(self.effectBox)
        self.label_9.setBuddy(self.noteHeadBox)
        self.label_7.setBuddy(self.muteButton)
        self.label.setBuddy(self.lockedCheckBox)

        self.retranslateUi(editKitDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), editKitDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), editKitDialog.reject)
        QtCore.QObject.connect(self.volumeSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.volumeIndicator.setNum)
        QtCore.QMetaObject.connectSlotsByName(editKitDialog)
        editKitDialog.setTabOrder(self.addButton, self.deleteButton)
        editKitDialog.setTabOrder(self.deleteButton, self.buttonBox)

    def retranslateUi(self, editKitDialog):
        editKitDialog.setWindowTitle(
            QtGui.QApplication.translate("editKitDialog", "Edit Drum Kit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "The drums in the kit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Drums", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEmptyButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Delete empty non-locked drums", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.deleteEmptyButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                         "<html><head/><body><p><span style=\" font-weight:600;\">Delete empty non-locked drums</span></p><p><br/></p><p>Any drums which are not locked and which do not have any notes on them in the current score will be deleted from the kit when this button is pressed.</p></body></html>",
                                                                         None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setToolTip(QtGui.QApplication.translate("editKitDialog", "Clear the kit and start again", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                   "<html><head/><body><p><span style=\" font-weight:600;\">New drum kit</span></p><p><br/></p><p>Click this button to remove all drums from the kit and start witha new kit.</p></body></html>",
                                                                   None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Reset the kit", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                   "<html><head/><body><p><span style=\" font-weight:600;\">Reset kit</span></p><p><br/></p><p>Click this button to revert to the kit as it was when you opened this editor window.</p></body></html>",
                                                                   None, QtGui.QApplication.UnicodeUTF8))
        self.defaultKitButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Default kits", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultKitButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                        "<html><head/><body><p><span style=\" font-weight:600;\">Default kits</span></p><p><br/></p><p>DrumBurp comes with a number of default kits that you can use, and you can add your own kits to this list. Click this button to load a default kit, or save the current kit as a default.</p></body></html>",
                                                                        None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Load a drum kit", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                  "<html><head/><body><p><span style=\" font-weight:600;\">Load a drum kit</span></p><p><br/></p><p>Load a drum kit from disk.</p></body></html>",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Save this drum kit", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                  "<html><head/><body><p><span style=\" font-weight:600;\">Save the drum kit</span></p><p><br/></p><p>Save the current drum kit to a file on disk.</p></body></html>",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.kitTable.setToolTip(QtGui.QApplication.translate("editKitDialog", "The drums and their order", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.kitTable.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                "<html><head/><body><p><span style=\" font-weight:600;\">List of instruments</span></p><p><br/></p><p>Each drum in the kit is represented by a single line in the score. This list of instruments defines what drums you have in the kit, and what order they appear in the score. You can add and delete drums, move them around, and edit their information.</p><p>Select one of the drums in this list to edit its name, abbreviation, note heads, Lilypond notation, and MIDI sound.</p><p><span style=\" font-weight:600;\">Note: </span>It is an error for more than one drum to have the same abbreviation. If this happens, the offending drums will be highlighted in red, and the <span style=\" font-style:italic;\">OK</span> button will be disabled.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Add a drum", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                 "<html><head/><body><p><span style=\" font-weight:600;\">Add a new drum</span></p><p><br/></p><p>Click this to add a new drum to the kit. It will be added at the bottom of the current kit, with some default settings.</p></body></html>",
                                                                 None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setToolTip(QtGui.QApplication.translate("editKitDialog", "Move the current drum up", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.upButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                "<html><head/><body><p><span style=\" font-weight:600;\">Move drum up</span></p><p><br/></p><p>Click this button to move the currently selected drum up in the kit list.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.downButton.setToolTip(QtGui.QApplication.translate("editKitDialog", "Move the current drum down", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.downButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                  "<html><head/><body><p><span style=\" font-weight:600;\">Move drum down</span></p><p><br/></p><p>Click this button to move the currently selected drum down in the kit.</p></body></html>",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setToolTip(QtGui.QApplication.translate("editKitDialog", "Remove the current drum", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                    "<html><head/><body><p><span style=\" font-weight:600;\">Delete selected drum</span></p><p><br/></p><p>Click this button to remove the currently selected drum from the kit.</p></body></html>",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Identifying information for the drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Drum Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Name for this drum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("editKitDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.drumName.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Name for this drum", None, QtGui.QApplication.UnicodeUTF8))
        self.drumName.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                "<html><head/><body><p><span style=\" font-weight:600;\">Drum name</span></p><p><br/></p><p>The long name of this instrument as it appears in the drum key.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("editKitDialog", "Abbreviation for this drum", None,
                                                             QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("editKitDialog", "Abbreviation", None, QtGui.QApplication.UnicodeUTF8))
        self.drumAbbr.setToolTip(QtGui.QApplication.translate("editKitDialog", "Abbreviation for this drum", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.drumAbbr.setStatusTip(QtGui.QApplication.translate("editKitDialog", "Abbreviation for this drum", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.drumAbbr.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                "<html><head/><body><p><span style=\" font-weight:600;\">Drum name abbreviation</span></p><p><br/></p><p>The short version of this drum name as it appears on the line labels to the left of every staff.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.drumAbbr.setInputMask(
            QtGui.QApplication.translate("editKitDialog", "Nn; ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("editKitDialog",
                                                             "Copy the existing notes from one of the drums in the current score to this drum",
                                                             None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("editKitDialog", "Convert from existing drum?", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.oldDrum.setToolTip(QtGui.QApplication.translate("editKitDialog",
                                                             "Copy the existing notes from one of the drums in the current score to this drum",
                                                             None, QtGui.QApplication.UnicodeUTF8))
        self.oldDrum.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                               "<html><head/><body><p><span style=\" font-weight:600;\">Convert from existing drum</span></p><p><br/></p><p>Selecting another drum in the kit means that the notes in the score currently assigned to that drum will instead be assigned to this drum.</p></body></html>",
                                                               None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Define the valid note heads for this drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Note Heads", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(
            QtGui.QApplication.translate("editKitDialog", "Current note head", None, QtGui.QApplication.UnicodeUTF8))
        self.currentNoteHead.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Change the selected note head", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.currentNoteHead.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                       "<html><head/><body><p><span style=\" font-weight:600;\">Current note head</span></p><p><br/></p><p>This option allows you to select the symbol that will be displayed for the currently selected note head.</p></body></html>",
                                                                       None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(
            QtGui.QApplication.translate("editKitDialog", "Shortcut", None, QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                     "<html><head/><body><p><span style=\" font-weight:600;\">Note head shortcut</span></p><p><br/></p><p>The keyboard shortcut that is associated with this note head.</p></body></html>",
                                                                     None, QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(0, QtGui.QApplication.translate("editKitDialog", "a", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(1, QtGui.QApplication.translate("editKitDialog", "b", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(2, QtGui.QApplication.translate("editKitDialog", "c", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(3, QtGui.QApplication.translate("editKitDialog", "d", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(4, QtGui.QApplication.translate("editKitDialog", "e", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(5, QtGui.QApplication.translate("editKitDialog", "f", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(6, QtGui.QApplication.translate("editKitDialog", "g", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(7, QtGui.QApplication.translate("editKitDialog", "h", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(8, QtGui.QApplication.translate("editKitDialog", "i", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(9, QtGui.QApplication.translate("editKitDialog", "j", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(10, QtGui.QApplication.translate("editKitDialog", "k", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(11, QtGui.QApplication.translate("editKitDialog", "l", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(12, QtGui.QApplication.translate("editKitDialog", "m", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(13, QtGui.QApplication.translate("editKitDialog", "n", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(14, QtGui.QApplication.translate("editKitDialog", "o", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(15, QtGui.QApplication.translate("editKitDialog", "p", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(16, QtGui.QApplication.translate("editKitDialog", "q", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(17, QtGui.QApplication.translate("editKitDialog", "r", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(18, QtGui.QApplication.translate("editKitDialog", "s", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(19, QtGui.QApplication.translate("editKitDialog", "t", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(20, QtGui.QApplication.translate("editKitDialog", "u", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(21, QtGui.QApplication.translate("editKitDialog", "v", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(22, QtGui.QApplication.translate("editKitDialog", "w", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(23, QtGui.QApplication.translate("editKitDialog", "x", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(24, QtGui.QApplication.translate("editKitDialog", "y", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.shortcutCombo.setItemText(25, QtGui.QApplication.translate("editKitDialog", "z", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.noteHeadTable.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "A list of the valid note heads for this drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.noteHeadTable.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                     "<html><head/><body><p><span style=\" font-weight:600;\">Note head list</span></p><p><br/></p><p>Each drum has a list of valid note heads that can be displayed on its line. Each note head corresponds to a different way of striking the drum, e.g. normal strikes, ghost notes, flams, etc. This window lists the valid note heads for the currently selected drum.</p><p><br/></p><p>Selecting a note head in this window allows you to choose MIDI and Lilypond notation to be associated with this note head for this drum.</p></body></html>",
                                                                     None, QtGui.QApplication.UnicodeUTF8))
        self.addHeadButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Add a new note head for this drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.addHeadButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                     "<html><head/><body><p><span style=\" font-weight:600;\">Add note head</span></p><p><br/></p><p>Add a new note head for this drum.</p></body></html>",
                                                                     None, QtGui.QApplication.UnicodeUTF8))
        self.headUpButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Move the current note head up", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.headUpButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                    "<html><head/><body><p><span style=\" font-weight:600;\">Move note head up</span></p><p><br/></p><p>Move the currently selected note head up in the list.</p></body></html>",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.setDefaultHeadButton.setToolTip(QtGui.QApplication.translate("editKitDialog",
                                                                          "Make the currently selected note head the default for this drum",
                                                                          None, QtGui.QApplication.UnicodeUTF8))
        self.setDefaultHeadButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                            "<html><head/><body><p><span style=\" font-weight:600;\">Set default note head</span></p><p><br/></p><p>The default note head is the one which is placed in the score when you click on a note position for this drum. Click this button to make the currently selected note head the default for this drum.</p></body></html>",
                                                                            None, QtGui.QApplication.UnicodeUTF8))
        self.setDefaultHeadButton.setText(
            QtGui.QApplication.translate("editKitDialog", "Set Default", None, QtGui.QApplication.UnicodeUTF8))
        self.headDownButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Move the current note head down", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.headDownButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                      "<html><head/><body><p><span style=\" font-weight:600;\">Move note head down</span></p><p><br/></p><p>Move the currently selected note head down in the list.</p></body></html>",
                                                                      None, QtGui.QApplication.UnicodeUTF8))
        self.deleteHeadButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Remove the currently selected note head", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.deleteHeadButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                        "<html><head/><body><p><span style=\" font-weight:600;\">Remove note head</span></p><p><br/></p><p>Remove the currently selected note head from the list of heads valid for this drum.</p></body></html>",
                                                                        None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Set how Lilypond will display this note", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Lilypond Notation", None, QtGui.QApplication.UnicodeUTF8))
        self.noteView.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Example note display", None, QtGui.QApplication.UnicodeUTF8))
        self.noteView.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                "<html><head/><body><p><span style=\" font-weight:600;\">Notation display</span></p><p><br/></p><p>This window shows you an example of how the current note head for the current drum will appear when you export the score to Lilypond.</p><p><br/></p><p>Note: Lilypond uses complex algorithms to determine exactly how to display each note so the example displayed here may not always be precisely how the note appears in the Lilypond output. However, DrumBurp tries hard to encourage Lilypond to display notes the way they are shown here.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.noteUpButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Move the note up", None, QtGui.QApplication.UnicodeUTF8))
        self.noteUpButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                    "<html><head/><body><p><span style=\" font-weight:600;\">Move note up</span></p><p><br/></p><p>Move the note up one step in the staff.</p></body></html>",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.noteDownButton.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Move the note down", None, QtGui.QApplication.UnicodeUTF8))
        self.noteDownButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                      "<html><head/><body><p><span style=\" font-weight:600;\">Move note down</span></p><p><br/></p><p>Move the note down one step in the staff.</p></body></html>",
                                                                      None, QtGui.QApplication.UnicodeUTF8))
        self.stemUpDownBox.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Note stems should prefer to go up", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.stemUpDownBox.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                     "<html><head/><body><p><span style=\" font-weight:600;\">Stem up/down</span></p><p><br/></p><p>DrumBurp groups notes together in the Lilypond export according to whether they are set to have their stems up or down. Notes with the same direction specified here will be displayed by Lilypond as part of the same voice.</p><p><br/></p><p>Lilypond may decide to set certain notes with their stems in the opposite direction to that selected here if it thinks it looks better.</p></body></html>",
                                                                     None, QtGui.QApplication.UnicodeUTF8))
        self.stemUpDownBox.setText(
            QtGui.QApplication.translate("editKitDialog", "Stem up", None, QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Notation effect to apply to the note", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                 "<html><head/><body><p><span style=\" font-weight:600;\">Lilypond note effect</span></p><p><br/></p><p>Select the effect that Lilypond will apply to this note head in the exported score.</p></body></html>",
                                                                 None, QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(0, QtGui.QApplication.translate("editKitDialog", "none", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(1, QtGui.QApplication.translate("editKitDialog", "open", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(2, QtGui.QApplication.translate("editKitDialog", "stopped", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(3, QtGui.QApplication.translate("editKitDialog", "ghost", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(4, QtGui.QApplication.translate("editKitDialog", "flam", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(5, QtGui.QApplication.translate("editKitDialog", "choke", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(6, QtGui.QApplication.translate("editKitDialog", "accent", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.effectBox.setItemText(7, QtGui.QApplication.translate("editKitDialog", "drag", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Notation effect to apply to the note", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(
            QtGui.QApplication.translate("editKitDialog", "Effect", None, QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Select the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                   "<html><head/><body><p><span style=\" font-weight:600;\">Lilypond note head</span></p><p><br/></p><p>Select the symbol that Lilypond will use to dispay this note head for this drum in the exported score.</p></body></html>",
                                                                   None, QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(0, QtGui.QApplication.translate("editKitDialog", "default", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(1, QtGui.QApplication.translate("editKitDialog", "harmonic", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(2, QtGui.QApplication.translate("editKitDialog", "harmonic black", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(3, QtGui.QApplication.translate("editKitDialog", "diamond", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(4, QtGui.QApplication.translate("editKitDialog", "cross", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(5, QtGui.QApplication.translate("editKitDialog", "xcircle", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.noteHeadBox.setItemText(6, QtGui.QApplication.translate("editKitDialog", "triangle", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.label_9.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Select the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(
            QtGui.QApplication.translate("editKitDialog", "Head", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setToolTip(QtGui.QApplication.translate("editKitDialog", "Mute audio in this dialog", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.muteButton.setToolTip(QtGui.QApplication.translate("editKitDialog", "Mute audio in this dialog", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.muteButton.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                  "<html><head/><body><p><span style=\" font-weight:600;\">Mute audio</span></p><p><br/></p><p>Turn MIDI sounds on/off in this dialog.</p></body></html>",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("editKitDialog", "Mute audio in this dialog", None,
                                                             QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(
            QtGui.QApplication.translate("editKitDialog", "Play sound effects", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "The MIDI noise associated with this note head for this drum",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(
            QtGui.QApplication.translate("editKitDialog", "MIDI Note", None, QtGui.QApplication.UnicodeUTF8))
        self.midiNoteCombo.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "The drum type associated with this note head for this drum",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.midiNoteCombo.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                     "<html><head/><body><p><span style=\" font-weight:600;\">MIDI note</span></p><p><br/></p><p>Select the MIDI note that will be associated with the currently selected note head for the current drum. This is used in MIDI playback and export, and is the noise that is played when new notes are added to the score in the editor window.</p></body></html>",
                                                                     None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "The volume of this note head on this drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("editKitDialog", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeIndicator.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "The volume of this note head on this drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.volumeIndicator.setText(
            QtGui.QApplication.translate("editKitDialog", "64", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeSlider.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "The volume of this note head on this drum", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.volumeSlider.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                    "<html><head/><body><p><span style=\" font-weight:600;\">MIDI note volume</span></p><p><br/></p><p>Adjust the volume of the MIDI note associated with the current drum and note head.</p></body></html>",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.effectsGroup.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Effects to apply to this note head", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.effectsGroup.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                    "<html><head/><body><p><span style=\" font-weight:600;\">MIDI note effect</span></p><p><br/></p><p>The sound effect to apply to the output MIDI.</p><p><br/></p><p><span style=\" font-weight:600;\">Note:</span> this only has an effect for &quot;Drag&quot; notes at the moment. Further effects will be added in future versions of DrumBurp.</p></body></html>",
                                                                    None, QtGui.QApplication.UnicodeUTF8))
        self.effectsGroup.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Effects", None, QtGui.QApplication.UnicodeUTF8))
        self.normalEffect.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "A normal strike", None, QtGui.QApplication.UnicodeUTF8))
        self.normalEffect.setText(
            QtGui.QApplication.translate("editKitDialog", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.accentEffect.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "A harder strike", None, QtGui.QApplication.UnicodeUTF8))
        self.accentEffect.setText(
            QtGui.QApplication.translate("editKitDialog", "Accent", None, QtGui.QApplication.UnicodeUTF8))
        self.ghostEffect.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "A quieter strike", None, QtGui.QApplication.UnicodeUTF8))
        self.ghostEffect.setText(
            QtGui.QApplication.translate("editKitDialog", "Ghost", None, QtGui.QApplication.UnicodeUTF8))
        self.chokeEffect.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "A choked strike", None, QtGui.QApplication.UnicodeUTF8))
        self.chokeEffect.setText(
            QtGui.QApplication.translate("editKitDialog", "Choke", None, QtGui.QApplication.UnicodeUTF8))
        self.flamEffect.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "A two-handed strike", None, QtGui.QApplication.UnicodeUTF8))
        self.flamEffect.setText(
            QtGui.QApplication.translate("editKitDialog", "Flam", None, QtGui.QApplication.UnicodeUTF8))
        self.dragEffect.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Two or more strikes in quick succession", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.dragEffect.setText(
            QtGui.QApplication.translate("editKitDialog", "Drag", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Should the drum line be locked?", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setWhatsThis(QtGui.QApplication.translate("editKitDialog",
                                                                  "<html><head/><body><p><span style=\" font-weight:600;\">Lock this drum</span></p><p><br/></p><p>If this drum is locked then:</p><p><br/></p><p>a) it will always be displayed in the score, even when there are no notes on its line and the <span style=\" font-style:italic;\">Omit Empty Lines</span> option is turned on, and;</p><p><br/></p><p>b) it will not be deleted from the kit if the <span style=\" font-style:italic;\">Delete Non-Locked Empty Drums</span> button is pressed in the kit editor.</p></body></html>",
                                                                  None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(
            QtGui.QApplication.translate("editKitDialog", "Line Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.lockedCheckBox.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Lock this line", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(
            QtGui.QApplication.translate("editKitDialog", "Lock this line", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("editKitDialog",
                                                        "The line for this drum will always be displayed, even if it contains no notes.",
                                                        None, QtGui.QApplication.UnicodeUTF8))


import buttons_rc
import DrumBurp_rc
