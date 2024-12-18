import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from network_utils import check_connection  # Import the check_connection function

class NetScope(QMainWindow):  # NetScope class that inherits from QMainWindow
   
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Netscope - Network Monitor")
        self.setGeometry(100, 100, 1080, 720)

        # Layout
        self.centralWidget = QWidget()  # Create centralWidget with QWidget class
        self.setCentralWidget(self.centralWidget)  # Declare the new centralWidget as the centralWidget for the QMainWindow
        self.layout = QVBoxLayout(self.centralWidget)  # Create a new layout with a vertical box and add it to the centralWidget

        # Button
        self.scan_button = QPushButton("Scan Network", self)
        self.scan_button.clicked.connect(self.check_connection)
        self.layout.addWidget(self.scan_button)

        # Labels for connection information
        self.status_label = QLabel("Status: unknown", self)
        self.layout.addWidget(self.status_label)
      
        self.ms_label = QLabel("Latency: -ms", self)
        self.layout.addWidget(self.ms_label)
        
        # Local Ip 
        self.local_ip_label = QLabel("Local IP: - ",self)
        self.layout.addWidget(self.local_ip_label)

    def check_connection(self):
        status, latency_or_error,local_ip = check_connection()  # Use the function from network_utils
        self.status_label.setText(f"Status: {status}")
        self.ms_label.setText(f"Latency: {latency_or_error} ms" if status == "Connected" else f"{latency_or_error}")
        self.local_ip_label.setText(f"Local IP: {local_ip}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetScope()
    window.show()
    sys.exit(app.exec_())
