from __future__ import absolute_import

import sys
from PyQt5 import QtWidgets

# gui.mainGUI_I import MainWindow
import gui.setupGUI_I 

def main():
    app = QtWidgets.QApplication(sys.argv)
    formSetup = gui.setupGUI_I.SetupWindow()
    formSetup.exec_()

#    formMain = MainWindow()

#    formMain.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    
