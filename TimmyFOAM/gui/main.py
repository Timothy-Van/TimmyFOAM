import sys
from mainGUI_I import MainWindow
from setupGUI_I import SetupWindow
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)

    form1 = SetupWindow()
    form1.exec_()

    form2 = MainWindow()
    form2.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
