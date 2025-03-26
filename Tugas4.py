n = int(input("masukkan jumlah pendaftar : "))
for i in range (1, n+1) :
    print("")
    print("Data Pendaftar ke: ", i)
    m = str(input("masukkan nama :"))
    o = str(input("masukkan nama mata kuliah : "))
    p = int(input("masukkan nilai wawancara: "))
    q = int(input("masukkan nilai tes tulis : "))
    r = int(input("masukkan nilai mengajar : "))
    nilai = (p+q+r)//3
    print("rata rata mahasiswa: ", nilai)
    if 80<= nilai <= 100:
        print("Lulus")
    else :
        print("Tidak Lulus")
