n = int(input("masukkan nilai n : "))
c = 1
d = 3
delta_x = d-c/n
for i in range (n) :
    xi= c+i * delta_x
    luas_daerah= (xi**2 + 2*xi)*delta_x
print("jadi, luas daerah dari fungsi x**2 + 2x dengan batas bawah c=1 dan d=3 dan jumlah partisi", [n], "adalah" , [luas_daerah])#

