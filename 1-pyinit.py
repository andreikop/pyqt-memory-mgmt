from PySide.QtCore import QObject

class MyObject(QObject):
    def __init__(self):
        self.field = 7

obj = MyObject()
print(obj.field)
obj.setObjectName("New object")
