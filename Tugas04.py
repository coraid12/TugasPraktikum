# Memasukkan data
n = 0
nama = []
nim = []
tugas = []
uts = []
uas = []
akhir = []
jawab = input("Masukan Data (y/t)?")
mhsw = []


# Looping
while jawab == 'y':
    s_nama = input("Nama :")
    nama.append(s_nama)
    i_nim = int(input("NIM :"))
    nim.append(i_nim)
    i_tugas = int(input("Nilai Tugas :"))
    tugas.append(i_tugas)
    i_uts = int(input("Nilai UTS :"))
    uts.append(i_uts)
    i_uas = int(input("Nilai UAS :"))
    uas.append(i_uas)
    i_akhir = (i_tugas * 30/100) + (i_uts * 35/100) + (i_uas * 35/100)
    akhir.append(i_akhir)
    jawab = input("Tambah data (y/t)?")
    if jawab == 't':
        break
    n += 0
    mhsw.append(nama)
    mhsw.append(nim)
    mhsw.append(tugas)
    mhsw.append(uts)
    mhsw.append(uas)
    mhsw.append(akhir)


# Cetak hasil
print("===============================================================================")
print("No.  |       Nama       |   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |")
print("===============================================================================")
for n in range(0, len(mhsw[n])):
    print('|',n+1,'|       ',nama[n],'      |  ',nim[n],'  |  ',tugas[n],'  |  ',uts[n],'  |  ',uas[n],'  |  ',akhir[n],'  |')
print("===============================================================================")