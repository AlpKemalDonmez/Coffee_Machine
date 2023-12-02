menu = {
    "espresso": {
        "icerikler": {
            "su": 50,
            "kahve": 18
        },
        "fiyat": 1.5
    },
    "latte": {
        "icerikler": {
            "su": 200,
            "sut": 150,
            "kahve": 24
        },
        "fiyat": 2.5
    },
    "cappucino": {
        "icerikler": {
            "su": 250,
            "sut": 100,
            "kahve": 24
        },
        "fiyat": 3.0
    }
}
kar = 0
kaynaklar = {
    "su": 500,
    "sut": 300,
    "kahve": 200
}

kasa = 50

def kaynak_kontrol (urun_icerikleri):
    for urun in urun_icerikleri:
        if urun_icerikleri[urun]>kaynaklar[urun]:
            print (f"Uzgunuz, kaynaklarimiz {urun} hazirlamamiz icin yeterli degil..")
            return False
        return True
    
def madeni_para_hesaplama ():
    toplam = int(input("Kac adet 1 TL?: ")) * 1
    toplam += int(input("Kac adet 50 kr?: ")) * 0.5
    toplam += int(input("Kac adet 25 kr?: ")) * 0.25
    toplam += int(input("Kac adet 10 kr?: ")) * 0.10
    return round(toplam,2)

def islem_basari_kontrolu (alinan_para, urun_ucreti):
    print (f"{alinan_para} TL para girisi yaptiniz.")
    if alinan_para >= urun_ucreti:
        para_ustu = round(alinan_para - urun_ucreti,2)
        if alinan_para > urun_ucreti:
            print (f"Buyrun, {para_ustu} TL para ustunuz.")
        global kar
        kar += urun_ucreti
        return True
    else:
        print (f"Uzgunuz, girdiginiz {alinan_para} TL tutari {secim} icin yeterli degil..")
        return False
    
def urun_icerik_raporu (urun, urun_icerikleri):
    for item in urun_icerikleri:
        kaynaklar[item] -= urun_icerikleri[item]
    print (f"{urun} urununuzu alabilirsiniz. Afiyet olsun :)")

while True:
    secim = input ("Hangi urunu secmek istersiniz? (espresso/latte/cappucino): ").lower()
    if secim == "off":
        break
    elif secim == "report":
        for i in kaynaklar:
               print (f"{i}: {kaynaklar[i]} ")
    elif secim == "latte" or secim == "espresso" or secim == "cappucino":
        print ("Ucret: ",menu[secim]["fiyat"])
        icecek = menu[secim]
        if kaynak_kontrol (icecek["icerikler"]):
            odeme = madeni_para_hesaplama ()
            if islem_basari_kontrolu (odeme, icecek["fiyat"]):
                urun_icerik_raporu (secim, icecek["icerikler"])
    else:
        print (f"{secim} maalesef bulunmuyor. Secebileceginiz urunler: espresso/latte/cappucino")

