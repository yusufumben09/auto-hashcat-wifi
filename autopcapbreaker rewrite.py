#geliştirilmiş adlandırma gereksinimi olmayan autopcapbreaker. HASHCAT KULLANIYOR
import os
import time
dir_path = os.path.dirname(os.path.realpath(__file__))#py dosyasının diri alınıp komutlar için chdir ile belirtiliyor.
os.chdir(dir_path) 
pcapfiles = os.listdir('pcaplar') #Kırılacak/gösterilecek hash dosyalarının alındığı klasör

def kirFunc(wordlist,delay): #kırar
    for file in pcapfiles:
        os.system('hashcat.exe -m 22000 pcaplar/' +  file + ' ' + wordlist)
        time.sleep(int(delay))
    print("Kırma işlemi sonlandı.")
    kullaniciistemi()

def gosterFunc(): #gösterir
    for file in pcapfiles:      
        os.system('hashcat.exe -m 22000 pcaplar/' +  file + ' --show')
    print("Bulunan sonuçlar yazdırıldı. Yazdırılmadı ise daha kırılmadı yada kırma başarısız oldu.")
    kullaniciistemi()

#kullanici istemi
def kullaniciistemi():
    kullaniciislemi = input("işlem gir:").lower()
    komut = kullaniciislemi.split()

    if(komut[0] == ("göster" or "gör" or "sonuc" or "gor" or "goster" or "sonuç")):
        gosterFunc()

    elif(komut[0] == ("kır" or "kir" or "başlat" or "baslat" or "başla" or "basla")):
        kirFunc(komut[1],komut[2]) #wordlist dosyasını belirt[1], kırma arası delay'ı beilrt[2]
    
    elif(komut[0] == ("çık" or "cık" or "exit")):
        input("enter tuşuna basarak çık...")

kullaniciistemi() #Başlat
