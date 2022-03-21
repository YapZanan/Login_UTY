from string import digits

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()


class presensi():
   def __init__(self):
      self.aa = None
      self.nama = None
   def login(self, url,usernameId, username, passwordId, password, submit_buttonId):
      driver.get(url)
      mumet = self.captcha(url)
      #depreceated
      # driver.find_element_by_id(usernameId).send_keys(username)
      # driver.find_element_by_id(passwordId).send_keys(password)
      driver.find_element(By.ID, usernameId).send_keys(username)
      driver.find_element(By.ID, passwordId).send_keys(password)
      driver.find_element(By.XPATH, '/ html / body / section / div / div / div / div[1] / div / div[2] / div / div[2] / form / div / input[3]').send_keys(mumet)
      driver.find_element(By.ID, submit_buttonId).click()

   def captcha(self, url):
      driver.get(url)
      soal = driver.find_element(By.XPATH, '/ html / body / section / div / div / div / div[1] / div / div[2] / div / div[2] / form / div / p').text
      # print(soal)
      #fungsi regex
      cari_angka = (re.findall('\d+', soal))
      # print (cari_angka)
      jumlah = self.jumlah_total(cari_angka)
      # print(jumlah)
      return jumlah


   def jumlah_total(self, daftar_nilai):
      z = 0;
      x = daftar_nilai
      jml = len(x)

      for i in range(jml):
         y = int(x[i])
         z += y

      return z

   def ambilnama(self):
      self.nama = driver.find_element(By.XPATH, '/html/body/div[2]/nav/div[2]/div/ul/div/center/p').text
      list = (re.findall(r"\S+", self.nama))
      self.nama = ' '.join(x for x in list if x.isalpha())

   def absensi(self, url, inputcode, absensi):

      driver.get(url)
      driver.find_element(By.ID, inputcode).send_keys(absensi)
      driver.find_element(By.XPATH, '/ html / body / div[2] / div / div[2] / div[2] / center / button').click()


   def alerta(self):
      try:
         WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                         'Timed out waiting for PA creation ' +
                                         'confirmation popup to appear.')

         alert = driver.switch_to.alert
         self.aa = alert.text
         alert.accept()
      except TimeoutException:
         print("no alert")

   def keluar(self, url):
      driver.get(url)

