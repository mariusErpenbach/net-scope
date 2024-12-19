from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget, QStackedWidget

class NetScopeUI(QWidget):
    def __init__(self):
        super().__init__()

        # Stacked Widget
        self.stacked_widget = QStackedWidget(self)

        # Main Page
        self.main_page = QWidget()
        self.main_layout = QVBoxLayout(self.main_page)

        self.scan_button = QPushButton("Scan Network", self.main_page)
        self.main_layout.addWidget(self.scan_button)

        self.devices_button = QPushButton("Show Connected Devices", self.main_page)
        self.main_layout.addWidget(self.devices_button)

        self.status_label = QLabel("Status: unknown", self.main_page)
        self.main_layout.addWidget(self.status_label)

        self.ms_label = QLabel("Latency: -ms", self.main_page)
        self.main_layout.addWidget(self.ms_label)

        self.local_ip_label = QLabel("Local IP: -", self.main_page)
        self.main_layout.addWidget(self.local_ip_label)

        # Devices Page
        self.devices_page = QWidget()
        self.device_layout = QVBoxLayout(self.devices_page)

        self.devices_label = QLabel("Devices:", self.devices_page)
        self.device_layout.addWidget(self.devices_label)

        self.back_button = QPushButton("Back", self.devices_page)
        self.device_layout.addWidget(self.back_button)

        # Stacked Widget Config
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.devices_page)

        # Hauptlayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Standard-Seite
        self.stacked_widget.setCurrentWidget(self.main_page)
