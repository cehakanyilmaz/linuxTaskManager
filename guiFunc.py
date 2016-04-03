from PyQt5 import QtCore, QtGui, QtWidgets
import xmlDosya,sys


class guiFunc(object):
    def showFunc(self):
        app =QtWidgets.QApplication(sys.argv)
        columnApp = QtWidgets.QMainWindow()
        ui = xmlDosya.Ui_MainWindow()
        ui.setupUi(columnApp)
        columnApp.show()
        sys.exit(app.exec_())