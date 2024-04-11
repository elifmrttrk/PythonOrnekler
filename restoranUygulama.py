masalar=dict()
for a in range(20):
    masalar[a]=0
def hesap_ekle():
    masa_no=int(input("Masa numarası: "))
    bakiye=masalar[masa_no]
    eklenecek_ucret=int(input("Eklenecek ücret : "))
    guncel_bakiye=bakiye+eklenecek_ucret
    masalar[masa_no]=guncel_bakiye
    print("İşleminiz tamamlandı.")
def hesap_odeme():
    masa_no = int(input("Masa numarası : "))
    bakiye=masalar[masa_no]
    print("{}. masanın hesap tutarı : {}".format(masa_no,masalar[masa_no]))
    masalar[masa_no]=0
    print("İşleminiz tamamlandı.")
def dosya_kontrolu(dosya_adi):
    try:
        dosya=open(dosya_adi,"r",encoding="utf-8")
        veri=dosya.read()
        veri=veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]]=float(a[1])
    except FileNotFoundError:
        dosya=open(dosya_adi,"w",encoding="utf-8")
        dosya.close()
        print("Kayıt dosyası oluşturuldu.")

def dosya_guncelle(dosya_adi):
    dosya=open(dosya_adi,"w",encoding="utf-8")
    for a in range(20):
        bakiye=masalar[a]
        bakiye=str(bakiye)
        dosya.write(bakiye+"\n")
    dosya.close()

def ana_islemler():
    dosya_kontrolu("restoran.txt")
    while True:
        print("""
        Restaurant Uygulaması
        
        1)Masaları Görüntüle
        2)Hesap ekle
        3)Hesap ödeme
        4)Çıkış
        
        """)
        secim=input("Yapılacak işlemi giriniz : ")
        if secim=="1":
            for a in range(20):
                print("{}.i masa hesap bakiyesi: {}".format(a+1,masalar[a]))
        elif secim=="2":
            hesap_ekle()
        elif secim=="3":
            hesap_odeme()
        elif secim=="4":
            print("Çıkış yapılıyor...")
            quit()
        else:
            print("Yanlış seçim!")
        dosya_guncelle("restoran.txt")
        input("Ana menüye dönmek için enter'a basınız.")
ana_islemler()






