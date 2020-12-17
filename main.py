"""
# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from PySide2.QtWidgets import QApplication



class main(QWidget):
    def __init__(self):
        super(main, self).__init__()
        self.load_ui()
         # Find the button with the name "pushButton"
        btn = self.window.findChild(QPushButton, 'pushButton')
         #child = self.window.findChild(QPushButton,'PushButton')
        # child = self.findChild(self.QWidget,"main")
        # self.button = self.findChild(QWidgets.QPushButton, 'PushButton')



    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    widget.show()
    sys.exit(app.exec_())
"""
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

        # self.btn = self.window.findChild(QPushButton, 'pushButton')
        # self.btn.clicked.connect(self.ok_handler)
        self.window.pushButton.clicked.connect(self.ok_handler)

       # self.line = self.window.findChild(QLineEdit, 'lineEdit')
        #lbl_kg = self.window.findChild(QTextEdit,'txtKg').toPlainText()
        #self.kgroesse = float(lbl_kg)/100
        #print(lbl_kg)       # string
       # print(type(lbl_kg))
       # self.ausgabe = int(lbl_kg)
       # print("ausgabe: " + lbl_kg)
        #print(type(self.ausgabe))
       # print("Ausgave: " + str(self.ausgabe))
       # ergEnde = self.ausgabe * 2
       # print(ergEnde)

      #  lbl_gewicht = self.window.findChild(QTextEdit,'txtGw').toPlainText()
      #  print(lbl_gewicht)
      #  self.gewicht = lbl_gewicht  # lbl_gewicht
       # print("GEWICHT")
       # print(self.gewicht)

      #  self.txtErg2 = self.window.findChild(QTextEdit,'txtErg')
      #  self.txtErg2.insertPlainText(str(ergEnde))
        # oder
        # self.txtErg2.setText(str(ergEnde))
        # oder
        # self.txtErg2.setPlainText(str(ergEnde))

        # print(type(txtErg2.setText))

        # self.lbl = self.window.findChild(QLabel, 'label')
        # self.gewicht = self.window.txtGw.text()
        # bmi = 12
        # self.bmi = berechne_bmi(141, self.kgroesse)
        # print(str(self.bmi))


        self.window.show()

    def get_text_field(self):
        height = self.window.txtKg.toPlainText()
        weight = self.window.txtGw.toPlainText()

        return weight, height

    def check_input(self, value):
        #print(type(value))
        #print(value)
        test = "300"
        print(type(test))
        print(test)
        pattern = r'^[0-9]+(\s|\.[0-9]+\s)'
        print(pattern)
        #match = re.search(r'^[0-9]+(\s|\.[0-9]+\s)', "300")

        match = re.search(r"Test", "Das ist ein Test")
        print(type(match))
        print(match)

        if match:
            return True
        else:
            return False


    def ok_handler(self):
        #language = 'None' if not self.line.text() else self.line.text()
        #print('Favorite language: {}'.format(language))
        #self.line.clear()
        #self.line.setText(str(self.ausgabe))
        #self.window.label.setText(self.line.text())
        #print(self.line.text)
        #print('Input-text:' + self.line.text())
       #print(self.lbl_kg.text())
       #self.txtErg2.insertpl (str(ausgabe + ausgabe))
       #self.txtErg2.insertPlainText("jooooooo")         #(str(ergEnde))
       #self.txtErg2.setText("jo")
        #print("Gewicht")
        #print(self.gewicht)

        groesse, gewicht = self.get_text_field()

        # test = self.check_input(groesse)
        # print(test)

       # if self.check_input(groesse) and self.check_input(gewicht):
        self.bmi = berechne_bmi(float(groesse), float(gewicht))
        #else:
        #    print("Hat nicht funktioniert")

        #self.line.setText("jo")
        #self.txtErg2.clear()
        #self.txtErg2.insertPlainText(str(self.bmi))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('form.ui')
    sys.exit(app.exec_())
