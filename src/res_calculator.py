import sys
from equation import Equation
from symbols import Variable
from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class ResCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.equation = Equation()
        self.init_ui()

    def init_ui(self):
        # Create widgets
        title = QLabel('Resolution Calculator', self)
        self.variable_input = QLineEdit()
        button = QPushButton('Add Variable', self)
        self.variable_list = QLabel("",self)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.variable_input)
        layout.addWidget(button)

        # Create central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set central widget
        self.setCentralWidget(central_widget)

        # Connect button click event to a function
        button.clicked.connect(self.on_add_variable_button_click)

        # Set window properties
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Resolution Calculator')
        self.show()
        
    def on_add_variable_button_click(self):
        self.equation.add_variable(Variable(self.variable_input.text()))
        self.variable_list.setText(self.variable_list.text()+"\n"+self.variable_input.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = ResCalculator()
    sys.exit(app.exec_())
