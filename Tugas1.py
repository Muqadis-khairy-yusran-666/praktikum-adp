#masukkan nama barang beserta harga satuannya
barang = {
    "sabun muka"                        : 50000,
    "gelas kaca"                        : 60000,
    "piring kaca"                       : 65000,
    "handbody"                          : 70000,
    "sabun mandi"                       : 55000,
    "parfum"                            : 100000,
    "minyak rambut"                     : 55000, 
    "minuman dingin 1 dus"              : 60000, 
    "bodylotion"                        : 85000,
    "Baju koko"                         : 100000, 
}

#masukkan nama barang yang akan dibeli dan juga kuantitas yang akan dibeli
print("========================= Daftar Barang =========================")
for i in barang :
    print("Daftar Barang : ", i, "\t Harga : ",barang[i])
print("=================================================================")
beli = input("Pilih Barang : ")
kuantitas = int(input("masukkan jumlah barang yang dibeli : "))

harga = kuantitas * barang[beli]

#buat diskon dan potongan harga
if harga < 1000000 :
    diskon = harga * 0
    print("anda tidak mendapatkn diskon")
    print("harga yang harus dibayarkan", harga-diskon)
elif 1000000<= harga <= 1500000 :
    diskon = harga * 10/100
    print("anda mendapatkan diskon 10%")
    print("harga yang harus dibayarkan", harga-diskon)
elif harga > 1500000 :
    diskon = harga*15/100
    print("anda mendapatkan diskon 15%")
    print("harga yang harus dibayarkan", harga-diskon)

#buat detail pembayaran secara rinci
print("=============== Detai Pembayaran ===============")
print("barang yang dipilih", beli)
print("kuantitas barang", kuantitas)
print("harga satuan", barang[i])
print("harga total", harga)
print("potongan harga", diskon)
print("total harga", harga-diskon)
print("=================================================")






