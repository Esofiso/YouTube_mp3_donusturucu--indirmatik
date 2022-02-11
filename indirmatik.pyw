import os

from pyperclip import paste
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube


class Ui_Form_emin_misin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(265, 158)
        Form.setStyleSheet("background: qlineargradient(spread:pad, x1:0.858, y1:0.1535, x2:0.045, y2:1, stop:0.397727 rgba(22, 90, 173, 255), stop:0.721591 rgba(124, 131, 116, 255))")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.sorma_checkBox = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sorma_checkBox.setFont(font)
        self.sorma_checkBox.setObjectName("sorma_checkBox")
        self.sorma_checkBox.setChecked(True)
        self.gridLayout.addWidget(self.sorma_checkBox, 2, 0, 1, 2)
        self.geri_buton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.geri_buton.setFont(font)
        self.geri_buton.setObjectName("geri_buton")
        self.gridLayout.addWidget(self.geri_buton, 3, 0, 1, 1)
        self.indir_buton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.indir_buton.setFont(font)
        self.indir_buton.setObjectName("indir_buton")
        self.gridLayout.addWidget(self.indir_buton, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Emin Misin?"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600;\">indirilsin mi?</span></p></body></html>"))
        self.sorma_checkBox.setText(_translate("Form", "©EA 01/22"))
        self.geri_buton.setText(_translate("Form", "Geri Dön"))
        self.indir_buton.setText(_translate("Form", "İndir"))

    def closeEvent(s, e):
        Form.setEnabled(True)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 183)
        Form.setStyleSheet("background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.318182 rgba(114, 144, 10, 248), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: qradialgradient(spread:pad, cx:0.494, cy:0.505682, radius:0.5, fx:0.5, fy:0.517, stop:0 rgba(255, 188, 188, 0), stop:1 rgba(255, 255, 255, 0))")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setClearButtonEnabled(True)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: qradialgradient(spread:pad, cx:0.494, cy:0.505682, radius:0.5, fx:0.5, fy:0.517, stop:0 rgba(255, 188, 188, 0), stop:1 rgba(255, 255, 255, 0))")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.comboBox.setFont(font)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setEnabled(False)
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:rgb(44, 116, 28)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "İndirmatik"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">İndirmatik - YouTube </span><span style=\" font-weight:600;\"/><span style=\" font-style:italic; color:#484848;\">©EA 01/22</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Yapıştır"))
        self.comboBox_2.setItemText(0, _translate("Form", "Ses"))
        self.comboBox_2.setItemText(1, _translate("Form", "Video"))
        self.comboBox.setItemText(0, _translate("Form", "720 P"))
        self.comboBox.setItemText(1, _translate("Form", "360 P"))
        self.pushButton_2.setText(_translate("Form", "İndir"))

        self.comboBox_2.currentTextChanged.connect(self.degisti)
        self.pushButton.clicked.connect(self.yapistir)
        self.pushButton_2.clicked.connect(self.emin_misin)

    def emin_misin(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.lineEdit.text()) > 24 and self.lineEdit.text().startswith("https://www.youtube.com"):
            self.window = QtWidgets.QWidget()
            self.window.closeEvent = lambda self: Form.setEnabled(True)
            self.yeni_pencere = Ui_Form_emin_misin()
            self.yeni_pencere.setupUi(self.window)
            self.yeni_pencere.indir_buton.clicked.connect(self.indir)
            self.yeni_pencere.geri_buton.clicked.connect(lambda: [self.window.close(), Form.setEnabled(True)])
            self.window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.window.show()
            Form.setEnabled(False)
            baslik = YouTube(self.lineEdit.text()).title
            self.yeni_pencere.label.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600;\">'{baslik}' indirilsin mi?</span></p></body></html>"))

        else:
            self.lineEdit.setText("")
            self.lineEdit.setPlaceholderText("Lütfen Link Yapıştırın!")

      
    def degisti(self):
        if self.comboBox_2.currentText() == 'Ses':
            self.comboBox.setEnabled(False)
        else: 
            self.comboBox.setEnabled(True)

    def yapistir(self):
        self.lineEdit.setText(paste())

    def indir(self):
        Form.setEnabled(True)
        self.window.close()
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setText("İndiriliyor...")
        QtWidgets.qApp.processEvents()
        self.lineEdit.setPlaceholderText("")            
        P = self.comboBox.currentText()
        mp = self.comboBox_2.currentText()
        yol = "."
        link = YouTube(self.lineEdit.text())
        
        if mp == "Ses":
            renamee = link.streams.filter(only_audio=True).first().download(output_path=yol)
            pre, ext = os.path.splitext(renamee)
            new_extension = ".mp3"
            os.rename(renamee, pre + new_extension)

        elif mp == "Video":
            link.streams.filter(type="video", res="720p" if P == "720 P" else "360p").first().download(output_path=yol)

        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setText("İndir")
        self.lineEdit.setText("")        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
