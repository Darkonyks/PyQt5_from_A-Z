import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.resize(200, 200)

        btn = QPushButton("Show Message", self)
        btn.move(40, 40)
        btn.clicked.connect(self.evt_btn_clicked)

        btn1 = QPushButton("New information", self)
        btn1.move(40, 80)
        btn1.clicked.connect(self.evt_btn1_clicked)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, "Disk full", "Your disk is almost full")
        #warning
        print(res)
        if res == QMessageBox.Yes:
            QMessageBox.information(self, "", "You clicked YES")
        else:
            QMessageBox.information(self, "", "You clicked NO")

    def evt_btn1_clicked(self):
        msgDiskFull = QMessageBox()
        msgDiskFull.setText("Your disk is almost full")
        msgDiskFull.setDetailedText("Please make some space on your drive")
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setWindowTitle("Full Drive")
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()
   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())