# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\Widgets\measureTabs.ui'
#
# Created: Sat Mar 31 13:52:26 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_measureTabs(object):
    def setupUi(self, measureTabs):
        measureTabs.setObjectName(_fromUtf8("measureTabs"))
        measureTabs.resize(218, 155)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(measureTabs.sizePolicy().hasHeightForWidth())
        measureTabs.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(measureTabs)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.counterTabs = QtGui.QTabWidget(measureTabs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.counterTabs.sizePolicy().hasHeightForWidth())
        self.counterTabs.setSizePolicy(sizePolicy)
        self.counterTabs.setMinimumSize(QtCore.QSize(200, 85))
        self.counterTabs.setMaximumSize(QtCore.QSize(500, 85))
        self.counterTabs.setTabShape(QtGui.QTabWidget.Triangular)
        self.counterTabs.setObjectName(_fromUtf8("counterTabs"))
        self.simpleTab = QtGui.QWidget()
        self.simpleTab.setObjectName(_fromUtf8("simpleTab"))
        self.gridLayout = QtGui.QGridLayout(self.simpleTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.simpleTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.beatsSpinBox = QtGui.QSpinBox(self.simpleTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beatsSpinBox.sizePolicy().hasHeightForWidth())
        self.beatsSpinBox.setSizePolicy(sizePolicy)
        self.beatsSpinBox.setBaseSize(QtCore.QSize(100, 0))
        self.beatsSpinBox.setMinimum(1)
        self.beatsSpinBox.setMaximum(256)
        self.beatsSpinBox.setProperty("value", 4)
        self.beatsSpinBox.setObjectName(_fromUtf8("beatsSpinBox"))
        self.gridLayout.addWidget(self.beatsSpinBox, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.simpleTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.beatCountComboBox = QtGui.QComboBox(self.simpleTab)
        self.beatCountComboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.beatCountComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.beatCountComboBox.setBaseSize(QtCore.QSize(200, 0))
        self.beatCountComboBox.setObjectName(_fromUtf8("beatCountComboBox"))
        self.gridLayout.addWidget(self.beatCountComboBox, 1, 2, 1, 1)
        self.counterTabs.addTab(self.simpleTab, _fromUtf8(""))
        self.complexTab = QtGui.QWidget()
        self.complexTab.setObjectName(_fromUtf8("complexTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.complexTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.complexEditButton = QtGui.QPushButton(self.complexTab)
        self.complexEditButton.setObjectName(_fromUtf8("complexEditButton"))
        self.gridLayout_3.addWidget(self.complexEditButton, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.counterTabs.addTab(self.complexTab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.counterTabs, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(measureTabs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox.setBaseSize(QtCore.QSize(200, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.previewText = QtGui.QLabel(self.groupBox)
        self.previewText.setAlignment(QtCore.Qt.AlignCenter)
        self.previewText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.previewText.setObjectName(_fromUtf8("previewText"))
        self.verticalLayout_2.addWidget(self.previewText)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.label_2.setBuddy(self.beatsSpinBox)

        self.retranslateUi(measureTabs)
        self.counterTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(measureTabs)

    def retranslateUi(self, measureTabs):
        measureTabs.setWindowTitle(
            QtGui.QApplication.translate("measureTabs", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.simpleTab.setToolTip(QtGui.QApplication.translate("measureTabs", "Edit a simple measure count", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(
            QtGui.QApplication.translate("measureTabs", "The size of each measure in the new score in beats", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("measureTabs", "Beats", None, QtGui.QApplication.UnicodeUTF8))
        self.beatsSpinBox.setToolTip(
            QtGui.QApplication.translate("measureTabs", "The size of each measure in the new score in beats", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.beatsSpinBox.setStatusTip(
            QtGui.QApplication.translate("measureTabs", "The size of each measure in the new score in beats", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.beatsSpinBox.setSuffix(
            QtGui.QApplication.translate("measureTabs", " beats", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("measureTabs", "The number of beats in this measure", None,
                                                             QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("measureTabs", "Beat count", None, QtGui.QApplication.UnicodeUTF8))
        self.beatCountComboBox.setToolTip(
            QtGui.QApplication.translate("measureTabs", "The number of beats in this measure", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.counterTabs.setTabText(self.counterTabs.indexOf(self.simpleTab),
                                    QtGui.QApplication.translate("measureTabs", "Simple Count", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.complexTab.setToolTip(QtGui.QApplication.translate("measureTabs", "Edit a complex measure count", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.complexEditButton.setToolTip(
            QtGui.QApplication.translate("measureTabs", "Edit a complex count", None, QtGui.QApplication.UnicodeUTF8))
        self.complexEditButton.setText(
            QtGui.QApplication.translate("measureTabs", "Edit Count", None, QtGui.QApplication.UnicodeUTF8))
        self.counterTabs.setTabText(self.counterTabs.indexOf(self.complexTab),
                                    QtGui.QApplication.translate("measureTabs", "Complex Count", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(
            QtGui.QApplication.translate("measureTabs", "A preview of the measure count currently selected", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(
            QtGui.QApplication.translate("measureTabs", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.previewText.setText(
            QtGui.QApplication.translate("measureTabs", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

