from PyQt4.QtGui import QApplication, QLabel

def createLabel():
    label = QLabel("Hello, world!")
    label.show()
    return label

app = QApplication([])
label = createLabel()

app.exec_()
