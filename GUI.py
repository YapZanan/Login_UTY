from threading import *
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
        self.pushButton_Presensi.clicked.connect(self.thread_presensi)
        self.pushButton_Tambah.clicked.connect(self.tambahrow)
        self.pushButton_Hapus.clicked.connect(self.hapusrow)

    def loadkeui(self):

        email = self.presensi.email()
        password = self.presensi.password()
        total = len(email)
        print("data masuk ke UI: ", total)
        self.Tabel_Mahasiswa.setRowCount(total)
        for i in range(total):
            self.Tabel_Mahasiswa.setItem(i, 0, QTableWidgetItem(str(email[i])))
            self.Tabel_Mahasiswa.setItem(i, 1, QTableWidgetItem(str(password[i])))

    def loadkeprogram(self):
        row = self.Tabel_Mahasiswa.rowCount()
        print("data masuk ke Program: ", row)
        for i in range(row):
            self.dataui_NIM.insert(i, self.Tabel_Mahasiswa.item(i, 0).text())
            self.dataui_Password.insert(i, self.Tabel_Mahasiswa.item(i, 1).text())

    def ambil_link_presensi(self):
        link = self.Text_Edit_Presensi.toPlainText()
        return link

    def presensi_data(self):
        self.loadkeprogram()
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

            self.presensi.ambilnama()
            nama = QListWidgetItem(str("Nama: " + str(self.presensi.nama)))
            self.listWidget_Progres.addItem(nama)
            print("nama")

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
        selesai = QListWidgetItem("Program Selesai")
        self.listWidget_Progres.addItem(selesai)
        print("selesai")

        self.dataui_NIM.clear()
        self.dataui_Password.clear()


    def thread_presensi(self):
        t1 = Thread(target=self.presensi_data)
        t1.start()

    def tambahrow(self):
        row = self.Tabel_Mahasiswa.rowCount()
        self.Tabel_Mahasiswa.insertRow(row)

    def hapusrow(self):
        indices = self.Tabel_Mahasiswa.selectionModel().selectedRows()
        for each_row in reversed(sorted(indices)):
            self.Tabel_Mahasiswa.removeRow(each_row.row())
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
