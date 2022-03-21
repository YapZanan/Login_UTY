# from threading import *
# from PyQt5 import QtWidgets, uic
# import sys
# import presensi
# from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
#
# import json
#
#
# # class Worker(QObject):
# #     finished = pyqtSignal()
# #     progress = pyqtSignal(str)
# #     login = pyqtSignal(str)
# #
# #
# #     def __init__(self):
# #         super(Worker, self).__init__()
# #         self.presensi = presensi.presensi()
# #
# #     def run(self, dataui_NIM, dataui_Password, absensi_kode):
# #         uty = "https://sia.uty.ac.id/"
# #         uty_absen = "https://sia.uty.ac.id/std/scanabsen"
# #         # absensi_kode = self.ambil_link_presensi()
# #         uty_keluar = "https://sia.uty.ac.id/home/keluar"
# #         for i in range(len(dataui_NIM)):
# #
# #             NIM_saat_ini = dataui_NIM[i]
# #             password_saat_ini = dataui_Password[i]
# #             self.presensi.login(uty, "loginNipNim", NIM_saat_ini, "loginPsw", password_saat_ini, "BtnLogin")
# #             login = "Berhasil login: " + NIM_saat_ini
# #             self.login.emit(login)
# #             # berhasil_login = QListWidgetItem(str("Berhasil login: " + str(NIM_saat_ini)))
# #             # self.listWidget_Progres.addItem(berhasil_login)
# #             print("login")
# #
# #             self.presensi.absensi(uty_absen, "inputcode", absensi_kode)
# #             # berhasil_presensi = QListWidgetItem(str("Berhasil presensi: " + str(NIM_saat_ini)))
# #             # self.listWidget_Progres.addItem(berhasil_presensi)
# #             print("presensi")
# #
# #             self.presensi.alerta()
# #             # alert_box = QListWidgetItem(str(self.presensi.aa))
# #             # self.listWidget_Progres.addItem(alert_box)
# #             print("alerta")
# #
# #             self.presensi.keluar(uty_keluar)
# #             # keluar = QListWidgetItem("Keluar")
# #             # self.listWidget_Progres.addItem(keluar)
# #             print("keluar")
# #
# #             # w = QListWidgetItem("-----------------")
# #             # self.listWidget_Progres.addItem(w)
# #             self.progress.emit(login)
# #             # self.login.emit(login)
# #         self.finished.emit()
# #         # self.finished.login()
# #
# #     # def run(self, aa):
# #     #     """Long-running task."""
# #     #     for i in range(5):
# #     #         sleep(1)
# #     #         self.progress.emit("wow")
# #     #     self.finished.emit()
#
#
# class Ui(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(Ui, self).__init__()
#         uic.loadUi('presensi.ui', self)
#
#         self.presensi = presensi.presensi()
#         self.dataui_NIM = []
#         self.dataui_Password = []
#         self.show()
#         self.loadkeui()
#         self.loadkeprogram()
#
#         # self.pushButton_Presensi.clicked.connect(self.presensi_data())
#         self.pushButton_Presensi.clicked.connect(self.thread)
#
#         # print(self.dataui_NIM)WWWWWW
#         # print(self.dataui_Password)
#         # print(self.presensi_data())
#
#     def loadkeui(self):
#
#         email = self.presensi.email()
#         password = self.presensi.password()
#         total = len(email)
#         print(total)
#         self.Tabel_Mahasiswa.setRowCount(total)
#         for i in range(total):
#             self.Tabel_Mahasiswa.setItem(i, 0, QTableWidgetItem(str(email[i])))
#             self.Tabel_Mahasiswa.setItem(i, 1, QTableWidgetItem(str(password[i])))
#
#     def loadkeprogram(self):
#         row = self.Tabel_Mahasiswa.rowCount()
#         print(row)
#         for i in range(row):
#             self.dataui_NIM.insert(i, self.Tabel_Mahasiswa.item(i, 0).text())
#             self.dataui_Password.insert(i, self.Tabel_Mahasiswa.item(i, 1).text())
#
#     def ambil_link_presensi(self):
#         link = self.Text_Edit_Presensi.toPlainText()
#         return link
#
#     def presensi_data(self):
#         # link uty
#         uty = "https://sia.uty.ac.id/"
#         uty_absen = "https://sia.uty.ac.id/std/scanabsen"
#         absensi_kode = self.ambil_link_presensi()
#         uty_keluar = "https://sia.uty.ac.id/home/keluar"
#         for i in range(len(self.dataui_NIM)):
#             NIM_saat_ini = self.dataui_NIM[i]
#             password_saat_ini = self.dataui_Password[i]
#             self.presensi.login(uty, "loginNipNim", NIM_saat_ini, "loginPsw", password_saat_ini, "BtnLogin")
#             berhasil_login = QListWidgetItem(str("Berhasil login: " + str(NIM_saat_ini)))
#             self.listWidget_Progres.addItem(berhasil_login)
#             print("login")
#
#             self.presensi.ambilnama()
#             nama = QListWidgetItem(str("Nama: " + str(self.presensi.nama)))
#             self.listWidget_Progres.addItem(nama)
#             print("nama")
#
#             self.presensi.absensi(uty_absen, "inputcode", absensi_kode)
#             berhasil_presensi = QListWidgetItem(str("Berhasil presensi: " + str(NIM_saat_ini)))
#             self.listWidget_Progres.addItem(berhasil_presensi)
#             print("presensi")
#
#             self.presensi.alerta()
#             alert_box = QListWidgetItem(str(self.presensi.aa))
#             self.listWidget_Progres.addItem(alert_box)
#             print("alerta")
#
#             self.presensi.keluar(uty_keluar)
#             keluar = QListWidgetItem("Keluar")
#             self.listWidget_Progres.addItem(keluar)
#             print("keluar")
#
#             w = QListWidgetItem("-----------------")
#             self.listWidget_Progres.addItem(w)
#
#     def reportProgress(self, n):
#         berhasil_presensi = QListWidgetItem(str(n))
#         self.listWidget_Progres.addItem(berhasil_presensi)
#
#     def thread(self):
#         t1 = Thread(target=self.presensi_data)
#         t1.start()
#
#
#
#     # def runLongTask(self):
#     # threading menggunakan PYQT API, NANTI DILIHAT LAGI, RIBET
#     #     # Step 2: Create a QThread object
#     #     self.thread = QThread()
#     #     # Step 3: Create a worker object
#     #     self.worker = Worker()
#     #     # Step 4: Move worker to the thread
#     #     self.worker.moveToThread(self.thread)
#     #     # Step 5: Connect signals and slots
#     #     aa = 2
#     #     checked = False
#     #     aa = self.ambil_link_presensi()
#     #     self.thread.started.connect(functools.partial(self.worker.run, self.dataui_NIM, self.dataui_Password, aa))
#     #     self.worker.finished.connect(self.thread.quit)
#     #     self.worker.finished.connect(self.worker.deleteLater)
#     #     self.thread.finished.connect(self.thread.deleteLater)
#     #     self.worker.progress.connect(self.reportProgress)
#     #     # Step 6: Start the thread
#     #     self.thread.start()
#
#         # Final resets
#         # self.longRunningBtn.setEnabled(False)
#         # self.thread.finished.connect(
#         #     lambda: self.listWidget_Progres.clear()
#         # )
#
#
# app = QtWidgets.QApplication(sys.argv)
# window = Ui()
# app.exec_()
