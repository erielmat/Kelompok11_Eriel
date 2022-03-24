# Data Pegawai ICL Supermarket
class pegawai:
    jumlahPegawai = 0

    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
        pegawai.jumlahPegawai += 1

    def totalPegawai(self):
        print("Total pegawai di ICL Supermarket adalah, {pegawai.jumlahPegawai}, orang")

    def dataPegawai(self):
        print("Nama \t\t: ", self.nama)
        print("Jabatan \t: ", self.jabatan)
        print("Gaji \t\t:  Rp", self.gaji)

# List Pegawai
pegawai1 = pegawai("Akmal", "Direktur Keuangan", 25000000)
pegawai2 = pegawai("Faza", "Manager", 12000000)
pegawai3 = pegawai("Eriel", "Supervisor", 7000000)


delattr(pegawai3, 'gaji')
setattr(pegawai3, 'gaji', 8500000)
delattr(pegawai3, 'jabatan')
setattr(pegawai3, 'jabatan', "Head Supervisor")

class magang(pegawai):
    def __init__(self, nama, jabatan, gaji, asal_sekolah):
        super().__init__(nama, jabatan, gaji)
        self.asal_sekolah = asal_sekolah
    
    def dataMagang(self):
        print("Nama \t\t: ", self.nama)
        print("Jabatan \t: ", self.jabatan)
        print("Gaji \t\t:  Rp", self.gaji)
        print("Sekolah \t: ", self.asal_sekolah)

# List Magang
magang1 = magang("Nila", "Associate Manager", 5000000, "SMA 1")
magang2 = magang("Fina", "Junior Analyst", 6000000, "SMA 2")
magang3 = magang("Carla", "Data Engineer", 6500000, "SMA 3")

class parttime(pegawai):
    def __init__(self, nama, jabatan, gaji, harikerja):
        pegawai.__init__(self, nama, jabatan, gaji)
        self.harikerja = harikerja

    def dataPartTime(self):
        print("Nama \t\t: ", self.nama)
        print("Jabatan \t: ", self.jabatan)
        print("Gaji \t\t:  Rp", self.gaji)
        print("Hari Kerja \t: ", self.harikerja)

# List PartTime
partTime1 = parttime("Ariza", "Kasir", 2000000, "Sabtu dan Minggu")
partTime2 = parttime("Diva", "Kasir", 2000000, "Senin dan Rabu")

pegawai1.dataPegawai()
pegawai2.dataPegawai()
pegawai3.dataPegawai()
magang1.dataMagang()
magang2.dataMagang()
magang3.dataMagang()
partTime1.dataPartTime()
partTime2.dataPartTime()
print("Total Pegawai di ICL Supermarket adalah", pegawai.jumlahPegawai, "orang")