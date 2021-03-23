import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
dlgMain = QWidget()
#dlgMain = QDialog()
#dlgMain = QMessageBox() 
dlgMain.setWindowTitle("My GUI")
dlgMain.show()
sys.exit(app.exec_())