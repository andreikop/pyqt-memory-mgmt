"""Basic example for
    RuntimeError: Internal C++ object (Label) already deleted.

Works on PyQtx and Pyside
"""

from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication, QWidget


app = QApplication([])

widget = QWidget()
widget.setWindowTitle("Dead widget")
widget.deleteLater()

QTimer.singleShot(0, app.quit)
app.exec_()

print(widget.windowTitle())
