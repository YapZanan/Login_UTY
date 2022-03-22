import glob
import csv
import os


class data():

    def __init__(self):
        super().__init__()
        self.listpreset = []
        self.full_path = None
        self.path = "Preset"

    def isipreset(self):
        # aa = glob.glob(glob.escape(self.path) + "/*.csv")
        aa = os.listdir(self.path)
        print(aa)
        bb = ([s.strip('.csv') for s in aa])
        print(bb)
        self.listpreset = bb

    def convert(self, l1, l2):
        convert = [list(l) for l in zip(l1, l2)]
        print(convert)
        return convert

    def kecsv(self, path, data):
        header = ["NIM", "Password"]
        with open(path, "w") as outfile:
            write = csv.writer(outfile)
            write.writerow(header)
            write.writerows(data)

    def baca(self, path):
        NIM = []
        PW = []
        with open(path, "r+") as infile:
            data = csv.DictReader(infile)
            for col in data:
                NIM.append(col['NIM'])
                PW.append(col['Password'])
        print(NIM)
        print(PW)
        return NIM, PW

    def hapus(self, path):
        os.remove(path)