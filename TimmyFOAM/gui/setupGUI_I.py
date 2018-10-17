from PyQt5 import QtWidgets
import sys

import  UI.setupGUI 

class SetupWindow(QtWidgets.QDialog, UI.setupGUI.Ui_Dialog):
    """Documentation for SetupWindow

    """
    def __init__(self, parent=None):
        super(SetupWindow, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = SetupWindow()
    form.show() # form.exec_()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()

