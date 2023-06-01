# ATM sistemi projesi:
# Para Çekme, Para Yatırma, Bakiye Öğrenme ve Para Transferi yapan bir ATM programı yazıldı.
# Sisteme giriş için ATM sisteminde olduğu gibi sadece sayılardan oluşan bir şifre ve kullanıcıya hitap etmesi için bir isim sorulur.
# Sisteme giriş şifresi 1453 olarak belirlenmiştir. 
# Sistem try-except blokları kullanılarak yapıldı. Çünkü olası bazı hataları engellemek hedeflendi.
# Gerekli görülen kod bloklarında yapılan yorumlar ile programa açıklık getirilmesi amaçlanmaktadır.
# Yorumlar kendisinden bir sonraki kod bloğu/blokları için yapılmıştır.

while True:
    try:
        sifre = int(input("Kart Şifresi : "))
        if sifre == 1453:
            break
        else:
            print("Hatalı Şifre")
    except ValueError:
        print("Şifre sadece sayılardan oluşur!")


while True:
    try:
        name = input("Adınız: ")
        anapara = int(input("Ana Para Miktarı: "))
        break
    except ValueError:
        print("Sadece sayı giriniz!")



# Kullanıcın sisteme girişinde göreceği mesaj aşağıdaki print() ifadesi içerisine yazılmıştır.
print(
    """
Hoşgeldin {}. 
Hesabınızdaki para miktarı: {} ₺
İşlemler için lütfen bir işlem numarası seç:

1 -- Para Çekme
2 -- Para Yatırma
3 -- Bakiye Öğrenme
4 -- Para Transferi
q -- Çıkış
""".format(name, anapara))


# işlem adında bir değişken tanımlandı ve değişkene kullanıcıdan girilen değer durumuna göre işlemler yapılacaktır.
# İşlemlerin kullanıcı tarafından bitirilmemesi halinde farklı işlemleri yapması için bütün işlem blokları while döngüsüne yazıldı.
while True:
    işlem = input("İşlem Numarası: ")

    if işlem == "1":
        while True:
            print("\n \n----- Para Çekme İşlemi ----- \n")
            try:
                çekilecek_para = int(input("Çekilecek Para Miktarı: "))
                if çekilecek_para > anapara:
                    print("Bakiye Yetersiz. Hesabınızdaki para miktarı: ", anapara)
                    print("Lütfen tekrar deneyiniz!")
                elif çekilecek_para <= anapara:
                    onay_para_çekimi_giriş = input(
                        "Hesabınızdan {} ₺ miktarında para çekilecek. Onaylıyor musunuz? '(E/H)' : )".format(çekilecek_para))
                    
            # Kullanıcıya E/H sorusunda klavyeden e/h girişi sırasında hata ile karşılaşmamak için upper() metodunu kullanıldı.
                    onay_para_çekimi = onay_para_çekimi_giriş.upper()
                    if onay_para_çekimi == "E":
                        anapara -=çekilecek_para
                        print("Hesabınızdan {} miktar para çekildi. Kalan anaparanız: {}".format(çekilecek_para, anapara))
                        break
                    elif onay_para_çekimi == "H":
                        print("İşleminiz gerçekleşmedi.")
                        break
                    else:
                        print("Geçersiz İşlem!")
                        break
                        
            # Kullanıcının sayı dışında başka karakter girmesi halinde olası hataları engellemek için hata mesajı verildi.
            except ValueError:
                print("Lütfen sadece sayı giriniz!")

                
    elif işlem == "2":
        while True:
            print("\n \n----- Para Yatırma İşlemi ----- \n")
            try:
                yatırılacak_para = int(input("Yatırılacak para miktarı: "))
                anapara += yatırılacak_para
                print(
                    "Hesabınıza {} ₺ para yatırıldı. Güncel anaparanız: {}".format(yatırılacak_para, anapara))
                break
            except ValueError:
                print("Sadece sayı giriniz!")

    elif işlem == "3":
        print(
            """
        \n \n----- Bakiye Öğrenme ----- \n
        Merhaba {}. Umarım güzel bir geçiriyorsundur :)
        Hesabınızda daha fazla para olmasını diler ve 
        Hesabınızdaki para miktarının {} ₺ olduğunu söylemekten sevinç duyarım.
        """.format(name, anapara))

    elif işlem == "4":
        while True:
            print("\n \n----- Para Transferi ----- \n")
            try:
                transfer_no = int(input("Transfer edilecek IBAN Numarasını Yazınız: TR"))
                
                # int türündeki bir IBAN numarasının basamak sayısını öğrenmek için str türüne çevirip 
                # len() fonksiyonu kullanıldı.
                if len(str((transfer_no))) == 24:
                    transfer_para = int(input("Gönderilecek Para Miktarı: "))
                    
                    # Anaparanın transfer edilecek paraya eşit veya daha fazla olmasını sağlayan kod bloğu. 
                    if anapara >= transfer_para:
                        transfer_onay_giriş = input(
                            "Hesabınızdan {} IBAN numarasına {} ₺ para transferi yapılacak. Onaylıyor musunuz? (E/H): ".format(
                                transfer_no, transfer_para))
                        
                        # Kullanıcının gireceği E/H değerinin e/h olası durumda bir hata vermemesi için upper() metodu kullanıldı.    
                        transfer_onay = transfer_onay_giriş.upper()
                        
                        if transfer_onay == "E":
                            
                        # Gönderilen para anapara miktarından azaldı.
                            anapara -= transfer_para
                            print(
                                 "İşleminiz başarıyla gerçekleştirildi. İşlem sonu bakiyeniz: {} ₺".format(anapara))
                            break
                        elif transfer_onay == "H":
                            print("İşleminiz iptal edildi.")
                            break
                        else:
                            print("Geçersiz İşlem!")
                            
                    # Anaparanın transfer edilecek paradan az olması durumunda Bakiyenin yetersiz olduğunu gösteren ifade.
                    else:
                        print("Bakiyeniz Yetersiz!")
                        
                #IBAN no'nun eksik olduğu durumda verilecek uyarı.
                else:
                    print("IBAN no 24 basamaklı olmalıdır!")
                    
            except ValueError:
                print("sadece sayı giriniz!")

    elif işlem == "q" and "Q":
        print("\nİşleminniz sonlandı. \nSizi tekrar görmek dileğiyle iyi günler.")
        break
    else:
        print("Geçersiz İşlem!")