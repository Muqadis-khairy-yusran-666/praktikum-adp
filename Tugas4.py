n = int(input("masukkan jumlah pendaftar : "))
for i in range (1, n+1) :
    print("")
    print("Data Pendaftar ke: ", i)
    m = str(input("masukkan nama :"))
    o = str(input("masukkan nama mata kuliah : "))
    while True :
        p = int(input("masukkan nilai wawancara: "))
        if 1 <= p <= 100:
            print(p)
            break 
        else: 
            print("Input ulang nilai anda")
    while True :
        q = int(input("masukkan nilai tes tulis : "))
        if 1 <= q <= 100:
            print(q)
            break 
        else :
            print("input ulang nilai anda")
    while True :
        r = int(input("masukkan nilai mengajar : "))
        if 1 <= r <=100:
            print(r)
            break
        else :
            print("Input ulang nilai anda")
    nilai = (p+q+r)//3
    print("rata rata mahasiswa: ", nilai)
    if 80<= nilai <= 100:
        print("Lulus")
    else :
        print("Tidak Lulus")
