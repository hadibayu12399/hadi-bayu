import os
import time

while True:
    try:
      os.system('cls' if os.name == 'nt' else 'clear')
        #NIM: 2009106006 + 10 = 16
      angka = int(input("Masukkan angka: "))
      a = 1
      b = 1
      while b <= angka:
            print (a)
            a += 1
            if a == 10:
                a -= 9
            b += 1
      break
    except ValueError:
        print("salah")
        time.sleep(1)