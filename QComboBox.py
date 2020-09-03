from PySide2 import QtWidgets, QtGui, QtCore

class MaFenetre(QtWidgets.QWidget):
    def __init__(self):
        super(MaFenetre, self).__init__()
        self.setWindowTitle("La ComboBox")  
        self.resize(700, 700)
        self.initUi()
        
    def initUi(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_demo = QtWidgets.QComboBox(self)
        self.cbb_demo.addItems(["Zephrys", "Ras Murmegivre", "Uther", "Rexxar"])
        self.label_image = QtWidgets.QLabel(self)
        self.layout.addWidget(self.cbb_demo)
        self.layout.addWidget(self.label_image)
        self.cbb_demo.activated[str].connect(self.afficherImage)

    def afficherImage(self):
       self.pixmap1 = QtGui.QPixmap("Cartes Hearthstone Scholomance/Chaman/2227.jpg")
       self.pixmap2 = QtGui.QPixmap("Cartes Hearthstone Scholomance/Chaman/2763.jpg")
       if self.cbb_demo.currentText() == "Zephrys":
            self.label_image.setPixmap(self.pixmap1)
       elif self.cbb_demo.currentText() == "Ras Murmegivre":
            self.label_image.setPixmap(self.pixmap2)


app = QtWidgets.QApplication()
fenetre = MaFenetre()
fenetre.show()

app.exec_()