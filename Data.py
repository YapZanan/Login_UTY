import os.path
import json

datasaatini = [["5191011008", "5191011024", "5191011029", "5191011036", "5191011038"],
        ["Mayaltn417#", "220222", "032001", "asdqwe123@@A", "032001"]]
# password =

print(datasaatini[0][1])
print(datasaatini[1][1])
path = "Preset"
nama_file = "a.json"
full_path = path+ "/" +nama_file
cek_file = os.path.exists(full_path)
print(full_path)

class data():

    def __init__(self):
        super().__init__()

    def datatojson (self):
        if cek_file == False:
            # data = {'mahasiswa': [{'NIM': data1[0][0], 'Password': data1[1][0]}]}
            self.file(datasaatini)
        else:
            self.file_tidak_ada(self.tambah_data(datasaatini))

    def file_tidak_ada(self, data):
        with open(full_path, 'w') as outfile:
            for i in range(len(data)):
                data = {'mahasiswa': [{'NIM': data[0][i], 'Password': data[1][i]}]}
                json.dump(data, outfile, indent=3)

    def tambah_data(self, data_baru):
        with open(full_path, 'r+') as read:
            bacadata = json.load(read)
            # databaru = {'NIM': data1[0][0], 'Password': data1[1][0]}
            bacadata["mahasiswa"].append(data_baru)
            print(bacadata)
            return bacadata

aa = data()
aa.datatojson()

