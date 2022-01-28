import random rastgeleSayi = random.randint(1,100) tahminSayi=0 while True: sayi=int(input("1 ile 100 arasında bir sayı giriniz")) tahminSayi+=1 if(sayi==0): print("Oyundan çıkış yaptınız") break elif sayi< rastgeleSayi: print("Daha büyük sayı giriniz") continue elif sayi> rastgeleSayi: print("Daha küçük giriniz") continue

else:
    print("Tebrikler Sayıyı Tahmin Ettiniz")
    print("{0} kerde Sayıyı Tahmin  Ettiniz". format(tahminSayi))
