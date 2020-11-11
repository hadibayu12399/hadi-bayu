def tambah(x, y):
   return x + y
def kurang(x, y):
   return x - y
def kali(x, y):
   return x * y
def bagi(x, y):
   return x / y
def pangkat(x, y):
   return x ** y 
def modulus(x, y):
   return x % y 
 
def hitung():
    print('\n\t=============================')
    print('\tProgram Kalkulator Sederhana')
    print('\t===============================')
    print('\t1. Penjumlahan')
    print('\t2. Pengurangan')
    print('\t3. Pembagian')
    print('\t4. Perkalian')
    print('\t5. pemangkatan')
    print('\t6. modulus')
    print('\t===============================')
    print('\tSilahkan pilih 1-6')
    print('')
     
    pilih = input("Masukkan pilihan(1/2/3/4/5/6): ")
    # Meminta input dari user
    angka1 = int(input("Masukkan bilangan pertama: "))
    angka2 = int(input("Masukkan bilangan kedua: "))
    if pilih == '1':
       print(angka1,"+",angka2,"=", tambah(angka1,angka2))
       tanya()
    elif pilih == '2':
       print(angka1,"-",angka2,"=", kurang(angka1,angka2))
       tanya()
    elif pilih == '3':
       print(angka1,"*",angka2,"=", kali(angka1,angka2))
       tanya()
    elif pilih == '4':
       print(angka1,"/",angka2,"=", bagi(angka1,angka2))
       tanya()
    elif pilih == '5':
       print(angka1,"**",angka2,"=", pangkat(angka1,angka2))
       tanya()
    elif pilih == '6':
       print(angka1,"%",angka2,"=", modulus(angka1,angka2))
       tanya()
    else:
       print("Input salah !!")
        
def tanya():
    tanya = input('\n\tKembali ke menu kalkulator (y/t)?')
    if tanya == 'y':
        hitung()
    elif tanya == 't':
        exit
    else:
        print('\n\tsalah input.........!!!')
 
hitung()