# Tugas Praktikum
# Looping Jika jawab 'y' (ya)
daftar_nilai = [] #berfungsi sebagai integer list

ulangi = True #keadaan looping saat kondisi true

while ulangi : #masukan while do kemudian masukan data yang dibutuhkan seperti contoh berikut

# Masukan Data
- nama = input("Masukan nama: ")
    - nim = input("Masukan NIM: ")
    - tugas = int(input("Masukan nilai Tugas: "))
    - uts = int(input("Masukan nilai UTS: "))
    - uas = int(input("Masukan nilai UAS: "))
    - akhir = (tugas*30/100)+(uts*35/100)+(uas*35/100)
    
    - daftar_nilai.append([nama, int(nim), int(tugas), int(uts), int(uas), int(akhir)],)
    - if (input("tambah data lagi (y/t)?") == 't'):
        - ulangi = False

# Cetak hasil Jika jawaban 't' (tidak)                                                                
- print("\nDaftar Nilai Mahasiswa:")
- print("===================================================================")
- print("| No |      Nama      |    Nim    | Tugas |  UTS  |  UAS  | Akhir |")
- print("===================================================================")
- i=0
- for item in daftar_nilai:
    - i+=1
    - print("| {no:2d} | {nama:14s} | {nim:9d} | {tugas:5.2f} | {uts:5.2f} | {uas:5.2f} | {akhir:5.2f} |"
            - .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
- print("==================================================================")

# Hasilnya
![SharedScreenshot](https://user-images.githubusercontent.com/56239989/69056540-c952fd80-0a42-11ea-949a-4cdd02c0f2ed.jpg)

# Flow Chartnya
![SharedScreenshot](https://user-images.githubusercontent.com/56239989/69056270-28fcd900-0a42-11ea-89c8-fdcb089a38ef.jpg)
