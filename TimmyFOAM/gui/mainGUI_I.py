from PyQt5 import QtWidgets
import sys


#import UI.mainGUI 
import UI.mainGUI 

class MainWindow(QtWidgets.QMainWindow, UI.mainGUI.Ui_MainWindow):
    """Documentation for MainWindo

    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menubar.setNativeMenuBar(False)

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    
    sys.exit(app.exec_())
        
            
