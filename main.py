from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys

class Calculator(QWidget):
    def __init__(self):
        """  super().__init__() is used to call the parent class's constructor from within a child class.
        This ensures that the parent class is properly initialized, allowing the child class to inherit
        and use its attributes and methods.
        If a child class defines its own __init__ method, it overrides the parent's. Without super().__init__(),
        the parent's setup code never runs, which can lead to errors when trying to access parent attributes
        """
        super().__init__()
        self.setWindowTitle("Feet to Centi-meter Calculator")

        grid = QGridLayout()

        enter_label = QLabel("Enter Value :")
        self.enter_box = QLineEdit()

        value_label = QLabel("( Feet or cm ) ")

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Feet (ft)", "Centimeter (cm)"])

        calculate_button = QPushButton("Convert")
        calculate_button.clicked.connect(self.calculate)
        self.output_label = QLabel("")

        grid.addWidget(enter_label, 0,0)
        grid.addWidget(self.enter_box, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(value_label, 1, 0)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)



app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())