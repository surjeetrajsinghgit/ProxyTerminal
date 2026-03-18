import sys
import os
import subprocess
import urllib.parse
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QFormLayout, 
                             QLineEdit, QPushButton, QMessageBox)
from PyQt6.QtGui import QIcon 
from pathlib import Path         

class ProxyLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configure the main window
        self.setWindowTitle('Proxy Terminal {@SRS}')
        self.setFixedSize(350, 200)
        self.setWindowIcon(QIcon("C:/Users\\surje\\OneDrive\\Desktop\\proxy ui\\icon.png"))

        # Create layouts
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Create input fields
        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("e.g., 127.0.0.1")
        
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("e.g., 8080")
        
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Optional")
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Optional")
        # Hide the password characters
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        #enter key to submit 
        self.host_input.returnPressed.connect(self.focusNextChild)
        self.port_input.returnPressed.connect(self.focusNextChild)
        self.user_input.returnPressed.connect(self.focusNextChild)
        self.pass_input.returnPressed.connect(self.launch_cmd)        

        # Add fields to the form layout
        form_layout.addRow('Proxy IP/Host:', self.host_input)
        form_layout.addRow('Port:', self.port_input)
        form_layout.addRow('Username:', self.user_input)
        form_layout.addRow('Password:', self.pass_input)

        main_layout.addLayout(form_layout)

        # Create the launch button
        self.launch_btn = QPushButton('Launch Proxy Terminal')
        self.launch_btn.setFixedHeight(35)
        self.launch_btn.setStyleSheet("background-color: #3b8132 ; font-weight: bold; color: white; border-radius: 5px;")
        self.launch_btn.clicked.connect(self.launch_cmd)
        main_layout.addWidget(self.launch_btn)

        self.setLayout(main_layout)

    def launch_cmd(self):
        # Gather inputs
        host = self.host_input.text().strip()
        port = self.port_input.text().strip()
        user = self.user_input.text()
        password = self.pass_input.text()

        # Validation
        if not host or not port:
            QMessageBox.warning(self, "Error", "IP and Port are strictly required.")
            return

        # Safely URL-encode credentials and build the proxy string
        proxy_str = ""
        if user:
            # safe='' ensures even characters like '/' and '@' in passwords get encoded
            enc_user = urllib.parse.quote(user, safe='')
            enc_pass = urllib.parse.quote(password, safe='')
            proxy_str = f"http://{enc_user}:{enc_pass}@{host}:{port}"
        else:
            proxy_str = f"http://{host}:{port}"

        # Copy the current system environment variables
        env = os.environ.copy()
        
        # Inject our proxy settings into this copy
        env['http_proxy'] = proxy_str
        env['https_proxy'] = proxy_str

        try:
            # Launch a new independent CMD window with the modified environment
            # CREATE_NEW_CONSOLE ensures it opens a brand new black window
            subprocess.Popen(
                ['cmd.exe'], 
                env=env, 
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            
            # Optional: Uncomment the next line if you want the GUI to close after launching CMD
            self.close()
            
        except Exception as e:
            QMessageBox.critical(self, "Launch Error", f"Failed to launch CMD:\n{str(e)}")
#SRS
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Apply a cleaner, native-looking style
    app.setStyle('Fusion') 
    
    launcher = ProxyLauncher()
    launcher.show()
    sys.exit(app.exec())