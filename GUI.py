from threading import *
from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem, QMainWindow, QWidget, QLabel, QDialog
import presensi
import Data
import json


class savedata(QDialog):
    def __init__(self):
        super(savedata, self).__init__()
        uic.loadUi('savedata.ui', self)

        self.pushButton_Cancel.clicked.connect(self.cancel)
    def cancel(self):
        self.close


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('presensi.ui', self)

        self.presensi = presensi.presensi()
        self.data = Data.data()


        self.dataui_NIM = []
        self.dataui_Password = []
        self.saat_ini = []
        self.path = None


        # self.loadkeui()
        self.loadpreset()


        self.pushButton_Presensi.clicked.connect(self.thread_presensi)
        self.pushButton_Tambah.clicked.connect(self.tambahrow)
        self.pushButton_Hapus.clicked.connect(self.hapusrow)

        self.comboBox_Preset.activated[str].connect(self.finds)

        self.save = savedata()
        self.pushButton_Simpan.clicked.connect(self.save.show)
        self.save.pushButton_OK.clicked.connect(self.simpankecsv)


    def simpankecsv(self):

        nama_baru = self.save.textEdit_Nama_File.toPlainText()

        path = "Preset\\"+nama_baru+".csv"
        self.loadkeprogram()
        data = self.data.convert(self.dataui_NIM, self.dataui_Password)
        self.aa = self.data.kecsv(path, data)
        print(path)
        self.save.close()
        self.loadpreset()

    def finds(self):
        self.saat_ini = str(self.comboBox_Preset.currentText())
        print(self.saat_ini)
        if self.saat_ini == "None":
            self.Tabel_Mahasiswa.setRowCount(0)
        else:
            self.path = "Preset\\"+self.saat_ini+".csv"
            print(self.path)
            self.loadkeui()

    def loadpreset(self):
        self.comboBox_Preset.clear()
        self.data.isipreset()
        preset = self.data.listpreset
        print(preset)
        self.comboBox_Preset.addItem("None")
        self.comboBox_Preset.addItems(preset)

    def loadkeui(self):

        email, password = self.data.baca(self.path)
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
window.show()
app.exec_()
