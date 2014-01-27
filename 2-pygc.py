from PyQt4.QtGui import QApplication, QLabel

def createLabel():
    label = QLabel("Hello, world!")
    label.show()

app = QApplication([])
createLabel()

app.exec_()
