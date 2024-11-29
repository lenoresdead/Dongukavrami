# Dongu kavrami
Bir olaya bağlı gerçekleşen ve kendisini tekrar eden yapıya döngü denir.

# 1)For Döngüsü
Çoklu veri elemanlarının yerini alan ve işlem yapmamızı sağlayan döngü çeşididir.

# a) in yapisi
Bir verinin çoklu veride olup olmadığını mantıksal(True/False) olarak kontrol etmemizi sağlar.

örnek:

liste=[1,2,3,4,5]

print(2 in liste)

print(2.5 in liste)

bunların sonucu olarak ilkine True ikinciye False çıktısı alırız, çünkü 2 sayısı listede olan bir veridir ve 2.5 sayısı değildir.

# for için örnek

isim="Selman"

for harf in isim:

  print(harf)

demet=(10,-5,5,7,-9,-8)

for sayi in demet:

  if(sayi<0):

    print(sayi)
  
