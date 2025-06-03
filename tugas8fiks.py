while True:
    print("===================================")
    print("1. Lihat Catatan")
    print("2. Buat catatan baru")
    print("3. Exit")
    print("===================================")
    n = int(input("Masukkan angka 1/2/3: "))
    if n == 2:
        judul = str(input("judul catatan: "))
        isi = str(input("catatan buku: "))
        f = open('buku.txt', 'a')
        f.write(judul + '\n')
        f.write (isi + '\n')
        f.close()
        print("Data sudah disimpan")
    elif n == 1:
        f = open('buku.txt', 'r')
        line = f.readlines()
        f.close()
        data = []
        o = 0
        while o < len(line)-1:
            judul = ""
            isi = ""
            for k in line[o]:
                if k != "\n":
                    judul = judul + k
            for k in line[o+1]:
                if k != "\n":
                    isi = isi +k
            data.append([judul, isi])
            o = o+2
            if len(data) == 0:
                print("data belum ada")
            else:
                print("Judul catatan yang ada: ")
                for j in data:
                    print("-"+j[0])
                pilih = str(input("Masukkan judul yg akan dibaca: "))
                for j in data:
                    if pilih == j[0]:
                        print(j[1])
                        break
                    else:
                        print("Data tidak ada")
    else: 
        f.close()
        print("Data sudah diinput seluruhnya")
        break


    
