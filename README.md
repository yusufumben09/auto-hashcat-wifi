# auto-hashcat-wifi
otomatik olarak klasörün içindeki kırılabilir wifi (.22000 ve .16900) dosyalarını sırayla hashcat ile kırmaya çalışır.

kullanmak için .py dosyasını hashcat'ın bulunduğu klasöre atın. aynı yerde bir pcaplar adında klasör oluşturun ve kullanmak istediğiniz wordlist'i atın. Kırılması için .22000 ve .16900 dosyalarınızın hepsini içine atın. Ardından .py dosyasını çaqlıştırın.
Kırmak için cmd'ye "kır (wordlistdosyası.txt) (işlemler arası delay)" şekline komut yazın.
Kırılmış .22000 ve .16900 dosyalarının sonuçlarını görmek için cmd ekranına "gör" yazın.
Çıkmak için ise "çık"

Hashcat gereklidir ve kırma işlemini hashcat yapar, bu program değil. Bu program işlemi otomatik yapar ve kırma işlemi için güçlü bir grafik kardı yada işlemci gerektir.
