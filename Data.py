import glob




import csv

class data():

    def __init__(self):
        super().__init__()
        self.listpreset = []
        self.full_path = None
        self.path = "Preset"

    def isipreset(self):
        aa = glob.glob(glob.escape(self.path) + "/*.csv")
        bb = ([s.strip('Preset\\') for s in aa])
        self.listpreset = ([s.strip('.csv') for s in bb])

    def convert(self, l1, l2):
        aa = [list(l) for l in zip(l1, l2)]
        print(aa)
        return aa

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