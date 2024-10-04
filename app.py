# This file is part of the GrowthRateApp project. 
#
# Copyright (C) 2024 Kristian Kinderlöv
#
# This program is free software; you can redistribute it and/or modify it under the terms of the 
# GNU Lesser General Public License as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along with this program;
# if not, see <http://www.gnu.org/licenses/>.
#
# Author: Kristian Kinderlöv
# Email: kristian.kinderlov@gmail.com

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox, QToolTip
from PySide6.QtGui import QFont, QDoubleValidator
from PySide6.QtCore import Qt

class GrowthRateApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Growth Rate Calculator')
        self.setFixedSize(300, 300)  # Set fixed size of the window
        
        main_layout = QVBoxLayout()
        
        # Font customization
        result_font = QFont("Arial", 14, QFont.Bold)

        # GroupBox for input fields
        input_groupbox = QGroupBox("Input Values")
        input_layout = QVBoxLayout()

        # Current Value
        current_layout = QVBoxLayout()
        current_label = QLabel("Current:")
        self.current_textbox = QLineEdit(self)
        self.current_textbox.setValidator(QDoubleValidator(0.0, 1000000.0, 2))
        self.current_textbox.textChanged.connect(self.calculate_growth_rate)
        current_layout.addWidget(current_label)
        current_layout.addWidget(self.current_textbox)

        # Initial Value
        initial_layout = QVBoxLayout()
        initial_label = QLabel("Initial:")
        self.initial_textbox = QLineEdit(self)
        self.initial_textbox.setValidator(QDoubleValidator(0.0, 1000000.0, 2))
        self.initial_textbox.textChanged.connect(self.calculate_growth_rate)
        initial_layout.addWidget(initial_label)
        initial_layout.addWidget(self.initial_textbox)

        # Year Value
        year_layout = QVBoxLayout()
        year_label = QLabel("Year:")
        self.year_textbox = QLineEdit(self)
        self.year_textbox.setValidator(QDoubleValidator(0.0, 1000.0, 2))
        self.year_textbox.setToolTip("Number of years")
        self.year_textbox.textChanged.connect(self.calculate_growth_rate)
        year_layout.addWidget(year_label)
        year_layout.addWidget(self.year_textbox)

        # Add input fields to the input groupbox layout
        input_layout.addLayout(current_layout)
        input_layout.addLayout(initial_layout)
        input_layout.addLayout(year_layout)
        input_groupbox.setLayout(input_layout)

        # GroupBox for result
        result_groupbox = QGroupBox("CAGR")
        result_layout = QVBoxLayout()
        #self.result_label = QLabel("Growth Rate: ")
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignHCenter)
        self.result_label.setAlignment(Qt.AlignVCenter)
        self.result_label.setFont(result_font)
        result_layout.addWidget(self.result_label, alignment=Qt.AlignCenter)
        result_groupbox.setLayout(result_layout)

        # Add groupboxes to the main layout
        main_layout.addWidget(input_groupbox)
        main_layout.addWidget(result_groupbox)

        self.setLayout(main_layout)
        self.show()

    def calculate_growth_rate(self):
        try:
            current_value = float(self.current_textbox.text())
            initial_value = float(self.initial_textbox.text())
            years = float(self.year_textbox.text())

            if initial_value == 0 or years == 0:
                self.result_label.setText("Error: Initial value and years must be non-zero.")
                return

            growth_rate = ((current_value / initial_value) ** (1 / years) - 1) * 100
            # self.result_label.setText(f"Growth Rate: {growth_rate:.2f}%")
            self.result_label.setText(f"{growth_rate:.2f}%")
        except ValueError:
            self.result_label.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GrowthRateApp()
    sys.exit(app.exec())
