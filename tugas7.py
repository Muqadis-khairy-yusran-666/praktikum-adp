pemakaian = int(input("Jumlah pemakaian (dalam kwh): "))
gol = int(input("Golongan listrik: "))
def golongan (gol):
    print("=====================================================================================")
    print("Golongan 1: Rp 1500/kwh untuk 100 kwh pertama, selanjutnya dikenakan  Rp 2000/kwh")
    print("Golongan 2: Rp 2500/kwh untuk 100 kwh pertama, selanjutnya dikenakan  Rp 3000/kwh")
    print("Golongan 3: Rp 4000/kwh untuk 100 kwh pertama, selanjtnya dikenakan   Rp 5000/kwh")
    print("Golongan 4: Rp 5000/kwh untuk 100 kwh pertama, selanjutnya dikenakan  Rp 7000/kwh")
    print("=====================================================================================")
    if gol == 1:
        print("Golongan listrik anda:", gol)
        if pemakaian > 100:
            kwh = pemakaian-100
            Total_biaya = (1500*100)+(kwh*2000)
            print("Total biaya yang harus dibayar Rp", Total_biaya)
        else:
            biaya = pemakaian*1500
            print("Total yang harus dibayar Rp", biaya)
    elif gol == 2:
        print("Golongan listrik anda:", gol)
        if pemakaian > 100:
            kwh = pemakaian-100
            BIAYA = (2500*100)+(kwh*3000)
            print("Total biaya yang harus dibayar Rp", BIAYA)
        else:
            biaya = pemakaian*2500
            print("Total biaya yang harus dibayar Rp", biaya)
    elif gol == 4:
        print("Golongan listrik anda:", gol)
        if pemakaian > 100:
            kwh = pemakaian-100
            harga = (5000*100)+(kwh*7000)
            print("Total biaya yang harus dibayar Rp", harga)
        else:
            Biaya = pemakaian*5000
            print("Total biaya yang harus dibayar Rp", Biaya)
    else:
        print("Golongan listrik anda: 3")
        if pemakaian >100:
            kwh = pemakaian-100
            Total = (4000*100)+(kwh*5000)
            print("Total biaya yang harus dibayar Rp", Total)
        else :
            Uang = pemakaian*4000
            print("Total biaya yang harus dibayar Rp", Uang)
golongan(gol)