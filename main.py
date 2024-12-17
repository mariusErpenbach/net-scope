import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow

class NetScope(QMainWindow): #create NetScope class that inherits from QMainWindow 
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Netscope - Network Monitor")
        self.setGeometry(100,100,1080, 720)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetScope()
    window.show()
    sys.exit(app.exec_())

