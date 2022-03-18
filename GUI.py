import threading


from PyQt5 import QtWidgets, uic

import sys
import presensi
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem

import json


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('presensi.ui', self)

        self.presensi = presensi.presensi()
        self.dataui_NIM = []
        self.dataui_Password = []
        self.show()
        self.loadkeui()
        self.loadkeprogram()

        # self.pushButton_Presensi.clicked.connect(self.presensi_data())
        self.pushButton_Presensi.clicked.connect(lambda: self.thread())

        # print(self.dataui_NIM)
        # print(self.dataui_Password)
        # print(self.presensi_data())

    def loadkeui(self):

        email = self.presensi.email()
        password = self.presensi.password()
        total = len(email)
        print(total)
        self.Tabel_Mahasiswa.setRowCount(total)
        for i in range(total):
            self.Tabel_Mahasiswa.setItem(i, 0, QTableWidgetItem(str(email[i])))
            self.Tabel_Mahasiswa.setItem(i, 1, QTableWidgetItem(str(password[i])))


    def loadkeprogram(self):
        row = self.Tabel_Mahasiswa.rowCount()
        print(row)
        for i in range (row):
            self.dataui_NIM.insert(i, self.Tabel_Mahasiswa.item(i, 0).text())
            self.dataui_Password.insert(i, self.Tabel_Mahasiswa.item(i, 1).text())

    def ambil_link_presensi(self):
        link = self.Text_Edit_Presensi.toPlainText()
        return link

    def presensi_data(self):
        # link uty
        uty = "https://sia.uty.ac.id/"
        uty_absen = "https://sia.uty.ac.id/std/scanabsen"
        absensi_kode = self.ambil_link_presensi()
        uty_keluar = "https://sia.uty.ac.id/home/keluar"
        for i in range(len(self.dataui_NIM)):
            NIM_saat_ini = self.dataui_NIM[i]
            password_saat_ini = self.dataui_Password[i]
            self.presensi.login(uty, "loginNipNim", NIM_saat_ini, "loginPsw", password_saat_ini, "BtnLogin")
            berhasil_login = QListWidgetItem(str("Berhasil login: " + str(NIM_saat_ini)))
            self.listWidget_Progres.addItem(berhasil_login)
            print("login")

            self.presensi.absensi(uty_absen, "inputcode", absensi_kode)
            berhasil_presensi = QListWidgetItem(str("Berhasil presensi: " + str(NIM_saat_ini)))
            self.listWidget_Progres.addItem(berhasil_presensi)
            print("presensi")

            self.presensi.alerta()
            alert_box = QListWidgetItem(str(self.presensi.aa))
            self.listWidget_Progres.addItem(alert_box)
            print("alerta")

            self.presensi.keluar(uty_keluar)
            keluar = QListWidgetItem("Keluar")
            self.listWidget_Progres.addItem(keluar)
            print("keluar")

            w = QListWidgetItem("-----------------")
            self.listWidget_Progres.addItem(w)



    def thread(self):
        t = threading.Thread(name='myThread', target=self.presensi_data())
        t.start()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
