import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog")
        self.resize(300, 300)

        self.btn = QPushButton("Enter name", self)
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.btn_age = QPushButton("Enter your age", self)
        self.btn_age.move(50, 80)
        self.btn_age.clicked.connect(self.evt_btn_age_clicked)

        self.btn_cost_coffee = QPushButton("Enter coffe price", self)
        self.btn_cost_coffee.move(50, 110)
        self.btn_cost_coffee.clicked.connect(self.evt_btn_cost_coffee_clicked)

        self.btn_color = QPushButton("Pick your color", self)
        self.btn_color.move(50, 140)
        self.btn_color.clicked.connect(self.evt_btn_color_clicked)

    def evt_btn_color_clicked(self):
        lstColor = ["Red", "Green", "Blue"]
        sColor, bOk = QInputDialog.getItem(self, "Color", "Pick your favorit color", lstColor, editable=False)
        if bOk:
            QMessageBox.information(self, "Color", "Your favorit color is " + sColor)
        else:
            QMessageBox.critical(self, "Text", "You did pick color")
            return

    def evt_btn_cost_coffee_clicked(self):
        sCoffe, bOk = QInputDialog.getDouble(self, "Price", "Please enter coffe price", 2.00, 0.10, 10.00, 2)
        if bOk:
            if sCoffe <= 5:
                QMessageBox.information(self, "Coffe price", "You paid your coffe " + str(sCoffe))
            if sCoffe > 5 :
                QMessageBox.question(self, "Price", "You realy paid {0} for the fu** coffe".format(sCoffe))
                res = QMessageBox.question(self, "Realy?", "No Realy you paid your coffe {0}".format(sCoffe))
                if res == QMessageBox.Yes:
                    QMessageBox.critical(self, "Idiote", "Ti stvarno nisi normalan")
                else:
                    QMessageBox.information(self, "Sala?", "dobro je nisi puko")
        else:
            QMessageBox.information(self, "", "User canceled")


        
    def evt_btn_age_clicked(self):
        sAge, bOk = QInputDialog.getInt(self, "Age", "Please enter your age", 18, 18, 65, 1)
        if bOk:
            QMessageBox.information(self, "Age", "Your age is " + str(sAge))
        else:
            QMessageBox.critical(self, "Error", "You did not entered your age")


    def evt_btn_clicked(self):
        sName, bOk = QInputDialog.getText(self, "Text", "Enter your name:")
        if bOk:
            QMessageBox.information(self, "Name", "Your name is " + sName)
        else:
            QMessageBox.critical(self, "Text", "You did not entered your name")
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
