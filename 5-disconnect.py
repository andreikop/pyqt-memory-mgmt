"""Real life example of
    RuntimeError: Internal C++ object (lineEdit) already deleted.

Works on PyQtx and Pyside
"""

PYSIDE = False
USE_SINGLESHOT = True

if PYSIDE:
    from PySide.QtCore import Qt, QTimer
    from PySide.QtGui import QApplication, QLineEdit
else:
    from PyQt4.QtCore import Qt, QTimer
    from PyQt4.QtGui import QApplication, QLineEdit


def onLineEditDestroyed():
    print('~~~~ C++ lineEdit object destroyed')

def onSelectionChanged():
    print('~~~~ Pure C++ method selectAll() called')


class LineEdit(QLineEdit):
    def __init__(self):
        QLineEdit.__init__(self)
        self.setText("foo bar")

        self.destroyed.connect(onLineEditDestroyed)
        #self.selectionChanged.connect(onSelectionChanged)

    def __del__(self):
        print('~~~~ Python lineEdit object destroyed')

    def clear(self):
        """Overriden Qt method
        """
        print('~~~~ Overriden method clear() called')
        QLineEdit.clear(self)

    def purePythonMethod(self):
        """Pure python method.
        Does not override any C++ methods
        """
        print('~~~~ Pure Python method called')
        self.windowTitle()  # generate exception


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

lineEdit = LineEdit()
lineEdit.deleteLater()


if USE_SINGLESHOT:
    #QTimer.singleShot(1000, lineEdit.clear)
    #QTimer.singleShot(1000, lineEdit.purePythonMethod)
    QTimer.singleShot(1000, lineEdit.selectAll)  # pure C++ method
else:
    timer = QTimer(None)
    timer.setSingleShot(True)
    timer.setInterval(1000)
    timer.start()

    #timer.timeout.connect(lineEdit.clear)
    #timer.timeout.connect(lineEdit.purePythonMethod)
    timer.timeout.connect(lineEdit.selectAll)  # pure C++ method


QTimer.singleShot(2000, app.quit)

app.exec_()

print('~~~~ Application exited')
