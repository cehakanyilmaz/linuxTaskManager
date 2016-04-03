import psutil, sys, xmlDosya, datetime
from PyQt5.QtWidgets import QTreeWidgetItem

class systemFunc(object):
    def systemData(self):
        pIDs = psutil.pids()
        process = []
        for i in pIDs:
            p = psutil.Process(i)
            pMet = p.name()
            pMet.append(str(i))
            pMet.append(str(p.cpu_percent()))
            pMet.append(str(p.memory_percent()))
            process.append(QTreeWidgetItem(pMet))
            pMet = []
        for j in process:
            xmlDosya.Ui_MainWindow.treeWidget.addTopLevelItem(j)
    b = datetime.datetime.now()