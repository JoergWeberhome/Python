import sys
from bmi_berechnen import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QTextEdit, QLabel
from PySide2.QtCore import QFile, QObject
import re


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        self.window.pushButton.clicked.connect(self.ok_handler)

        self.window.show()

        self.bmi = 0

    def get_text_field(self):
        height = self.window.txtKg.toPlainText()
        weight = self.window.txtGw.toPlainText()

        return weight, height


    def check_input(self, value):
        #test = r"300"
        print("_______")
        print(value)

        pattern = r"^[0-9]+($|\.[0-9]+$)"

        #test_pattern = r'^[0-9]+($|\.[0-9]+$)'

        match = re.search(pattern, value)
        #match = re.search(r'^[0-9]+(\s|\.[0-9]+\s)', "300")

        print(type(match))
        print(match)

        if match:
            return True
        else:
            return False

    def explanation(self, bmi):
        """
        < 17,5          17,5 - 20           20 - 26         26 - 31             > 31
        Kritisches                                          Leichtes
        Untergewicht    Untergewicht        Normalgewicht   Übergewicht         Übergewicht
        63,2 kg         63,2 - 72,2kg       72,2 - 93,9kg   93,9 - 111,9kg      111,9kg

        """
        kritisches_untergewicht = 17.5
        untergewicht = 20
        normalgewicht = 26
        leichtes_uebergewicht = 31

        if bmi < kritisches_untergewicht:
            return "Du hast kritisches Untergewicht"
        elif bmi < untergewicht:
            return "Du hast Untergewicht"
        elif bmi < normalgewicht:
            return "Du hast Normalgewicht"
        elif bmi < leichtes_uebergewicht:
            return "Du hast leichtes Übergewicht"
        else:
            return "Du fette Sau"


    def ok_handler(self):

        weight, height = self.get_text_field()

        if self.check_input(height) and self.check_input(weight):
            self.bmi = berechne_bmi(float(weight), float(height))
        else:
            print("Hat nicht funktioniert")

        self.window.txtErg.setText(str(self.bmi))

        self.window.lbl_ausgabe.setText(self.explanation(self.bmi))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('form.ui')
    sys.exit(app.exec_())
