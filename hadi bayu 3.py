nama = input("Masukan nama pelanggan : ")
tanggal = input("Masukan tanggal pembelian : ")

print("========Toko Kue Sule========")
print("         ==== MENU ====")
print("kue keju             6000")
print("kue coklat           3500")
print("         ==== MENU ====")


kk = int(input(" Jumlah kue keju : "))
harga = 6000
total = kk*harga

if kk >= 4 and kk <= 15: diskon = total * (10/100)
elif kk >= 16 and kk <= 25: diskon = total * (15/100)
elif kk < 4 : diskon = 0
    
hitung = total - diskon

print("Harga Total Sebelum Diskon: Rp. ",total) 
print("Potongan Harga            : Rp. ",diskon)
print("Harga Yang Harus Di Bayar : Rp. ",hitung)

bayar = int(input(" masukan pembayaran: "))
kurang = hitung - bayar
kembalian = bayar - hitung
 
if bayar > hitung:
    print("jumlah kembalian anda adalah : Rp. ",kembalian)   
elif bayar == hitung:
    print("uang anda pas")   
elif bayar < hitung:
    print("uang anda kurang : Rp. ",kurang)
        

kc = int(input(" Jumlah kue coklat : "))
harga = 3500
total = kc*harga

if kc >= 5 and kc <= 20: diskon = total * (7/100)
elif kc >= 21 and kc <= 35: diskon = total * (12/100)
elif kc < 5 : diskon = 0
    
hitung = total - diskon

print("Harga Total Sebelum Diskon: Rp. ",total)
print("Potongan Harga            : Rp. ",diskon)
print("Harga Yang Harus Di Bayar : Rp. ",hitung)

bayar = int(input(" masukan pembayaran: "))
kurang = hitung - bayar
kembalian = bayar - hitung
 
if bayar > hitung:
    print("jumlah kembalian anda adalah : Rp. ",kembalian)   
elif bayar == hitung:
    print("uang anda pas")   
elif bayar < hitung:
    print("uang anda kurang : Rp. ",kurang)
print(" ")
print("terima kasih sudah membeli")
        


        
        

