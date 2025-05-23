while True:
    spl = int(input("Banyak persamaan Linear (2/3): "))
    variabel = int(input("banyaknya variabel dalam persamaan linear (1/2/3): "))
    if spl > variabel:
        print("SPL tidak meiliki solusi")
    elif variabel > spl:
        print("SPL memiliki banyak solusi (tak hingga)")
    else:
        print("SPL memiliki solusi tunggal")
        break
matriks = []
for i in range (spl):
    baris_matriks = []
    print("Koefisien persamaan linear ke", i+1 )
    for k in range (variabel):
        angka = float(input(f'koefisien {k+1} = '))
        baris_matriks.append(angka)
        c = float(input("konstata: "))
        baris_matriks.append(c)
        matriks.append(baris_matriks)
print("Matriks")
for baris_matriks in matriks:
    print(baris_matriks)    

bisa = True
for j in range (variabel):
    if matriks [j][j]== 0:
        print("elemen diagonal pada baris", j+1, "adalah nol, maka pembagian tidak dapat dilakukan")  
        bisa = False
        break
    pembagi = matriks [j][j]
    for k in range (spl+1):
        matriks [i][k] = matriks [i][k]/pembagi
    for l in range (variabel):
        if l != i:
            faktor = matriks[l][i]/ pembagi
            for j in range (spl+1):
                matriks[l][j] = matriks [k][i]-faktor*matriks[i][j]
if bisa:
    print("Matriks setelah eliminasi Gauss: ")  
    for baris in matriks:
        print(baris)
    print("solusi: ")
    for i in range (spl):
        print(f'x{i+1} = {matriks[i][spl]}')
else :
    print("Pembagian tidak dapat dilakukan")













