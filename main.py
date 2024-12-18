import sys 
import subprocess 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout

class NetScope(QMainWindow): # NetScope class that inherits from QMainWindow
   
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Netscope - Network Monitor")
        self.setGeometry(100, 100, 1080, 720)

        # Layout
        self.centralWidget = QWidget() # Create centralWidget with QWidget class
        self.setCentralWidget(self.centralWidget) # Declare the new centralWidget as the centralWidget for the QMainWindow
        self.layout = QVBoxLayout(self.centralWidget) # Create a new layout with a vertical box and add it to the centralWidget

        # Button
        self.scan_button = QPushButton("Scan Network", self)
        self.scan_button.clicked.connect(self.check_connection)
        self.layout.addWidget(self.scan_button)

        # Labels for connection information
        self.status_label = QLabel("Status: unknown", self)
        self.layout.addWidget(self.status_label)
      
        self.ms_label = QLabel("Latency: -ms", self)
        self.layout.addWidget(self.ms_label)
        
    def check_connection(self):
        try:
            response = subprocess.run(
                ["ping", "-c", "1", "8.8.8.8"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if response.returncode == 0:
                self.status_label.setText("Status: Connected")
                output = response.stdout.decode()
                latency = self.extract_latency(output)
                self.ms_label.setText(f"Latency: {latency} ms")
            else:
                self.status_label.setText("Status: Not connected")
                self.ms_label.setText("Latency: -ms")
        except Exception as e:
            self.status_label.setText("Status: Error")
            self.ms_label.setText(f"Error: {str(e)}")

    def extract_latency(self, ping_output):
        for line in ping_output.splitlines():
            if "time=" in line:
                return line.split("time=")[-1].split(" ")[0]
        return "-"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetScope()
    window.show()
    sys.exit(app.exec_())
