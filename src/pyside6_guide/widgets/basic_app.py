"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a label to greet user
        self.hi_label = QLabel("Hello, ")
        self.greet_label = QLabel()
        



        # TODO: add a text input for user's name
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("What's your name?")
        self.user_input.textChanged.connect(self.greet_label.setText)
        
        self.username = self.user_input.text


        # TODO: add a push button to greet user

        self.greet_button = QPushButton("?")
        self.greet_button.clicked.connect(self.greet_button_clicked)

       
        

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.greet_button)
        layout.addWidget(self.user_input)
        layout.addWidget(self.hi_label)
        layout.addWidget(self.greet_label)
        
        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def greet_button_clicked(self):
        self.greet_button.setText("Greetings!")
    
    
    def edited(self, text):
        print(text)
        return (text)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
