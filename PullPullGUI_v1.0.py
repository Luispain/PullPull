# -*- coding: utf-8 -*-

"""
Pull-Pull Calculator v1.0 created by Luis Bernardos - luisfco.bernardos@gmail.com
This software is released under the GNU v3 License.
"""

import sys
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import *
import scipy.optimize

# Functions for calculations:
def diff_t2(T2, T01, R1, L, T1, self):
    # Makes the difference of length between the two chords. This function is used for obtaining T2 with fsolve.
    return -L + sqrt((R1*cos(deg2rad(T01 + T1)) + self.R2*cos(deg2rad(self.T02 - T2)))**2 +
                            (self.S - R1*sin(deg2rad(T01 + T1)) - self.R2*sin(deg2rad(self.T02 - T2)))**2)
def diff_t22(T22, T01, R1, L, T1, self):
    # Makes the difference of length between the two chords. This function is used for obtaining T22 with fsolve.
    return -L + sqrt((R1*cos(deg2rad(T01 - T1)) + self.R2*cos(deg2rad(self.T02 + T22)))**2 +
                     (self.S - R1*sin(deg2rad(T01 - T1)) - self.R2*sin(deg2rad(self.T02 + T22)))**2)
def optpoint(x, self):
    # x is array([T01, R1]). It defines the system of equations to be solved for optimization.
    L = sqrt((x[1] * cos(deg2rad(x[0])) + self.R2 * cos(deg2rad(self.T02))) ** 2 + \
             (self.S - x[1] * sin(deg2rad(x[0])) - self.R2 * sin(deg2rad(self.T02))) ** 2)
    return array([diff_t2(self.T2opt, x[0], x[1], L, self.T1opt, self),
                  diff_t22(self.T2opt, x[0], x[1], L, self.T1opt, self)])

# Class and functions for GUI:
# noinspection PyAttributeOutsideInit
class Help(QtWidgets.QDialog):
    def __init__(self, parent):
        super(Help, self).__init__(parent)
        self.setObjectName("Help")
        self.resize(497, 497)

class Ui_Form(object):
    def setupUi(self, Form):
        #  Creates the GUI:

        Form.setObjectName("Form")
        Form.resize(457, 421)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_Lang = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Lang.setObjectName("horizontalLayout_Lang")
        self.pushButton_English = QtWidgets.QPushButton(Form)
        self.pushButton_English.setObjectName("pushButton_English")
        self.horizontalLayout_Lang.addWidget(self.pushButton_English)
        self.pushButton_Spanish = QtWidgets.QPushButton(Form)
        self.pushButton_Spanish.setObjectName("pushButton_Spanish")
        self.horizontalLayout_Lang.addWidget(self.pushButton_Spanish)
        self.pushButton_French = QtWidgets.QPushButton(Form)
        self.pushButton_French.setObjectName("pushButton_French")
        self.horizontalLayout_Lang.addWidget(self.pushButton_French)
        self.gridLayout.addLayout(self.horizontalLayout_Lang, 0, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 4, 0, 1, 1)
        self.gridLayout_Design = QtWidgets.QGridLayout()
        self.gridLayout_Design.setObjectName("gridLayout_Design")
        self.doubleSpinBox_T2opt = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_T2opt.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_T2opt.setSizePolicy(sizePolicy)
        self.doubleSpinBox_T2opt.setDecimals(3)
        self.doubleSpinBox_T2opt.setMinimum(0.0)
        self.doubleSpinBox_T2opt.setMaximum(90.0)
        self.doubleSpinBox_T2opt.setSingleStep(0.5)
        self.doubleSpinBox_T2opt.setProperty("value", 30.0)
        self.doubleSpinBox_T2opt.setObjectName("doubleSpinBox_T2opt")
        self.gridLayout_Design.addWidget(self.doubleSpinBox_T2opt, 1, 3, 1, 1)
        self.label_Design = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Design.sizePolicy().hasHeightForWidth())
        self.label_Design.setSizePolicy(sizePolicy)
        self.label_Design.setObjectName("label_Design")
        self.gridLayout_Design.addWidget(self.label_Design, 0, 0, 1, 1)
        self.doubleSpinBox_T1opt = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_T1opt.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_T1opt.setSizePolicy(sizePolicy)
        self.doubleSpinBox_T1opt.setDecimals(3)
        self.doubleSpinBox_T1opt.setMinimum(0.0)
        self.doubleSpinBox_T1opt.setMaximum(90.0)
        self.doubleSpinBox_T1opt.setSingleStep(0.5)
        self.doubleSpinBox_T1opt.setProperty("value", 60.0)
        self.doubleSpinBox_T1opt.setObjectName("doubleSpinBox_T1opt")
        self.gridLayout_Design.addWidget(self.doubleSpinBox_T1opt, 1, 1, 1, 1)
        self.label_T1opt = QtWidgets.QLabel(Form)
        self.label_T1opt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_T1opt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T1opt.setObjectName("label_T1opt")
        self.gridLayout_Design.addWidget(self.label_T1opt, 1, 0, 1, 1)
        self.label_T2opt = QtWidgets.QLabel(Form)
        self.label_T2opt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_T2opt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T2opt.setObjectName("label_T2opt")
        self.gridLayout_Design.addWidget(self.label_T2opt, 1, 2, 1, 1)
        self.pushButton_Optimize = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Optimize.sizePolicy().hasHeightForWidth())
        self.pushButton_Optimize.setSizePolicy(sizePolicy)
        self.pushButton_Optimize.setObjectName("pushButton_Optimize")
        self.gridLayout_Design.addWidget(self.pushButton_Optimize, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_Design, 7, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 6, 0, 1, 1)
        self.gridLayout_Analysis = QtWidgets.QGridLayout()
        self.gridLayout_Analysis.setObjectName("gridLayout_Analysis")
        self.label_PrintMaxPlay = QtWidgets.QLabel(Form)
        self.label_PrintMaxPlay.setObjectName("label_PrintMaxPlay")
        self.gridLayout_Analysis.addWidget(self.label_PrintMaxPlay, 1, 3, 1, 1)
        self.label_MaxPlay = QtWidgets.QLabel(Form)
        self.label_MaxPlay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_MaxPlay.setObjectName("label_MaxPlay")
        self.gridLayout_Analysis.addWidget(self.label_MaxPlay, 1, 2, 1, 1)
        self.label_MaxPlayRudderDefl = QtWidgets.QLabel(Form)
        self.label_MaxPlayRudderDefl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_MaxPlayRudderDefl.setObjectName("label_MaxPlayRudderDefl")
        self.gridLayout_Analysis.addWidget(self.label_MaxPlayRudderDefl, 3, 2, 1, 1)
        self.label_MaxPlayServo = QtWidgets.QLabel(Form)
        self.label_MaxPlayServo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_MaxPlayServo.setObjectName("label_MaxPlayServo")
        self.gridLayout_Analysis.addWidget(self.label_MaxPlayServo, 2, 2, 1, 1)
        self.pushButton_PlotResult = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_PlotResult.sizePolicy().hasHeightForWidth())
        self.pushButton_PlotResult.setSizePolicy(sizePolicy)
        self.pushButton_PlotResult.setObjectName("pushButton_PlotResult")
        self.gridLayout_Analysis.addWidget(self.pushButton_PlotResult, 3, 1, 1, 1)
        self.label_Analysis = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Analysis.sizePolicy().hasHeightForWidth())
        self.label_Analysis.setSizePolicy(sizePolicy)
        self.label_Analysis.setObjectName("label_Analysis")
        self.gridLayout_Analysis.addWidget(self.label_Analysis, 0, 0, 1, 1)
        self.spinBox_steps = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_steps.sizePolicy().hasHeightForWidth())
        self.spinBox_steps.setSizePolicy(sizePolicy)
        self.spinBox_steps.setMinimum(2)
        self.spinBox_steps.setMaximum(1000)
        self.spinBox_steps.setProperty("value", 50)
        self.spinBox_steps.setObjectName("spinBox_steps")
        self.gridLayout_Analysis.addWidget(self.spinBox_steps, 2, 1, 1, 1)
        self.pushButton_Calculate = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Calculate.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate.setSizePolicy(sizePolicy)
        self.pushButton_Calculate.setObjectName("pushButton_Calculate")
        self.gridLayout_Analysis.addWidget(self.pushButton_Calculate, 3, 0, 1, 1)
        self.label_steps = QtWidgets.QLabel(Form)
        self.label_steps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_steps.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_steps.setObjectName("label_steps")
        self.gridLayout_Analysis.addWidget(self.label_steps, 2, 0, 1, 1)
        self.doubleSpinBox_T1max = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_T1max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_T1max.setSizePolicy(sizePolicy)
        self.doubleSpinBox_T1max.setDecimals(3)
        self.doubleSpinBox_T1max.setMinimum(0.0)
        self.doubleSpinBox_T1max.setMaximum(90.0)
        self.doubleSpinBox_T1max.setSingleStep(0.5)
        self.doubleSpinBox_T1max.setProperty("value", 45.0)
        self.doubleSpinBox_T1max.setObjectName("doubleSpinBox_T1max")
        self.gridLayout_Analysis.addWidget(self.doubleSpinBox_T1max, 1, 1, 1, 1)
        self.label_T1max = QtWidgets.QLabel(Form)
        self.label_T1max.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_T1max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T1max.setObjectName("label_T1max")
        self.gridLayout_Analysis.addWidget(self.label_T1max, 1, 0, 1, 1)
        self.label_PrintMaxPlayRudderDefl = QtWidgets.QLabel(Form)
        self.label_PrintMaxPlayRudderDefl.setObjectName("label_PrintMaxPlayRudderDefl")
        self.gridLayout_Analysis.addWidget(self.label_PrintMaxPlayRudderDefl, 3, 3, 1, 1)
        self.label_PrintMaxPlayServo = QtWidgets.QLabel(Form)
        self.label_PrintMaxPlayServo.setObjectName("label_PrintMaxPlayServo")
        self.gridLayout_Analysis.addWidget(self.label_PrintMaxPlayServo, 2, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_Analysis, 5, 0, 1, 1)
        self.label_credits = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_credits.sizePolicy().hasHeightForWidth())
        self.label_credits.setSizePolicy(sizePolicy)
        self.label_credits.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.gridLayout.addWidget(self.label_credits, 8, 0, 1, 1)
        self.gridLayout_Geom = QtWidgets.QGridLayout()
        self.gridLayout_Geom.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_Geom.setObjectName("gridLayout_Geom")
        self.label_S = QtWidgets.QLabel(Form)
        self.label_S.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_S.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_S.setObjectName("label_S")
        self.gridLayout_Geom.addWidget(self.label_S, 1, 0, 1, 1)
        self.doubleSpinBox_S = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_S.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_S.setSizePolicy(sizePolicy)
        self.doubleSpinBox_S.setDecimals(3)
        self.doubleSpinBox_S.setMinimum(0.0)
        self.doubleSpinBox_S.setMaximum(100000.0)
        self.doubleSpinBox_S.setSingleStep(0.5)
        self.doubleSpinBox_S.setProperty("value", 1000.0)
        self.doubleSpinBox_S.setObjectName("doubleSpinBox_S")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_S, 1, 1, 1, 1)
        self.label_T01 = QtWidgets.QLabel(Form)
        self.label_T01.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_T01.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T01.setObjectName("label_T01")
        self.gridLayout_Geom.addWidget(self.label_T01, 3, 0, 1, 1)
        self.label_SLengthOffset = QtWidgets.QLabel(Form)
        self.label_SLengthOffset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_SLengthOffset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_SLengthOffset.setObjectName("label_SLengthOffset")
        self.gridLayout_Geom.addWidget(self.label_SLengthOffset, 3, 3, 1, 1)
        self.label_Geometry = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Geometry.sizePolicy().hasHeightForWidth())
        self.label_Geometry.setSizePolicy(sizePolicy)
        self.label_Geometry.setObjectName("label_Geometry")
        self.gridLayout_Geom.addWidget(self.label_Geometry, 0, 0, 1, 1)
        self.doubleSpinBox_SLengthOffset = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_SLengthOffset.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_SLengthOffset.setSizePolicy(sizePolicy)
        self.doubleSpinBox_SLengthOffset.setDecimals(3)
        self.doubleSpinBox_SLengthOffset.setMinimum(-100000.0)
        self.doubleSpinBox_SLengthOffset.setMaximum(100000.0)
        self.doubleSpinBox_SLengthOffset.setSingleStep(0.5)
        self.doubleSpinBox_SLengthOffset.setProperty("value", 4.358)
        self.doubleSpinBox_SLengthOffset.setObjectName("doubleSpinBox_SLengthOffset")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_SLengthOffset, 3, 4, 1, 1)
        self.doubleSpinBox_R1 = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_R1.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_R1.setSizePolicy(sizePolicy)
        self.doubleSpinBox_R1.setDecimals(3)
        self.doubleSpinBox_R1.setMinimum(0.0)
        self.doubleSpinBox_R1.setMaximum(100000.0)
        self.doubleSpinBox_R1.setSingleStep(0.5)
        self.doubleSpinBox_R1.setProperty("value", 50.0)
        self.doubleSpinBox_R1.setObjectName("doubleSpinBox_R1")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_R1, 2, 1, 1, 1)
        self.label_R1 = QtWidgets.QLabel(Form)
        self.label_R1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_R1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_R1.setObjectName("label_R1")
        self.gridLayout_Geom.addWidget(self.label_R1, 2, 0, 1, 1)
        self.label_SArmLength = QtWidgets.QLabel(Form)
        self.label_SArmLength.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_SArmLength.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_SArmLength.setObjectName("label_SArmLength")
        self.gridLayout_Geom.addWidget(self.label_SArmLength, 2, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_Geom.addWidget(self.line_2, 3, 2, 1, 1)
        self.doubleSpinBox_T01 = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_T01.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_T01.setSizePolicy(sizePolicy)
        self.doubleSpinBox_T01.setDecimals(3)
        self.doubleSpinBox_T01.setMinimum(-90.0)
        self.doubleSpinBox_T01.setMaximum(90.0)
        self.doubleSpinBox_T01.setSingleStep(0.5)
        self.doubleSpinBox_T01.setProperty("value", 5.0)
        self.doubleSpinBox_T01.setObjectName("doubleSpinBox_T01")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_T01, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_Geom.addWidget(self.line, 2, 2, 1, 1)
        self.doubleSpinBox_SArmLength = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_SArmLength.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_SArmLength.setSizePolicy(sizePolicy)
        self.doubleSpinBox_SArmLength.setDecimals(3)
        self.doubleSpinBox_SArmLength.setMinimum(0.0)
        self.doubleSpinBox_SArmLength.setMaximum(100000.0)
        self.doubleSpinBox_SArmLength.setSingleStep(0.5)
        self.doubleSpinBox_SArmLength.setProperty("value", 99.619)
        self.doubleSpinBox_SArmLength.setObjectName("doubleSpinBox_SArmLength")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_SArmLength, 2, 4, 1, 1)
        self.label_R2 = QtWidgets.QLabel(Form)
        self.label_R2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_R2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_R2.setObjectName("label_R2")
        self.gridLayout_Geom.addWidget(self.label_R2, 4, 0, 1, 1)
        self.doubleSpinBox_R2 = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_R2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_R2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_R2.setDecimals(3)
        self.doubleSpinBox_R2.setMinimum(0.0)
        self.doubleSpinBox_R2.setMaximum(100000.0)
        self.doubleSpinBox_R2.setSingleStep(0.5)
        self.doubleSpinBox_R2.setProperty("value", 60.0)
        self.doubleSpinBox_R2.setObjectName("doubleSpinBox_R2")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_R2, 4, 1, 1, 1)
        self.label_HArmLength = QtWidgets.QLabel(Form)
        self.label_HArmLength.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_HArmLength.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_HArmLength.setObjectName("label_HArmLength")
        self.gridLayout_Geom.addWidget(self.label_HArmLength, 4, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_Geom.addWidget(self.line_3, 4, 2, 1, 1)
        self.doubleSpinBox_HArmLength = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_HArmLength.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_HArmLength.setSizePolicy(sizePolicy)
        self.doubleSpinBox_HArmLength.setDecimals(3)
        self.doubleSpinBox_HArmLength.setMinimum(0.0)
        self.doubleSpinBox_HArmLength.setMaximum(100000.0)
        self.doubleSpinBox_HArmLength.setSingleStep(0.5)
        self.doubleSpinBox_HArmLength.setProperty("value", 120.0)
        self.doubleSpinBox_HArmLength.setObjectName("doubleSpinBox_HArmLength")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_HArmLength, 4, 4, 1, 1)
        self.label_T02 = QtWidgets.QLabel(Form)
        self.label_T02.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_T02.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T02.setObjectName("label_T02")
        self.gridLayout_Geom.addWidget(self.label_T02, 5, 0, 1, 1)
        self.doubleSpinBox_T02 = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_T02.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_T02.setSizePolicy(sizePolicy)
        self.doubleSpinBox_T02.setDecimals(3)
        self.doubleSpinBox_T02.setMinimum(-90.0)
        self.doubleSpinBox_T02.setMaximum(90.0)
        self.doubleSpinBox_T02.setSingleStep(0.5)
        self.doubleSpinBox_T02.setObjectName("doubleSpinBox_T02")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_T02, 5, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_Geom.addWidget(self.line_4, 5, 2, 1, 1)
        self.label_HLengthOffset = QtWidgets.QLabel(Form)
        self.label_HLengthOffset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_HLengthOffset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_HLengthOffset.setObjectName("label_HLengthOffset")
        self.gridLayout_Geom.addWidget(self.label_HLengthOffset, 5, 3, 1, 1)
        self.doubleSpinBox_HLengthOffset = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_HLengthOffset.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_HLengthOffset.setSizePolicy(sizePolicy)
        self.doubleSpinBox_HLengthOffset.setDecimals(3)
        self.doubleSpinBox_HLengthOffset.setMinimum(-100000.0)
        self.doubleSpinBox_HLengthOffset.setMaximum(100000.0)
        self.doubleSpinBox_HLengthOffset.setSingleStep(0.5)
        self.doubleSpinBox_HLengthOffset.setObjectName("doubleSpinBox_HLengthOffset")
        self.gridLayout_Geom.addWidget(self.doubleSpinBox_HLengthOffset, 5, 4, 1, 1)
        self.toolButton_help = QtWidgets.QToolButton(Form)
        self.toolButton_help.setObjectName("toolButton_help")
        self.gridLayout_Geom.addWidget(self.toolButton_help, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_Geom, 3, 0, 1, 1)

        self.Language = "English"  # Sets default language

        self.retranslateUi(Form, self.Language)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # SET CONNECTIONS
        # Servo input data
        self.doubleSpinBox_R1.editingFinished.connect(self.updateServoOffset)
        self.doubleSpinBox_T01.editingFinished.connect(self.updateServoOffset)
        self.doubleSpinBox_SArmLength.editingFinished.connect(self.updateServoOffsetBack)
        self.doubleSpinBox_SLengthOffset.editingFinished.connect(self.updateServoOffsetBack)
        self.doubleSpinBox_R1.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_T01.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_SArmLength.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_SLengthOffset.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_S.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_R2.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_T02.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_HArmLength.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_HLengthOffset.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_T1opt.valueChanged.connect(self.whiteServo)
        self.doubleSpinBox_T2opt.valueChanged.connect(self.whiteServo)
        # Control horn input data
        self.doubleSpinBox_R2.editingFinished.connect(self.updateHingeOffset)
        self.doubleSpinBox_T02.editingFinished.connect(self.updateHingeOffset)
        self.doubleSpinBox_HArmLength.editingFinished.connect(self.updateHingeOffsetBack)
        self.doubleSpinBox_HLengthOffset.editingFinished.connect(self.updateHingeOffsetBack)
        self.pushButton_Calculate.pressed.connect(self.calculate)  # Performs analysis
        self.pushButton_PlotResult.pressed.connect(self.plot)  # Plots the results
        self.pushButton_Optimize.pressed.connect(self.optimize)  # Optimizes the geometry
        # Language
        self.pushButton_English.pressed.connect(self.englishPressed)
        self.pushButton_Spanish.pressed.connect(self.spanishPressed)
        self.pushButton_French.pressed.connect(self.frenchPressed)
        # Help
        self.toolButton_help.pressed.connect(self.helpPressed)

    def helpPressed(self):
        width = 860
        height = 316
        if self.Language is "English":
            title = "Help"
            help_image = "PPengHelpT.png"
        elif self.Language is "Spanish":
            title = "Ayuda"
            help_image = "PPespHelpT.png"
        elif self.Language is "French":
            title = "Aide"
            help_image = "PPfraHelpT.png"

        self.HelpDialog = Help(Form)
        self.HelpDialog.setWindowTitle(title)
        self.HelpDialog.setMinimumHeight(height)
        self.HelpDialog.setMaximumHeight(height)
        self.HelpDialog.setMinimumWidth(width)
        self.HelpDialog.setMaximumWidth(width)
        self.labelHelp = QtWidgets.QLabel(self.HelpDialog)
        myPixmap = QtGui.QPixmap(help_image)
        self.labelHelp.setPixmap(myPixmap)
        self.HelpDialog.show()

    def englishPressed(self):
        self.Language = "English"
        self.retranslateUi(Form, self.Language)

    def spanishPressed(self):
        self.Language = "Spanish"
        self.retranslateUi(Form, self.Language)

    def frenchPressed(self):
        self.Language = "French"
        self.retranslateUi(Form, self.Language)

    def retranslateUi(self, Form, Language):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pull-Pull Calculator"))
        Form.setWindowIcon(QtGui.QIcon("PPicoH.png"))
        if Language is "English":
            self.pushButton_English.setText(_translate("Form", "English"))
            self.pushButton_Spanish.setText(_translate("Form", "Español"))
            self.pushButton_French.setText(_translate("Form", "Français"))
            self.doubleSpinBox_T2opt.setSuffix(_translate("Form", " deg"))
            self.label_Design.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Design Data:</span></p></body></html>"))
            self.doubleSpinBox_T1opt.setSuffix(_translate("Form", " deg"))
            self.label_T1opt.setToolTip(_translate("Form", "Servo deflection at which optimum rudder deflection shall be obtained.\n"
            "At this point, zero play is obtained."))
            self.label_T1opt.setText(_translate("Form", "Optimum Servo Deflection"))
            self.label_T2opt.setToolTip(_translate("Form", "Rudder deflection at which optimum servo deflection shall be obtained.\n"
            "At this point, zero play is obtained."))
            self.label_T2opt.setText(_translate("Form", "Optimum Rudder Deflection"))
            self.pushButton_Optimize.setToolTip(_translate("Form", "Find the optimum servo arm length and offset for the given constraints."))
            self.pushButton_Optimize.setText(_translate("Form", "Optimize"))
            self.label_PrintMaxPlay.setText(_translate("Form", "<Calculate case>"))
            self.label_MaxPlay.setText(_translate("Form", "Maximum Rudder Play:"))
            self.label_MaxPlayRudderDefl.setToolTip(_translate("Form", "Rudder deflection at which maximum rudder play is produced."))
            self.label_MaxPlayRudderDefl.setText(_translate("Form", "@ Rudder Deflection:"))
            self.label_MaxPlayServo.setToolTip(_translate("Form", "Servo deflection at which maximum rudder play is produced."))
            self.label_MaxPlayServo.setText(_translate("Form", "@ Servo Deflection:"))
            self.pushButton_PlotResult.setToolTip(_translate("Form", "Plot the last calculated case."))
            self.pushButton_PlotResult.setText(_translate("Form", "Plot Result"))
            self.label_Analysis.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Analysis Data:</span></p></body></html>"))
            self.pushButton_Calculate.setToolTip(_translate("Form", "Launch the analysis"))
            self.pushButton_Calculate.setText(_translate("Form", "Calculate"))
            self.label_steps.setToolTip(_translate("Form", "Total number of analysis points from 0 up to Max Servo Deflection.\n"
            "Higher values improve the Rudder Play diagnosis accuracy, but\n"
            "the analysis and Optimization may slow down.\n"
            "Recommended value: 50"))
            self.label_steps.setText(_translate("Form", "# of steps"))
            self.doubleSpinBox_T1max.setSuffix(_translate("Form", " deg"))
            self.label_T1max.setToolTip(_translate("Form", "The analysis will be made from 0 up to this servo deflection value."))
            self.label_T1max.setText(_translate("Form", "Max Servo Deflection"))
            self.label_PrintMaxPlayRudderDefl.setText(_translate("Form", "<Calculate case>"))
            self.label_PrintMaxPlayServo.setText(_translate("Form", "<Calculate case>"))
            self.label_credits.setText(_translate("Form", "Pull-Pull Calculator v1.0 by Luis Bernardos - luisfco.bernardos@gmail.com"))
            self.label_S.setToolTip(_translate("Form", "Distance between the servo head and the hinge axis."))
            self.label_S.setText(_translate("Form", "Servo-Hinge Distance"))
            self.doubleSpinBox_S.setSuffix(_translate("Form", " mm"))
            self.label_T01.setToolTip(_translate("Form", "Offset of the servo link point measured in degrees from\n"
            "the perpendicular line of the Servo-Hinge line."))
            self.label_T01.setText(_translate("Form", "Servo Angle Offset"))
            self.label_SLengthOffset.setToolTip(_translate("Form", "Distance between the servo arm link-point and the perpendicular\n"
            "line of the servo-hinge line passing through the servo head."))
            self.label_SLengthOffset.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Servo Length Offset</span></p></body></html>"))
            self.label_Geometry.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Geometry Data:</span></p></body></html>"))
            self.doubleSpinBox_SLengthOffset.setSuffix(_translate("Form", " mm"))
            self.doubleSpinBox_R1.setSuffix(_translate("Form", " mm"))
            self.label_R1.setToolTip(_translate("Form", "Distance between the servo head and the servo arm link point."))
            self.label_R1.setText(_translate("Form", "Servo Arm Radius"))
            self.label_SArmLength.setToolTip(_translate("Form", "Distance between the link-points of the servo arm."))
            self.label_SArmLength.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Servo Arm Length</span></p></body></html>"))
            self.doubleSpinBox_T01.setSuffix(_translate("Form", " deg"))
            self.doubleSpinBox_SArmLength.setSuffix(_translate("Form", " mm"))
            self.label_R2.setToolTip(_translate("Form", "Distance between the hinge axis and the control horn link point."))
            self.label_R2.setText(_translate("Form", "Horn Radius"))
            self.doubleSpinBox_R2.setSuffix(_translate("Form", " mm"))
            self.label_HArmLength.setToolTip(_translate("Form", "Distance between the link-points of the rudder control horn."))
            self.label_HArmLength.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Horn Arm Length</span></p></body></html>"))
            self.doubleSpinBox_HArmLength.setSuffix(_translate("Form", " mm"))
            self.label_T02.setToolTip(_translate("Form", "Offset of the control horn link point measured in degrees from\n"
            "the perpendicular line of the Servo-Hinge line."))
            self.label_T02.setText(_translate("Form", "Horn Angle Offset"))
            self.doubleSpinBox_T02.setSuffix(_translate("Form", " deg"))
            self.label_HLengthOffset.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Horn Length Offset</span></p></body></html>"))
            self.doubleSpinBox_HLengthOffset.setSuffix(_translate("Form", " mm"))
            self.label_HLengthOffset.setToolTip(_translate("Form", "Distance between the horn link-point and the perpendicular\n"
            "line of the servo-hinge line passing through the hinge axis."))
            self.toolButton_help.setText(_translate("Form", "?"))
        elif Language is "Spanish":
            self.pushButton_English.setText(_translate("Form", "English"))
            self.pushButton_Spanish.setText(_translate("Form", "Español"))
            self.pushButton_French.setText(_translate("Form", "Français"))
            self.doubleSpinBox_T2opt.setSuffix(_translate("Form", " º"))
            self.label_Design.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Diseño:</span></p></body></html>"))
            self.doubleSpinBox_T1opt.setSuffix(_translate("Form", " º"))
            self.label_T1opt.setToolTip(_translate("Form", "Deflexión de servo a la cual se alcanza la deflexión óptima de timón.\n"
            "En este punto, el juego es cero."))
            self.label_T1opt.setText(_translate("Form", "Deflexión de servo óptima"))
            self.label_T2opt.setToolTip(_translate("Form", "Deflexión de timón a la cual se alcanza la deflexión óptima de servo.\n"
            "En este punto, el juego es cero."))
            self.label_T2opt.setText(_translate("Form", "Deflexión de timón óptima"))
            self.pushButton_Optimize.setToolTip(_translate("Form", "Halla la longitud de brazo de servo y desviación óptimos para las condiciones impuestas."))
            self.pushButton_Optimize.setText(_translate("Form", "Optimizar"))
            self.label_PrintMaxPlay.setText(_translate("Form", "<Calcule un caso>"))
            self.label_MaxPlay.setText(_translate("Form", "Máximo juego del timón:"))
            self.label_MaxPlayRudderDefl.setToolTip(_translate("Form", "Deflexión de timón a la cual se produce el máximo juego."))
            self.label_MaxPlayRudderDefl.setText(_translate("Form", "A la deflexión de timón:"))
            self.label_MaxPlayServo.setToolTip(_translate("Form", "Deflexión del servo a la cual el máximo juego se produce."))
            self.label_MaxPlayServo.setText(_translate("Form", "A la deflexión de servo:"))
            self.pushButton_PlotResult.setToolTip(_translate("Form", "Representa el último caso calculado."))
            self.pushButton_PlotResult.setText(_translate("Form", "Traza el resultado"))
            self.label_Analysis.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Análisis:</span></p></body></html>"))
            self.pushButton_Calculate.setToolTip(_translate("Form", "Lanza el cálculo"))
            self.pushButton_Calculate.setText(_translate("Form", "Calcular"))
            self.label_steps.setToolTip(_translate("Form", "Número total de puntos de cálculo desde 0 hasta Deflexión Máx Servo.\n"
            "Valores más elevados mejoran la precisión del diagnóstico del juego del timón, pero\n"
            "tanto el cálculo como la optimización tardará más en realizarse.\n"
            "Valor recomendado: 50"))
            self.label_steps.setText(_translate("Form", "# de pasos"))
            self.doubleSpinBox_T1max.setSuffix(_translate("Form", " º"))
            self.label_T1max.setToolTip(_translate("Form", "El análisis se realizará desde 0 hasta este valor de deflexión de servo."))
            self.label_T1max.setText(_translate("Form", "Deflexión Máx Servo"))
            self.label_PrintMaxPlayRudderDefl.setText(_translate("Form", "<Calcule un caso>"))
            self.label_PrintMaxPlayServo.setText(_translate("Form", "<Calcule un caso>"))
            self.label_credits.setText(_translate("Form", "Pull-Pull Calculator v1.0 by Luis Bernardos - luisfco.bernardos@gmail.com"))
            self.label_S.setToolTip(_translate("Form", "Distancia entre la cabeza del servo y el eje de bisagra del timón."))
            self.label_S.setText(_translate("Form", "Distancia Servo-Bisagra"))
            self.doubleSpinBox_S.setSuffix(_translate("Form", " mm"))
            self.label_T01.setToolTip(_translate("Form", "Desviación del punto de anclaje de la transmisión en el brazo de servo, medido\n"
            "desde la línea perpendicular a la línea Servo-Bisagra que pasa por la cabeza del servo."))
            self.label_T01.setText(_translate("Form", "Ángulo de desviación del brazo"))
            self.label_SLengthOffset.setToolTip(_translate("Form", "Distancia entre el punto de anclaje de la transmisión en el brazo del servo hasta\n"
            "la línea que forma una perpendicular con la línea Servo-Bisagra y que pasa por la cabeza del servo."))
            self.label_SLengthOffset.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Longitud de desviación del brazo</span></p></body></html>"))
            self.label_Geometry.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Geometría:</span></p></body></html>"))
            self.doubleSpinBox_SLengthOffset.setSuffix(_translate("Form", " mm"))
            self.doubleSpinBox_R1.setSuffix(_translate("Form", " mm"))
            self.label_R1.setToolTip(_translate("Form", "Distancia entre la cabeza del servo y el punto de anclaje de la transmisión en el brazo."))
            self.label_R1.setText(_translate("Form", "Radio del brazo"))
            self.label_SArmLength.setToolTip(_translate("Form", "Distancia entre los dos puntos de anclaje de la transmisión en el brazo del servo"))
            self.label_SArmLength.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Longitud del brazo</span></p></body></html>"))
            self.doubleSpinBox_T01.setSuffix(_translate("Form", " º"))
            self.doubleSpinBox_SArmLength.setSuffix(_translate("Form", " mm"))
            self.label_R2.setToolTip(_translate("Form", "Distancia entre el eje de bisagras y el punto de anclaje de la transmisión en la escuadra de mando."))
            self.label_R2.setText(_translate("Form", "Radio de la escuadra"))
            self.doubleSpinBox_R2.setSuffix(_translate("Form", " mm"))
            self.label_HArmLength.setToolTip(_translate("Form", "Distancia entre los puntos de anclaje de la transmisión en la escuadra de mando."))
            self.label_HArmLength.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Longitud de la escuadra</span></p></body></html>"))
            self.doubleSpinBox_HArmLength.setSuffix(_translate("Form", " mm"))
            self.label_T02.setToolTip(_translate("Form", "Ángulo de desviación del punto de anclaje de la transmisión en la escuadra de mando desde\n"
            "la perpendicular a la línea de Servo-Brisagra."))
            self.label_T02.setText(_translate("Form", "Ángulo de desviación de la escuadra"))
            self.doubleSpinBox_T02.setSuffix(_translate("Form", " º"))
            self.label_HLengthOffset.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Longitud de desviación de la escuadra</span></p></body></html>"))
            self.doubleSpinBox_HLengthOffset.setSuffix(_translate("Form", " mm"))
            self.label_HLengthOffset.setToolTip(_translate("Form", "Distancia entre el anclaje de la transmisión de la escuadra y la perpendicular\n"
            "a la línea Servo-Bisagra que pasa por el eje de bisagra."))
            self.toolButton_help.setText(_translate("Form", "?"))
        elif Language is "French":
            self.pushButton_English.setText(_translate("Form", "English"))
            self.pushButton_Spanish.setText(_translate("Form", "Español"))
            self.pushButton_French.setText(_translate("Form", "Français"))
            self.doubleSpinBox_T2opt.setSuffix(_translate("Form", " º"))
            self.label_Design.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Conception:</span></p></body></html>"))
            self.doubleSpinBox_T1opt.setSuffix(_translate("Form", " º"))
            self.label_T1opt.setToolTip(_translate("Form", "Déflexion du servo à laquelle la déflexion optimale du volet est atteinte.\n"
            "Sur ce point, le jeu est nul."))
            self.label_T1opt.setText(_translate("Form", "Déflexion optimale du servo"))
            self.label_T2opt.setToolTip(_translate("Form", "Déflexion du volet à laquelle la déflexion optimale du servo est atteinte.\n"
            "Sur ce point, le jeu est nul."))
            self.label_T2opt.setText(_translate("Form", "Déflexion optimale du volet"))
            self.pushButton_Optimize.setToolTip(_translate("Form", "Trouve la longeur du palonnier et son décallage optimales pour les contraintes imposées."))
            self.pushButton_Optimize.setText(_translate("Form", "Optimiser"))
            self.label_PrintMaxPlay.setText(_translate("Form", "<Veuillez lancer un calcul>"))
            self.label_MaxPlay.setText(_translate("Form", "Jeu maximum du volet:"))
            self.label_MaxPlayRudderDefl.setToolTip(_translate("Form", "Déflexion du volet à laquelle le jeu maximum se produit."))
            self.label_MaxPlayRudderDefl.setText(_translate("Form", "Pour la déflexion du volet:"))
            self.label_MaxPlayServo.setToolTip(_translate("Form", "Déflexion du servo à laquelle le jeu maximum se produit."))
            self.label_MaxPlayServo.setText(_translate("Form", "Pour la déflexion du servo:"))
            self.pushButton_PlotResult.setToolTip(_translate("Form", "Trace le résultat du dernier cas calculé."))
            self.pushButton_PlotResult.setText(_translate("Form", "Trace le résultat"))
            self.label_Analysis.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Analyse:</span></p></body></html>"))
            self.pushButton_Calculate.setToolTip(_translate("Form", "Démarrer le calcul"))
            self.pushButton_Calculate.setText(_translate("Form", "Calculer"))
            self.label_steps.setToolTip(_translate("Form", "Nombre total de points de calcul depuis 0 jusqu'à la Déflexion Max Servo.\n"
            "Un grand nombre améliore la précision du diagnostique du jeu du volet, mais\n"
            "et le calcul et l'analyse mettront plus longtemps à s'effectuer.\n"
            "Valeur recommandé: 50"))
            self.label_steps.setText(_translate("Form", "nombre de pas"))
            self.doubleSpinBox_T1max.setSuffix(_translate("Form", " º"))
            self.label_T1max.setToolTip(_translate("Form", "L'analyse s'effectuera depuis 0 jusqu'à ce-valeur-ci indiquant la déflexion du servo."))
            self.label_T1max.setText(_translate("Form", "Déflexion Max Servo"))
            self.label_PrintMaxPlayRudderDefl.setText(_translate("Form", "<Veuillez lancer un calcul>"))
            self.label_PrintMaxPlayServo.setText(_translate("Form", "<Veuillez lancer un calcul>"))
            self.label_credits.setText(_translate("Form", "Pull-Pull Calculator v1.0 by Luis Bernardos - luisfco.bernardos@gmail.com"))
            self.label_S.setToolTip(_translate("Form", "Distance entre la tête du servo et l'axe de la charnière du volet."))
            self.label_S.setText(_translate("Form", "Distance Servo-Charnière"))
            self.doubleSpinBox_S.setSuffix(_translate("Form", " mm"))
            self.label_T01.setToolTip(_translate("Form", "Angle de décallage entre le point d'attachement de la transmission sur le palonnier du servo et la ligne\n"
            "perpendiculaire à la ligne Servo-Charnière qui passe par la tête du servo."))
            self.label_T01.setText(_translate("Form", "Angle de décallage du palonnier"))
            self.label_SLengthOffset.setToolTip(_translate("Form", "Distance entre le point d'attachement de la transmission sur le palonnier du servo jusqu'à la ligne\n"
            "perpendiculaire à la ligne Servo-Charnière qui passe par la tête du servo."))
            self.label_SLengthOffset.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Distance de décallage du palonnier</span></p></body></html>"))
            self.label_Geometry.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Géométrie:</span></p></body></html>"))
            self.doubleSpinBox_SLengthOffset.setSuffix(_translate("Form", " mm"))
            self.doubleSpinBox_R1.setSuffix(_translate("Form", " mm"))
            self.label_R1.setToolTip(_translate("Form", "Distance entre la tête du servo et le point d'attachement de la transmission sur le palonnier."))
            self.label_R1.setText(_translate("Form", "Rayon du palonnier"))
            self.label_SArmLength.setToolTip(_translate("Form", "Distance entre les deux points d'attachement de la transmission sur le palonnier du servo."))
            self.label_SArmLength.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Longueur du palonnier</span></p></body></html>"))
            self.doubleSpinBox_T01.setSuffix(_translate("Form", " º"))
            self.doubleSpinBox_SArmLength.setSuffix(_translate("Form", " mm"))
            self.label_R2.setToolTip(_translate("Form", "Distance entre l'axe de charnière et le point d'attachement de la transmission sur le guignol de gouverne."))
            self.label_R2.setText(_translate("Form", "Rayon du guignol"))
            self.doubleSpinBox_R2.setSuffix(_translate("Form", " mm"))
            self.label_HArmLength.setToolTip(_translate("Form", "Distance entre les deux points d'attachement du guignol de gouverne."))
            self.label_HArmLength.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Longueur du guignol</span></p></body></html>"))
            self.doubleSpinBox_HArmLength.setSuffix(_translate("Form", " mm"))
            self.label_T02.setToolTip(_translate("Form", "Angle de décallage entre le point d'attachement de la transmission sur le guignol de gouverne et\n"
            "la ligne perpendiculaire à la ligne Servo-Charnière qui passe par l'axe de charnière."))
            self.label_T02.setText(_translate("Form", "Angle de décallage du guignol"))
            self.doubleSpinBox_T02.setSuffix(_translate("Form", " º"))
            self.label_HLengthOffset.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Distance de décallage du palonnier</span></p></body></html>"))
            self.doubleSpinBox_HLengthOffset.setSuffix(_translate("Form", " mm"))
            self.label_HLengthOffset.setToolTip(_translate("Form", "Distance entre le point d'attachement de la transmission du guignol de gouverne et\n"
            "la ligne perpendiculaire à la ligne Servo-Charnière qui passe par l'axe de charnière."))
            self.toolButton_help.setText(_translate("Form", "?"))

    def updateServoOffset(self):  # Updates the Servo Offset because a value was changed
        R1 = self.doubleSpinBox_R1.value()
        T01 = self.doubleSpinBox_T01.value()
        self.doubleSpinBox_SArmLength.setValue(2 * R1 * cos(deg2rad(T01)))
        self.doubleSpinBox_SLengthOffset.setValue(R1 * sin(deg2rad(T01)))

    def updateServoOffsetBack(self):  # Updates the Servo Offset because a value was changed
        LongLeg = self.doubleSpinBox_SArmLength.value() / 2
        ShortLeg = self.doubleSpinBox_SLengthOffset.value()
        R1 = sqrt(LongLeg ** 2 + ShortLeg ** 2)
        T01 = rad2deg(arctan(ShortLeg / LongLeg))
        self.doubleSpinBox_R1.setValue(R1)
        self.doubleSpinBox_T01.setValue(T01)

    def updateHingeOffset(self):  # Updates the Hinge Offset because a value was changed
        R2 = self.doubleSpinBox_R2.value()
        T02 = self.doubleSpinBox_T02.value()
        self.doubleSpinBox_HArmLength.setValue(2 * R2 * cos(deg2rad(T02)))
        self.doubleSpinBox_HLengthOffset.setValue(R2 * sin(deg2rad(T02)))

    def updateHingeOffsetBack(self):  # Updates the Hinge Offset because a value was changed
        LongLeg = self.doubleSpinBox_HArmLength.value() / 2
        ShortLeg = self.doubleSpinBox_HLengthOffset.value()
        R1 = sqrt(LongLeg ** 2 + ShortLeg ** 2)
        T01 = rad2deg(arctan(ShortLeg / LongLeg))
        self.doubleSpinBox_R2.setValue(R1)
        self.doubleSpinBox_T02.setValue(T01)

    def whiteServo(self):
        self.setBackColor(self.doubleSpinBox_R1, 'white')
        self.setBackColor(self.doubleSpinBox_T01, 'white')
        self.setBackColor(self.doubleSpinBox_SArmLength, 'white')
        self.setBackColor(self.doubleSpinBox_SLengthOffset, 'white')

    def setBackColor(self, Widget, Color):
        if Color is 'red':
            C = (255, 20, 24)  # red color code
        elif Color is 'green':
            C = (178, 255, 157)  # green color code
        else:
            C = (255, 255, 255)  # white color code
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(C[0], C[1], C[2]))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        Widget.setPalette(palette)

    def getppData(self):
        self.S = self.doubleSpinBox_S.value()  # Gets the distance between servo and hinge
        self.R1 = self.doubleSpinBox_R1.value()  # Gets the servo arm radius
        self.T01 = self.doubleSpinBox_T01.value()  # Gets the servo arm offset angle
        self.R2 = self.doubleSpinBox_R2.value()  # Gets the ctrl horn radius
        self.T02 = self.doubleSpinBox_T02.value()  # Gets the ctrl horn offset angle
        self.T1max = self.doubleSpinBox_T1max.value()  # Gets the maximum servo deflection
        self.steps = self.spinBox_steps.value()  # Gets the analysis #of steps
        self.T1opt = self.doubleSpinBox_T1opt.value()  # Gets the opt point of servo
        self.T2opt = self.doubleSpinBox_T2opt.value()  # Gets the opt point of rudder

    def calculate(self):
        self.getppData()
        self.T1 = linspace(0, self.T1max, self.steps)  # Creates the vector T1 of analysis
        # Length of cable:
        self.L = sqrt((self.R1 * cos(deg2rad(self.T01)) + self.R2 * cos(deg2rad(self.T02))) ** 2 +
                      (self.S - self.R1 * sin(deg2rad(self.T01)) - self.R2 * sin(deg2rad(self.T02))) ** 2)
        # Rudder deflection:
        self.T2 = scipy.optimize.fsolve(diff_t2, self.T1, args=(self.T01, self.R1, self.L, self.T1, self),
                                        xtol=1e-6, maxfev=1000,
                                        factor=2, diag=None)
        # Rudder sloppy deflection:
        self.T22 = scipy.optimize.fsolve(diff_t22, self.T1, args=(self.T01, self.R1, self.L, self.T1, self),
                                         xtol=1e-6, maxfev=1000,
                                         factor=2, diag=None)
        self.PlayT2 = self.T2 - self.T22
        iMaxPlay = argmax(self.PlayT2)
        suffix = "º"
        if self.Language is "English": suffix = "deg"
        self.label_PrintMaxPlay.setText("%0.3f %s" % (self.PlayT2[iMaxPlay], suffix))
        self.label_PrintMaxPlayRudderDefl.setText("%0.3f+/-%0.3f %s" % (mean([self.T2[iMaxPlay], self.T22[iMaxPlay]]),
                                                                         abs(self.PlayT2[iMaxPlay]) / 2, suffix))
        self.label_PrintMaxPlayServo.setText("%0.3f %s" % (self.T1[iMaxPlay], suffix))

    def plot(self):
        try:
            self.T1
        except AttributeError:
            self.calculate()
        if self.Language is "English":
            label_MaxDefl = "MAX deflection"
            label_MinDefl = "MIN deflection"
            label_PlayT2 = "Rudder Play"
            xlabel = "Servo deflection (degrees)"
            ylabel = "Control surface deflection (degrees)"
        elif self.Language is "Spanish":
            label_MaxDefl = "deflexión MAX"
            label_MinDefl = "deflexión MIN"
            label_PlayT2 = "Juego de timón"
            xlabel = "Deflexión del servo (grados)"
            ylabel = "Deflexión del timón (grados)"
        elif self.Language is "French":
            label_MaxDefl = "Déflexion MAX"
            label_MinDefl = "Déflexion MIN"
            label_PlayT2 = "Jeu du volet"
            xlabel = "Déflexion du servo (degrés)"
            ylabel = "Déflexion du volet (degrés)"

        plt.figure()
        plt.plot(self.T1, self.T2, '-b', label=label_MaxDefl)
        plt.plot(self.T1, self.T22, ':b', label=label_MinDefl)
        plt.plot(self.T1, self.PlayT2, '.-r', label=label_PlayT2)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc='upper left')
        plt.show()

    def optimize(self):
        self.getppData()
        self.T1 = linspace(0, self.T1opt, self.steps)  # Creates the vector T1 of optimization
        OptRes = scipy.optimize.fsolve(optpoint, array([self.T01, self.R1]), args=self,
                                       xtol=1e-6, maxfev=1000,
                                       factor=2, diag=None)
        self.doubleSpinBox_T01.setValue(OptRes[0])
        self.doubleSpinBox_R1.setValue(OptRes[1])
        self.doubleSpinBox_T01.editingFinished.emit()
        self.setBackColor(self.doubleSpinBox_T01, 'green')
        self.setBackColor(self.doubleSpinBox_R1, 'green')
        self.setBackColor(self.doubleSpinBox_SArmLength, 'green')
        self.setBackColor(self.doubleSpinBox_SLengthOffset, 'green')
        self.calculate()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
