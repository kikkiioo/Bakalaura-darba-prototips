import sys
import requests
import os
import shutil
import colorsys
from colorir import *
from PIL import Image, ImageGrab, ImageQt
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QFileDialog,
    QScrollArea,
    QMainWindow,
    QSizePolicy,
    QSpacerItem,
    QDialog,
    QStackedWidget,
    QFrame,
    QGridLayout,
)
import json


class PageSetupWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        atslegvardi_nosaukums = QLabel(
            "Krāsas, kas tiks izmantotas tīmekļa vietnes dizainā:"
        )
        atslegvardi_nosaukums.setAlignment(Qt.AlignLeft)

        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setFamily("Times new Roman")

        hbox = QHBoxLayout()

        self.square1 = QLabel()
        hbox.addWidget(self.square1)

        self.square2 = QLabel()
        hbox.addWidget(self.square2)

        self.square3 = QLabel()
        hbox.addWidget(self.square3)

        self.square4 = QLabel()
        hbox.addWidget(self.square4)

        self.square5 = QLabel()
        hbox.addWidget(self.square5)

        download_button = QPushButton("Lejupielādēt gatavo tīmekļa vietni")

        vbox = QVBoxLayout()
        vbox.addWidget(atslegvardi_nosaukums)
        vbox.addLayout(hbox)
        vbox.addWidget(download_button)

        download_button.clicked.connect(self.on_download_button_clicked)
        vbox.addWidget(download_button)

        self.setLayout(vbox)

    def handlePageSetup(self, colors, selection):
        self.handleColorDisplay(colors)
        self.izveletais_tips = selection

    def handleColorDisplay(self, colors):
        hex_colors = ["#" + "".join(f"{c:02x}" for c in color) for color in colors]

        self.square1.setStyleSheet(f"background-color: {hex_colors[0]};")
        self.square2.setStyleSheet(f"background-color: {hex_colors[1]};")
        self.square3.setStyleSheet(f"background-color: {hex_colors[2]};")
        self.square4.setStyleSheet(f"background-color: {hex_colors[3]};")
        self.square5.setStyleSheet(f"background-color: {hex_colors[4]};")

        with open("colors.css", "w") as f:
            f.write(":root {\n")
            for i, color in enumerate(hex_colors):
                f.write(f"  --color-{i+1}: {color};\n")
            f.write("}\n")

    def on_download_button_clicked(self):
        folder_path = QFileDialog.getExistingDirectory(
            None, "Izvēlieties mapi, kurā glabāt vietni", ".", QFileDialog.ShowDirsOnly
        )

        if folder_path:
            new_folder_path = os.path.join(folder_path, "Timekla vietne")
            os.mkdir(new_folder_path)

            colors_file_path = os.path.join(os.getcwd(), "colors.css")
            shutil.copy2(colors_file_path, new_folder_path)

            atteli_path = os.path.join(os.getcwd(), "atteli")
            shutil.copytree(atteli_path, os.path.join(new_folder_path, "atteli"))

            if self.izveletais_tips == 0:
                business_folder_path = os.path.join(
                    os.getcwd(), "biznesa_timekla_vietnes"
                )
                shutil.copytree(
                    business_folder_path,
                    os.path.join(new_folder_path, "biznesa_vietnes"),
                )
            elif self.izveletais_tips == 1:
                portfolio_folder_path = os.path.join(
                    os.getcwd(), "portfolio_timekla_vietnes"
                )
                shutil.copytree(
                    portfolio_folder_path,
                    os.path.join(new_folder_path, "portfolio_vietnes"),
                )
            elif self.izveletais_tips == 2:
                portfolio_folder_path = os.path.join(
                    os.getcwd(), "interneta_veikala_timekla_vietnes"
                )
                shutil.copytree(
                    portfolio_folder_path,
                    os.path.join(new_folder_path, "interneta_veikala_vietnes"),
                )
