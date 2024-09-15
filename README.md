# Kişisel Blog Sitesi

Bu proje, Django kullanarak geliştirilmiş kişisel bir blog sitesidir. Blog yazıları, dinamik olarak veritabanından çekilmekte ve kullanıcı dostu bir arayüz ile sunulmaktadır. Proje, sanal ortamda çalıştırılması ve geliştirilmesi için gerekli adımları içermektedir.

## Proje Özeti

Bu proje, kişisel blog yazılarınızı paylaşmanıza olanak tanıyan bir web sitesidir. Django framework'ü kullanılarak oluşturulmuştur ve aşağıdaki özelliklere sahiptir:
- **Anasayfa**
- **Blog yazıları listesi**
- **Blog yazısı detay sayfası**
- **Dinamik içerik yönetimi**

## Özellikler

- **Django ile Güçlendirilmiş**: Güçlü bir Python web framework'ü kullanılarak geliştirilmiştir.
- **Responsive Tasarım**: Mobil uyumlu ve kullanıcı dostu bir tasarıma sahiptir.
- **Dinamik İçerik**: Blog yazıları, veritabanından dinamik olarak çekilmektedir.
- **Kullanıcı Dostu Arayüz**: Bootstrap ve modern web standartları kullanılarak tasarlanmıştır.

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Gereksinimler

- Python 3.x
- Django 4.x
- virtualenv (veya benzeri sanal ortam yöneticisi)

### 2. Sanal Ortam Oluşturma

İlk olarak, projenizi izole bir sanal ortamda çalıştırmak için sanal bir ortam oluşturun ve aktifleştirin:

```bash
# Proje dizinine gidin
cd /path/to/your/project

# Sanal ortam oluşturun
python -m venv venv

# Sanal ortamı aktifleştirin
# Windows için:
venv\Scripts\activate
# macOS/Linux için:
source venv/bin/activate

### 3.  Veritabanı Migrasyonları
Veritabanı tablolarını oluşturmak için aşağıdaki komutları çalıştırın:

python manage.py makemigrations
python manage.py migrate


### 5. Yerel Sunucuyu Başlatma
Projenizi yerel sunucuda çalıştırmak için aşağıdaki komutu kullanın:

python manage.py runserver

- Tarayıcınızda http://127.0.0.1:8000/ adresini ziyaret ederek blog sitenizi görebilirsiniz.

# Proje Yapısı
blog/: Blog uygulaması ile ilgili dosyalar.
models.py: Blog yazıları ile ilgili model tanımlamaları.
views.py: Blog yazıları ve sayfalar için görünümler.
templates/: HTML şablon dosyaları.
static/: CSS, JavaScript ve diğer statik dosyalar.
manage.py: Django yönetim komutlarını çalıştırmak için kullanılan dosya.
requirements.txt: Projede kullanılan Python kütüphaneleri.
# Katkıda Bulunma
Herhangi bir katkı sağlamak isterseniz, lütfen aşağıdaki adımları izleyin:

Bu depoyu çatallayın (fork).
Yeni bir dal (branch) oluşturun.
Değişikliklerinizi yapın.
Pull request oluşturun.
# Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

# İletişim
Proje ile ilgili sorularınız veya geri bildirimleriniz için İbrahim Püsküllü ile iletişime geçebilirsiniz.





























