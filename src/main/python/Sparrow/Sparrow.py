# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sparrow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 635)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.conversationTitleBar = QtWidgets.QTextBrowser(self.centralwidget)
        self.conversationTitleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.conversationTitleBar.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.conversationTitleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conversationTitleBar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.conversationTitleBar.setLineWidth(1)
        self.conversationTitleBar.setDocumentTitle("")
        self.conversationTitleBar.setObjectName("conversationTitleBar")
        self.verticalLayout.addWidget(self.conversationTitleBar)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.conversationList = QtWidgets.QListView(self.horizontalWidget)
        self.conversationList.setMaximumSize(QtCore.QSize(400, 16777215))
        self.conversationList.setStyleSheet("")
        self.conversationList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conversationList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.conversationList.setLineWidth(1)
        self.conversationList.setObjectName("conversationList")
        self.horizontalLayout.addWidget(self.conversationList)
        self.verticalWidget = QtWidgets.QWidget(self.horizontalWidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.conversationHistoryArea = QtWidgets.QScrollArea(self.verticalWidget)
        self.conversationHistoryArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.conversationHistoryArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conversationHistoryArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conversationHistoryArea.setWidgetResizable(True)
        self.conversationHistoryArea.setObjectName("conversationHistoryArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 736, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.conversationHistoryArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.conversationHistoryArea)
        self.messageWidget = QtWidgets.QWidget(self.verticalWidget)
        self.messageWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageWidget.sizePolicy().hasHeightForWidth())
        self.messageWidget.setSizePolicy(sizePolicy)
        self.messageWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.messageWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.messageWidget.setSizeIncrement(QtCore.QSize(0, 16))
        self.messageWidget.setBaseSize(QtCore.QSize(-1, 60))
        self.messageWidget.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.messageWidget.setObjectName("messageWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.messageWidget)
        self.horizontalLayout_2.setContentsMargins(9, 12, 0, 12)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.messageBox = QtWidgets.QTextEdit(self.messageWidget)
        self.messageBox.setMaximumSize(QtCore.QSize(16777215, 96))
        self.messageBox.setBaseSize(QtCore.QSize(0, 25))
        self.messageBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.messageBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.messageBox.setStyleSheet("border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 15px;\n"
"background-color: white;\n"
"padding: 4px 6px 4px 6px;\n"
"color: #111111;\n"
"font: normal 12px;")
        self.messageBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.messageBox.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.messageBox.setObjectName("messageBox")
        self.horizontalLayout_2.addWidget(self.messageBox)
        self.sendWidget = QtWidgets.QWidget(self.messageWidget)
        self.sendWidget.setObjectName("sendWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sendWidget)
        self.verticalLayout_3.setContentsMargins(4, 0, 8, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.sendButton = QtWidgets.QPushButton(self.sendWidget)
        self.sendButton.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.sendButton.setPalette(palette)
        self.sendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sendButton.setStyleSheet("border: none;\n"
"outline: none;")
        self.sendButton.setText("")
        self.sendButton.setIconSize(QtCore.QSize(32, 32))
        self.sendButton.setFlat(True)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout_3.addWidget(self.sendButton)
        self.horizontalLayout_2.addWidget(self.sendWidget)
        self.verticalLayout_2.addWidget(self.messageWidget)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuSparrow = QtWidgets.QMenu(self.menubar)
        self.menuSparrow.setObjectName("menuSparrow")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAcceptDrops(False)
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setCheckable(False)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAboutSparrow = QtWidgets.QAction(MainWindow)
        self.actionAboutSparrow.setObjectName("actionAboutSparrow")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setCheckable(True)
        font = QtGui.QFont()
        self.actionDark_Mode.setFont(font)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.action24Hour = QtWidgets.QAction(MainWindow)
        self.action24Hour.setCheckable(True)
        self.action24Hour.setChecked(True)
        self.action24Hour.setObjectName("action24Hour")
        self.actionAs_Sender = QtWidgets.QAction(MainWindow)
        self.actionAs_Sender.setCheckable(True)
        self.actionAs_Sender.setChecked(True)
        self.actionAs_Sender.setObjectName("actionAs_Sender")
        self.menuSparrow.addAction(self.actionAboutSparrow)
        self.menuSparrow.addSeparator()
        self.menuSparrow.addAction(self.actionPreferences)
        self.menuSparrow.addSeparator()
        self.menuSparrow.addAction(self.actionQuit)
        self.menuView.addAction(self.actionDark_Mode)
        self.menuView.addAction(self.action24Hour)
        self.menuView.addAction(self.actionAs_Sender)
        self.menubar.addAction(self.menuSparrow.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sparrow"))
        self.conversationTitleBar.setToolTip(_translate("MainWindow", "Name of the conversation"))
        self.conversationTitleBar.setStatusTip(_translate("MainWindow", "Conversation name"))
        self.conversationTitleBar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Manchester CS</span></p></body></html>"))
        self.conversationList.setToolTip(_translate("MainWindow", "A list of your conversations"))
        self.conversationList.setStatusTip(_translate("MainWindow", "Conversation list"))
        self.conversationHistoryArea.setStatusTip(_translate("MainWindow", "Conversation history"))
        self.messageBox.setStatusTip(_translate("MainWindow", "Message box"))
        self.messageBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.messageBox.setPlaceholderText(_translate("MainWindow", "Type a message..."))
        self.sendButton.setToolTip(_translate("MainWindow", "Sends the message"))
        self.sendButton.setStatusTip(_translate("MainWindow", "Send"))
        self.menuSparrow.setTitle(_translate("MainWindow", "Sparrow"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Quit the app"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit the app"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAboutSparrow.setText(_translate("MainWindow", "About Sparrow"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionDark_Mode.setToolTip(_translate("MainWindow", "Enables a darker environment"))
        self.actionDark_Mode.setStatusTip(_translate("MainWindow", "Enable a darker environment"))
        self.action24Hour.setText(_translate("MainWindow", "24h Format"))
        self.actionAs_Sender.setText(_translate("MainWindow", "As Sender"))


# Redefined MainWindow of the app
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setupIcons()
        if sys.platform.startswith("win"):
            self.setupForWindows()
        self.setupToolTipStyleSheet()
        self.setupSendButtonStyleSheet()
        self.setupMessageBox()
        self.setupTypingTimer()
        self.setupSparrowMenu()
        self.setupViewMenu()
        self.userSettingsDefaults()
        
        # Bullshit        
        self.setMouseTracking(True)
        self.installEventFilter(self)


# SETUP functions

    # Retrieves the correct icons for logo and buttons
    def setupIcons(self):
        #appIcon = QtGui.QIcon()
        #appIconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/logo.png")
        #appIcon.addPixmap(QtGui.QPixmap(appIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #MainWindow.setWindowIcon(self, appIcon)
        sendIcon = QtGui.QIcon()
        sendIconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/send.png")
        sendIcon.addPixmap(QtGui.QPixmap(sendIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(sendIcon)
        self.sendButton.setIconSize(QtCore.QSize(32, 32))


    # If platform is Windows, adapt some variables to keep the same behaviour
    def setupForWindows(self):
        self.messageWidget.setSizeIncrement(QtCore.QSize(0, 14))
        self.messageWidget.setMaximumSize(QtCore.QSize(16777215, 57))
        self.messageBox.setMaximumSize(QtCore.QSize(16777215, 93))
        self.messageBox.setBaseSize(QtCore.QSize(0, 22))
        self.conversationList.setFrameShape(QtWidgets.QFrame.VLine)
        self.conversationList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.conversationList.setLineWidth(1)
        self.conversationHistoryArea.setFrameShape(QtWidgets.QFrame.HLine)
        self.conversationHistoryArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.conversationHistoryArea.setLineWidth(1)
        self.conversationTitleBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conversationTitleBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.conversationTitleBar.setLineWidth(0)


    # Changes the style of all tooltips
    def setupToolTipStyleSheet(self):
        self.setStyleSheet("""
                            QToolTip 
                            { 
                              background-color: #DDDDDD; 
                              color: black; 
                              font: 12px;
                              padding: 2px;
                              border-width: 0px;
                              border-style: solid;
                              border-color: #DDDFFF;
                            }
                            """)


    # Changes the style of the send button
    def setupSendButtonStyleSheet(self):
        self.sendButton.setStyleSheet("""
                            QPushButton
                            {
                              border: none;
                              outline: none;
                            }
                            """)


    # Installs triggers to control message box logic
    def setupMessageBox(self):
        self.messageBox.installEventFilter(self)
        self.messageBox.textChanged.connect(self.updateMessageBoxAfterInput)
        self.sendButton.clicked.connect(self.sendMessage)
        self.lastMessageHeight = self.messageBox.baseSize().height()
        self.bubbleList = list()
        self.SEND = QtCore.Qt.LeftToRight
        self.RECEIVE = QtCore.Qt.RightToLeft


    # Creates timer to check typing status
    def setupTypingTimer(self):
        self.typingTimer =  QtCore.QTimer()
        self.typingTimer.setSingleShot(True)
        self.typingTimer.timeout.connect(self.updateTypingStatus)


    # Defines behaviour in the Sparrow menu
    def setupSparrowMenu(self):
        self.actionQuit.triggered.connect(QtWidgets.QApplication.quit)


    # Defines behaviour in the View menu
    def setupViewMenu(self):
        self.action24Hour.triggered.connect(self.toggleTimeFormat)
        self.actionAs_Sender.triggered.connect(self.DEBUG_toggleInputChannel) # DEBUG
        self.inputAsSender = True


    # User-changable variables:
    def userSettingsDefaults(self):
        self.time24HourFormat = True
        self.darkMode = False


# END setup functions


    # DEBUG FEATURE
    def DEBUG_toggleInputChannel(self):
        if self.inputAsSender:
          self.inputAsSender = False
        else:
          self.inputAsSender = True


    def toggleTimeFormat(self):
        if self.time24HourFormat:
          self.time24HourFormat = False
        else:
          self.time24HourFormat = True
        for bubble in self.bubbleList:
            bubble.updateToolTip()


    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            self.updateMessageBoxAfterResize()


    def eventFilter(self, source, event):

        if source is self.messageBox:
            if event.type() == QtCore.QEvent.KeyPress:
                shift = event.modifiers() & QtCore.Qt.ShiftModifier

                if shift and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter):
                    self.messageBox.append(" ")
                    return True
                elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
                    if self.messageBox.toPlainText() != "":
                        self.sendMessage()
                    return True

            if event.type() == QtCore.QEvent.Resize:
                self.updateMessageBoxAfterResize()

        return super(MainWindow, self).eventFilter(source, event)


    def sendMessage(self):
        direction = self.SEND if self.inputAsSender else self.RECEIVE # DEBUG
        bubble = MessageBubble(self, self.messageBox.toPlainText(), direction) # DEBUG "direction"
        self.bubbleList.append(bubble)
        self.messageBox.clear()
        self.messageWidget.setMaximumSize(QtCore.QSize(self.messageWidget.maximumSize().width(), self.messageWidget.baseSize().height()))


    def updateTypingStatus(self):
        self.statusbar.showMessage("")


    def updateMessageBoxAfterResize(self):
        actualContentHeight = self.messageBox.document().size().height()
        defaultContentHeight = self.messageBox.baseSize().height()

        defaultWidgetHeight = self.messageWidget.baseSize().height()
        actualWidgetWidth = self.messageWidget.maximumSize().width()
        actualWidgetHeight = self.messageWidget.maximumSize().height()
        incrementStep = self.messageWidget.sizeIncrement().height()

        rows = int((actualContentHeight - defaultContentHeight) / incrementStep)
        
        if actualContentHeight > defaultContentHeight:    
            if rows < 1:
                newHeight = defaultWidgetHeight
            else:
                newHeight = defaultWidgetHeight + rows * incrementStep
                if newHeight > 120:
                    newHeight = 120
                elif newHeight < 60:
                    newHeight = 60

            self.messageWidget.setMaximumSize(QtCore.QSize(actualWidgetWidth, newHeight))


    def updateMessageBoxAfterInput(self):
        self.typingTimer.start(500)
        self.statusbar.showMessage("Typing...")

        actualContentHeight = self.messageBox.document().size().height()

        actualWidgetWidth = self.messageWidget.maximumSize().width()
        actualWidgetHeight = self.messageWidget.maximumSize().height()
        incrementStep = self.messageWidget.sizeIncrement().height()
    
        if self.lastMessageHeight != actualContentHeight:
            difference = actualContentHeight - self.lastMessageHeight
            steps = int(difference / incrementStep)
            newHeight = actualWidgetHeight + incrementStep * steps
            if newHeight > 120:
                newHeight = 120
            elif newHeight < 60:
                newHeight = 60

            self.messageWidget.setMaximumSize(QtCore.QSize(actualWidgetWidth, newHeight))
            self.lastMessageHeight = actualContentHeight


# Speech bubble class
class MessageBubble():
    def __init__(self, appWindow: MainWindow, message, direction):
        self.window = appWindow
        self.setupLayout(direction)
        self.setupStyleSheet(direction)
        self.updateToolTip()
        self.setupText(message)


# SETUP functions


    # Generate required layout
    def setupLayout(self, direction):
        self.bubbleWidget = QtWidgets.QWidget(self.window.scrollAreaWidgetContents)
        self.bubbleWidget.setObjectName("bubbleWidget")
        horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bubbleWidget)
        horizontalLayout_3.setContentsMargins(12, 12, 12, 12)
        horizontalLayout_3.setSpacing(6)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout_3.addItem(spacerItem1)
        self.bubbleText = QtWidgets.QTextBrowser(self.bubbleWidget)
        self.bubbleText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bubbleText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bubbleText.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.bubbleText.setObjectName("bubbleText")
        horizontalLayout_3.addWidget(self.bubbleText)
        horizontalLayout_3.setStretch(1, 2)
        self.bubbleWidget.setLayoutDirection(direction)
        self.window.verticalLayout_4.addWidget(self.bubbleWidget)
        self.window.conversationHistoryArea.verticalScrollBar().setMaximum(self.window.conversationHistoryArea.verticalScrollBar().maximum() + self.bubbleText.maximumSize().height())
        self.window.conversationHistoryArea.verticalScrollBar().setValue(self.window.conversationHistoryArea.verticalScrollBar().maximum())


    # Generate required stylesheet
    def setupStyleSheet(self, direction):
        statusTip = "Sent by you" if direction == self.window.SEND else "Sent by {name}"
        background_color = "rgb(71, 183, 99);" if direction == self.window.SEND else "rgb(240,240,240);"
        color = "#ffffff;" if direction == self.window.SEND else "#000000;"
        self.bubbleText.setStyleSheet("""
                            QTextBrowser
                            {
                                border-style: outset;
                                border-width: 0px;
                                border-radius: 15px;
                                background-color: """ + background_color + """
                                padding: 5px 6px 5px 10px;
                                color: """ + color + """
                                font: normal 12px;
                            }
                            QToolTip 
                            { 
                                background-color: #DDDDDD; 
                                color: black; 
                                font: 12px;
                                padding: 2px;
                                border-width: 0px;
                                border-style: solid;
                                border-color: #DDDFFF;
                            }
                                   """)
        self.bubbleText.setStatusTip(statusTip)
        self.bubbleText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))


    # Update tooltip depending on general setting (24h or AM/PM)
    def updateToolTip(self):
        tooltipTimeStamp, historyTimeStamp = self.determineTimeStampFormat()
        self.bubbleText.setToolTip(tooltipTimeStamp) # NEEDS UPDATING TO PREVIOUS TUPLE


    # Retrieve the text and generate decent sizes for the bubble
    def setupText(self, text):
        document = QtGui.QTextDocument()
        document.setHtml(text)
        documentWidth = document.size().width()
        self.bubbleText.setDocument(document)
        messageWidth, messageHeight = self.determineMessageDimensions(documentWidth)
        self.bubbleWidget.setMaximumSize(QtCore.QSize(16777215, messageHeight))
        self.bubbleText.setMaximumSize(QtCore.QSize(messageWidth, 16777215))


# END setup functions


    # Helper function: check what time format the app is currently using
    def determineTimeStampFormat(self):
        if self.window.time24HourFormat:
          tooltipTimeStamp = time.strftime("%H:%M", time.localtime())
        else:
          tooltipTimeStamp = time.strftime("%I:%M %p", time.localtime())

        historyTimeStamp = tooltipTimeStamp

        return tooltipTimeStamp, historyTimeStamp


    # TODO: FIX THE HEIGHT JESUS
    # TODO: FIX UPDATE AFTER RESIZE
    # Helper function: check how big the bubble needs to be
    def determineMessageDimensions(self, documentWidth):
        width = 600
        height = 60
        
        someWidth = documentWidth + 22
        if someWidth <= 600:
            width = someWidth
        else:
            rows = int(someWidth / 600)
            width = 600
            height = 60 + rows * 16;
            if rows > 3:
                height += 16

        return width, height


################ MAIN ################
if __name__ == '__main__':
    from fbs_runtime.application_context import ApplicationContext
    from PyQt5.QtWidgets import QMainWindow
    import sys, os, time
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    Sparrow = MainWindow()
    Sparrow.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)