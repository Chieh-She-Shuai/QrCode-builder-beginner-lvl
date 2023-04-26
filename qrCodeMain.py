##Ilk olarak bilgisayarımızın arabirim terminalinden gerekli python kütüphanelerimizi indiriyoruz
##pip install qrcode
##pip install image (kod çıktımızı resim olarak alabilmemiz için)


##Bu işlemleri bitirdikten sonra kütüphaneleri kodumuza import ediyoruz
import qrcode
#qrkod oluşturmak için kütüphenimizi kodumuza import ediyoruz
import random
#her çıktının isminin farklı olmasını sağlayacak kütüphanemiz
from PIL import Image
#grafik işlemede kullanmak için PIL(Python Imaging Library) ekliyoruz


while True:
#kodumuzun tekrarlanması için bir while döngüsü açıyoruz
    qr = qrcode.QRCode(version=4,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=2)
# version: QR kodunun sürümüdür. QR kodunun boyutunu belirler. Değerler 1-40 arasındadır.
# Değer arttıkça QR kodunun boyutu da artar.
# error_correction: QR kodunun hata düzeltme seviyesini belirler.
# --QR kodunun herhangi bir kısmının kaybolması durumunda bile QR kodunun doğru okunabilmesini sağlar.
# Değerler qrcode.constants.ERROR_CORRECT_L,
# --qrcode.constants.ERROR_CORRECT_M,
# ---qrcode.constants.ERROR_CORRECT_Q ve qrcode.constants.ERROR_CORRECT_H olabilir.
# ----Bu kodda, qrcode.constants.ERROR_CORRECT_L olarak belirlenmiştir, yani en düşük hata düzeltme seviyesi kullanılmıştır.
# box_size: QR kodunun kutu boyutudur. Değer arttıkça QR kodunun boyutu da artar. Bu kodda, box_size=10 olarak belirlenmiştir.
# border: QR kodunun kenar boşluğudur. Değer arttıkça QR kodunun boyutu da artar. Bu kodda, border=2 olarak belirlenmiştir.



    data = input("QR kod oluşturmak istediğiniz linki giriniz: ")

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    random_name = (random.randint(1000, 9999))
    filename = f'image_{random_name}.jpg'

    img.save(filename)

# İlk olarak input() fonksiyonu ile kullanıcıdan bir veri girdisi istedik
# -Bu veri, QR kodu olarak oluşturulmak istenen veridir.
# Daha sonra qr.add_data() metodu kullanarak, oluşturulan QR kod nesnesine bu veriyi ekledik.
# qr.make() metodu ile QR kod nesnesi, veriye göre oluşturulur.
# fit=True parametresi, QR kodunun boyutunu otomatik olarak ayarlamak için kullanılır.
# qr.make_image() metodu, QR kodunun görüntüsünü oluşturur.
# -Bu görüntü, siyah-beyaz bir görüntüdür, beyaz arka plana ve siyah renkli kutulara sahiptir.
# img.save() metodu, oluşturulan QR kodu görüntüsünü kaydeder.
# -filename değişkeni, oluşturulan dosyanın adını tutar.
# --Bu kodda random kütüphanesi kullanılarak, dosya adı rastgele bir sayı ile oluşturulur ve .jpg uzantısı eklenir.
# ---Böylece her seferinde farklı bir isimle kaydedilmesi sağlanır.



    devam = input("Devam etmek istiyor musunuz? (E/H): ")
    if devam.lower() != 'e':
            break

# input("Devam etmek istiyor musunuz? (E/H): ") satırı kullanıcıdan bir girdi alır ve "Devam etmek istiyor musunuz? (E/H):" şeklinde bir mesaj gösterir. Kullanıcı girdi olarak "E" veya "H" harflerinden birini vermelidir.
# devam.lower() != 'e' satırı, kullanıcının verdiği girdinin büyük/küçük harf duyarlılığına bakmaksızın "e" harfi olup olmadığını kontrol eder. Eğer kullanıcının verdiği girdi "e" harfi değilse, break ifadesi programın çalışmasını durdurur ve program sonlanır.
# Bu kod bloğu, programın belirli bir yerinde belirli koşullar altında çalıştırılabilir ve kullanıcının programın devam etmesini isteyip istemediğini kontrol eder. Kullanıcının "H" harfini vermesi halinde, program sonlanır ve daha fazla işlem yapılmaz.