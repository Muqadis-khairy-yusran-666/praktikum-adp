nomor = []
nama = []
belanja = []
while True:
    print("Menu data")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Cetak Data")
    print("4. Keluar")
    pilih_menu = int(input("Pilih Menu: "))
    if pilih_menu == 1:
        nomor_pelanggan = str(input("No Pelanggan: "))
        nomor.append(nomor_pelanggan)
        nama_pelanggan = str(input("Nama Pelanggan: ")) 
        nama.append(nama_pelanggan)
        total_belanja = str(input("Rp "))
        belanja.append(total_belanja)
        print("Data Berhasil Ditambah")
    elif pilih_menu == 2:
        deleted = int(input("Data yang akan dihapus: "))
        nomor.pop(deleted)
        nama.pop(deleted)
        belanja.pop(deleted)
        print("Data Berhasil Dihapus")
    elif pilih_menu == 3:
        print("Data Pelanggan")
        if len(nomor)>0:
            print("No Pelanggan     Nama Pelanggan     Total Belanja")
            for i in range (len(nomor)):
                print(f'{nomor[i]} {nama[i]:>22} {belanja[i]:>22}')
    else:
        break
print("Data Berhasil Dicetak Seluruhnya")