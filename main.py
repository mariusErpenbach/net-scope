import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from network_utils import check_connection, scan_devices
from ui import NetScopeUI

class NetScope(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Netscope - Network Monitor")
        self.setGeometry(100, 100, 1080, 720)

        # UI-Setup
        self.ui = NetScopeUI()
        self.setCentralWidget(self.ui)

        # Button-Callbacks
        self.ui.scan_button.clicked.connect(self.check_connection)
        self.ui.devices_button.clicked.connect(self.show_devices_page)
        self.ui.back_button.clicked.connect(self.show_main_page)

    def check_connection(self):
        status, latency_or_error, local_ip = check_connection()
        self.ui.status_label.setText(f"Status: {status}")
        self.ui.ms_label.setText(
            f"Latency: {latency_or_error} ms" if status == "Connected" else f"{latency_or_error}"
        )
        self.ui.local_ip_label.setText(f"Local IP: {local_ip}")

    def show_devices_page(self):
        try:
            devices = scan_devices()  # Funktion zum Scannen aufrufen
            print(f"Scan result: {devices}")  # Debugging-Ausgabe in die Konsole

            # Überprüfen, ob Geräte gefunden wurden
            devices_text = "\n".join(devices) if devices else "No devices found."
            self.ui.devices_label.setText(devices_text)

        except Exception as e:
            # Fehler abfangen und im Label anzeigen
            print(f"Error while scanning devices: {e}")
            self.ui.devices_label.setText(f"Error: {e}")

        # Zur Geräte-Ansicht wechseln
        self.ui.stacked_widget.setCurrentWidget(self.ui.devices_page)

    def show_main_page(self):
        # Zur Hauptansicht zurückkehren
        self.ui.stacked_widget.setCurrentWidget(self.ui.main_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetScope()
    window.show()
    sys.exit(app.exec_())
