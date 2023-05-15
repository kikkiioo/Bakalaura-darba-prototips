import sys
import requests
import os
import time
from PIL import Image
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
)

from kmeans import get_colors_from_image
from webPageSetup import PageSetupWidget


class InputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tipa_izvele_nosaukums = QLabel("Izvēlieties mājas lapas tipu")
        tipa_izvele_nosaukums.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

        self.tipa_izvele = QComboBox()
        self.tipa_izvele.addItems(["Bizness", "Portfolio", "Interneta veikals"])

        atslegvardi_nosaukums = QLabel("Atslēgvārdi tīmekļa vietnes ģenerēšanai")
        atslegvardi_nosaukums.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        atslegvardi_nosaukums.setFont(font)
        tipa_izvele_nosaukums.setFont(font)

        label1 = QLabel("Ievadiet galveno atslēgvārdu")
        self.teksta_ievade = QLineEdit()
        self.teksta_ievade.setFixedSize(250, 20)

        label2 = QLabel("Ievadiet papildus atslēgvārdus")
        self.teksta_ievade2 = QLineEdit()
        self.teksta_ievade2.setFixedSize(250, 20)
        self.teksta_ievade3 = QLineEdit()
        self.teksta_ievade3.setFixedSize(250, 20)
        self.teksta_ievade4 = QLineEdit()
        self.teksta_ievade4.setFixedSize(250, 20)

        vbox = QVBoxLayout()
        vbox.addWidget(tipa_izvele_nosaukums)
        vbox.addWidget(self.tipa_izvele)
        vbox.addWidget(atslegvardi_nosaukums)
        vbox.addWidget(label1)
        vbox.addWidget(self.teksta_ievade)
        vbox.addWidget(label2)
        vbox.addWidget(self.teksta_ievade2)
        vbox.addWidget(self.teksta_ievade3)
        vbox.addWidget(self.teksta_ievade4)

        self.setLayout(vbox)

        frame = QFrame(self)
        frame.setFrameStyle(QFrame.Box)
        frame.setStyleSheet(
            """
            QFrame {
                background-color: #E8D5C4;
                
            }
        """
        )

        frame.setLineWidth(1)
        frame.setMidLineWidth(0)
        frame.setLayout(vbox)

        frame.setFixedSize(300, 300)

        layout = QHBoxLayout(self)
        layout.addWidget(frame)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget(self)

        rtu = QLabel("Rīgas Tehniskā Universitāte")
        bakalaura_darbs = QLabel("Bakalaura darbs")
        studiju_programma = QLabel("Datorsistēmas")
        kurss = QLabel("3.kurss 3.grupa")
        vards_uzvards = QLabel("Kristiāna Heniņa")

        info_par_autoru = QVBoxLayout()
        info_par_autoru.addWidget(rtu)
        info_par_autoru.addWidget(bakalaura_darbs)
        info_par_autoru.addWidget(studiju_programma)
        info_par_autoru.addWidget(kurss)
        info_par_autoru.addWidget(vards_uzvards)

        info_par_autoru.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        ievades_forma = InputWidget()
        self.ievades_forma = ievades_forma

        otra_lapa = PageSetupWidget()
        self.otra_lapa = otra_lapa

        self.poga_atpakal = QPushButton("Atpakaļ")

        second = QVBoxLayout()
        second.addWidget(otra_lapa)
        second.addWidget(self.poga_atpakal)

        wid = QWidget()
        wid.setLayout(second)

        self.poga_atpakal.clicked.connect(self.next_page)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.attela_forma = QLabel()
        self.attela_forma.setAlignment(Qt.AlignCenter)
        self.attela_forma1 = QLabel()
        self.attela_forma1.setAlignment(Qt.AlignCenter)
        self.attela_forma2 = QLabel()
        self.attela_forma2.setAlignment(Qt.AlignCenter)
        self.attela_forma3 = QLabel()
        self.attela_forma3.setAlignment(Qt.AlignCenter)

        self.kreisa_poga = QPushButton("<")
        self.laba_poga = QPushButton(">")
        self.kreisa_poga1 = QPushButton("<")
        self.laba_poga1 = QPushButton(">")
        self.kreisa_poga2 = QPushButton("<")
        self.laba_poga2 = QPushButton(">")
        self.kreisa_poga3 = QPushButton("<")
        self.laba_poga3 = QPushButton(">")
        self.kreisa_poga4 = QPushButton("<")
        self.laba_poga4 = QPushButton(">")

        hbox = QHBoxLayout()
        hbox.addWidget(self.kreisa_poga, alignment=Qt.AlignCenter)
        hbox.addWidget(self.attela_forma, alignment=Qt.AlignTop)
        hbox.addWidget(self.laba_poga, alignment=Qt.AlignCenter)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.kreisa_poga1, alignment=Qt.AlignCenter)
        hbox1.addWidget(self.attela_forma1, alignment=Qt.AlignTop)
        hbox1.addWidget(self.laba_poga1, alignment=Qt.AlignCenter)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.kreisa_poga2, alignment=Qt.AlignCenter)
        hbox2.addWidget(self.attela_forma2, alignment=Qt.AlignTop)
        hbox2.addWidget(self.laba_poga2, alignment=Qt.AlignCenter)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.kreisa_poga3, alignment=Qt.AlignCenter)
        hbox3.addWidget(self.attela_forma3, alignment=Qt.AlignTop)
        hbox3.addWidget(self.laba_poga3, alignment=Qt.AlignCenter)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(ievades_forma, alignment=Qt.AlignTop)
        vbox2.setAlignment(Qt.AlignHCenter)

        self.poga_saglabat = QPushButton("Saglabāt izvēli")
        self.poga_saglabat.setEnabled(True)
        self.poga_nakama_lapa = QPushButton("Nākamais solis")
        self.poga_nakama_lapa.setEnabled(True)
        footer = QHBoxLayout()
        footer.addWidget(self.poga_saglabat)
        footer.addWidget(self.poga_nakama_lapa)

        vbox = QVBoxLayout()
        vbox.addLayout(info_par_autoru)
        vbox.addLayout(vbox2)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(footer)
        vbox.setContentsMargins(20, 20, 20, 20)
        self.setLayout(vbox)

        central_widget = QWidget()
        central_widget.setLayout(vbox)

        scroll_area.setWidget(central_widget)
        scroll_area.setFixedWidth(1500)
        scroll_area.setMinimumHeight(500)

        self.stacked_widget.addWidget(scroll_area)
        self.stacked_widget.addWidget(wid)

        self.setCentralWidget(self.stacked_widget)

        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle("Automātiska tīmekļa vietņu izstrāde")
        self.show()

        self.kreisa_poga.clicked.connect(self.show_previous_image)
        self.laba_poga.clicked.connect(self.show_next_image)

        self.kreisa_poga1.clicked.connect(self.show_previous_image)
        self.laba_poga1.clicked.connect(self.show_next_image)

        self.kreisa_poga2.clicked.connect(self.show_previous_image)
        self.laba_poga2.clicked.connect(self.show_next_image)

        self.kreisa_poga3.clicked.connect(self.show_previous_image)
        self.laba_poga3.clicked.connect(self.show_next_image)

        self.current_image_index = 0
        self.kreisa_poga.setEnabled(False)
        self.laba_poga.setEnabled(False)
        self.kreisa_poga1.setEnabled(False)
        self.laba_poga1.setEnabled(False)
        self.kreisa_poga2.setEnabled(False)
        self.laba_poga2.setEnabled(False)
        self.kreisa_poga3.setEnabled(False)
        self.laba_poga3.setEnabled(False)
        ievades_forma.teksta_ievade.returnPressed.connect(self.handle_input)
        ievades_forma.teksta_ievade2.returnPressed.connect(self.handle_input2)
        ievades_forma.teksta_ievade3.returnPressed.connect(self.handle_input3)
        ievades_forma.teksta_ievade4.returnPressed.connect(self.handle_input4)

        self.poga_saglabat.clicked.connect(self.save_current_image)
        self.poga_nakama_lapa.clicked.connect(self.next_page)
        self.poga_nakama_lapa.clicked.connect(self.handle_color)

        self.poga_nakama_lapa.setEnabled(False)

    def handle_input(self):
        text = self.ievades_forma.teksta_ievade.text()
        self.search_images(text, 1)

    def handle_input2(self):
        text = self.ievades_forma.teksta_ievade2.text()
        self.search_images(text, 2)

    def handle_input3(self):
        text = self.ievades_forma.teksta_ievade3.text()
        self.search_images(text, 3)

    def handle_input4(self):
        text = self.ievades_forma.teksta_ievade4.text()
        self.search_images(text, 4)

    def translate_text(self, text):
        URL = f"https://api.mymemory.translated.net/get?q={text}&langpair=lv|en"
        response = requests.get(URL)
        translation = response.json()["responseData"]["translatedText"]
        return translation

    def search_images(self, query, attela_forma):
        query = self.translate_text(query)
        api_key = "34683408-389739146796b837ff785d8e1"
        params = {
            "q": query,
            "per_page": 3,
            "image_type": "photo",
            "key": api_key,
            "previewWidth": 150,
            "previewHeight": 84,
        }
        response = requests.get("https://pixabay.com/api/", params=params)

        if response.status_code == 200:
            data = response.json().get("hits", [])
            if data:
                self.images = []
                for i, hit in enumerate(data):
                    image_url = hit.get("largeImageURL", "")
                    pixmap = QPixmap()
                    pixmap.loadFromData(requests.get(image_url).content)
                    self.images.append(pixmap)
                self.current_image_index = 0

                self.show_current_image(attela_forma)
                self.disableAllButtons()
                if attela_forma == 1:
                    self.kreisa_poga.setEnabled(len(self.images) > 1)
                    self.laba_poga.setEnabled(len(self.images) > 1)
                elif attela_forma == 2:
                    self.kreisa_poga1.setEnabled(len(self.images) > 1)
                    self.laba_poga1.setEnabled(len(self.images) > 1)
                elif attela_forma == 3:
                    self.laba_poga2.setEnabled(len(self.images) > 1)
                    self.kreisa_poga2.setEnabled(len(self.images) > 1)
                elif attela_forma == 4:
                    self.laba_poga3.setEnabled(len(self.images) > 1)
                    self.kreisa_poga3.setEnabled(len(self.images) > 1)
            else:
                print("No images found")
        else:
            print("API request failed")

    def show_previous_image(self):
        self.current_image_index -= 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.images) - 1
        self.show_current_image(self.label)

    def show_next_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.images):
            self.current_image_index = 0
        self.show_current_image(self.label)

    def show_current_image(self, label):
        pixmap = self.images[self.current_image_index]

        if label == 1:
            self.attela_forma.setPixmap(pixmap)
            self.label = 1
        elif label == 2:
            self.attela_forma1.setPixmap(pixmap)
            self.label = 2
        elif label == 3:
            self.attela_forma2.setPixmap(pixmap)
            self.label = 3
        elif label == 4:
            self.attela_forma3.setPixmap(pixmap)
            self.label = 4

    def save_current_image(self):
        for file_name in os.listdir("atteli"):
            file_path = os.path.join("atteli", file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(e)

        folder_path = "atteli"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        attela_cels = os.path.join(folder_path, f"main.png")
        pixmap = self.attela_forma.pixmap()

        attela_cels2 = os.path.join(folder_path, "second_image.png")
        pixmap2 = self.attela_forma1.pixmap()

        attela_cels3 = os.path.join(folder_path, "third_image.png")
        pixmap3 = self.attela_forma2.pixmap()

        attela_cels4 = os.path.join(folder_path, "fourth_image.png")
        pixmap4 = self.attela_forma3.pixmap()

        if pixmap:
            pixmap.save(attela_cels)
            pixmap2.save(attela_cels2)
            pixmap3.save(attela_cels3)
            pixmap4.save(attela_cels4)
            self.poga_nakama_lapa.setEnabled(True)

    def next_page(self):
        current_index = self.stacked_widget.currentIndex()
        next_index = (current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(next_index)

    def handle_color(self):
        image = Image.open("atteli/main.png")
        colors = get_colors_from_image(image, n_colors=5)
        selected_text = self.ievades_forma.tipa_izvele.currentIndex()
        self.otra_lapa.handlePageSetup(colors, selected_text)

    def disableAllButtons(self):
        self.kreisa_poga1.setDisabled(True)
        self.laba_poga1.setDisabled(True)
        self.kreisa_poga.setDisabled(True)
        self.laba_poga.setDisabled(True)
        self.kreisa_poga2.setDisabled(True)
        self.laba_poga2.setDisabled(True)
        self.kreisa_poga3.setDisabled(True)
        self.laba_poga3.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
