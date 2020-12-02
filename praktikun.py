from prettytable import  prettytable

print("=============================")
print("NAMA : BAGUS TRIARSA")
print("NIM : 312010202")
print("Kelas : TI.20.B.1")
print("Mata Kuliah : Bahasa Pemprrogram")
print("Tugas : Praktikum lab 6 - Pertemuan 10")
print("=============================")

tampunglist = {}
x = prettytable


def tambah():
    print("========= TAMBAH DATA NILAI MAHASISWA ===========")
    tnama = imput("Masukkan Nama Mahasiswa  : ")
    tnim = imput("Masukkan NIM Masahasiswa : ")
    ttugas = int(input("Masukkan Nilai Tugas Mahasiswa : "))
    tuts = int(input("Masukkan Nilai UTS Mahasiswa : "))
    tuas = int(input("Masukkan Nilai UAS Mahasiswa :"))
    takhir = 0.3 * float(ttugas) + 0.35 * float(tuas) + 0.35 *float(tuas)
    tampunglist[tnama] = tnim, ttugas, tuts, tuas, takhir


def tampilkan():
    print("======== LIHAT DATA NILAI MAHASISWA ========")
    no = 0
    x.flield_names = ["NO", "NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"]
    for tdata in tampunglist():
        no +=1
        x.add_row([no, tdata[0], tdata[1][1], tdata[1][2], tdata[1][3], tdata[1][4]])
        print(x)


def hapus(hxsiapa)
    print("======== Hapus Data Nilai Mahasiswa =========")
    if hxsiapa in tampunglist.keys():
        print(f"DATA {hxsiapa} BERHASIL DIHAPUS")
        mhs = int(input(" 1. NIM \n 2. Tugas Nilai \n 3. Nilai UAS\n pilih dengan angka (1/2/3/4) : "))
        if mhs == 1:
            ubahnim = input("Silahkan masukkan NIM yang bener : ")
            1 = 0
            vtug = tampunglist[xsiapa][1]
            vuts = tampunglist[xsiapa][2]
            vuas = tampunglist[xsiapa][3]
            vakh = tampunglist[xsiapa][4]
            tampunglist[xsiapa] = ubahnim, vtug, vuts, vuas, vakh
            x.field_names = ["No", "NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"]
            for tdata in tampunglist.items():
                i += 1
                x.add_row([i,  tdata[0], tdata[1][0], tdata[1][1], tdata[1][2], tdata[1][3], tdata[1][4]])
            print(x)
        elif mhs == 2:
            ubahtugas = int(input("Masukkan Nilai TUGAS Yang Benar"))
            i = 0
            vnim = tampunglist[xsiapa][0]
            vuts = tampunglist[xsiapa][2]
            vuas = tampunglist[xsiapa][3]
            vakh = tampunglist[xsiapa][4]
            tampunglist[xsiapa] = vnim, ubahtugas, vuts, vuas, vakh
            x.field_names = ["No", "NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"]
            for tdata in tampunglist.items():
                1 +=  1
                x.add_row([i, tdata[0], tdata[1][0], tdata[1][1], tdata[1][2], tdata[1][3], tdata[1][4]])
            print(x)
        elif mhs == 3:
            ubahuts = int(input("Masukkan Nilai UTS yang benar : "))
            1 = 0
            vnim = tampunglist[xsiapa][0]
            vtug = tampunglist[xsiapa][1]
            vuas = tampunglist[xsiapa][3]
            vakh = tampunglist[xsiapa][4]
            tampunglist[xsiapa] = vnim, vtug, ubahuts, vuas, vakh
            x.field_names = ["No", "NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"]
            for tdata in tampunglist.items():
                i = 1
                x.add_row([i, tdata[0], tdata[1][0], tdata[1][1], tdata[1][2], tdata[1][3], tdata[1][4]])
            print(x)
        elif mhs == 4:
            ubahuas = int(input("Masukkan Nilai UAS yang benar : "))
            1 = 0
            vnim = tampunglist[xsiapa][0]
            vtug = tampunglist[xsiapa][1]
            vuts = tampunglist[xsiapa][2]
            vakh = tampunglist[xsiapa][4]
            tampunglist[xsiapa] = vnim,  vtug, vuts, ubahuas, vakh
            x.field_names = ["No", "NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"]
            for tdata in tampunglist.items():
                i += 1
                x.add_row([i, tdata[0], tdata[1][0], tdata[1][1], tdata[1][2], tdata[1][3], tdata[1][4]])
            print(x)
        else:
            print("!!! === ERROR! Anda Memasukkan pilihan yang Salah === !!!")
    else:
        print("!!! === ERROR! DATA TIDAK TERSEDIA === !!!")


print("===== APLIKASI PENGOLAHAN DATA NILAI MAHASISWA =====")
while True:
    print("MENU : \n 1. Tanbah Data \n 2. Lihat Data \n 3. Ubah Data \n 4. Hapus Data \n 5. Keluar Aplikasi")
    pilih = int(input("Pilih Menu (1/2/3/4/5) : "))
    if pilih == 1:
        tambah()
    elif pilih == 2:
        tampilkan()
    elif pilih == 3:
        print("======== UBAH DATA NILAI MAHASISWA =========")
        print("data siapa yang akan diubah ?")
        siapa input("Masukkan Nama MAHASISWA yang akan diubah")
        ubah(siapa)
    elif pilih == 4:
        print("======== HAPUS DATA NILAI MAHASISWA ========")
        print("Data siapa yang akan diubah ?")
        hsiapa = input("Masukkan Nama MAHASISWA yang akan diubah : ")
        hapus(hsiapa)
    elif pilih == 5:
        break
    else:
        print("!!! === ERROR! Anda Memasukkan Pilihan yang salah === !!!")









