"""Real life example of
    RuntimeError: Internal C++ object (Label) already deleted.

Works on PyQtx and Pyside
"""

from PyQt4.QtCore import Qt, QTimer
from PyQt4.QtGui import QApplication, QLabel, QLineEdit


def onLineEditTextChanged():
    print('~~~~ Line edit text changed')

def onLabelDestroyed():
    print('~~~~ C++ label object destroyed')

def changeLineEditText():
    print('~~~~ Changing line edit text')
    lineEdit.setText("New text")


class Label(QLabel):
    def __init__(self):
        QLabel.__init__(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.destroyed.connect(onLabelDestroyed)

    def __del__(self):
        print('~~~~ Python label object destroyed')

    def setText(self, text):
        print('~~~~ Changing label text')
        QLabel.setText(self, text)

    def close(self):
        print('~~~~ Closing label')
        QLabel.close(self)


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

label = Label()
label.show()

lineEdit = QLineEdit()
lineEdit.textChanged.connect(onLineEditTextChanged)
lineEdit.textChanged.connect(label.setText)


QTimer.singleShot(1000, label.close)
QTimer.singleShot(2000, changeLineEditText)
QTimer.singleShot(3000, app.quit)

app.exec_()

print('~~~~ Application exited')
