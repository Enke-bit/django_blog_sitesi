from django.db import models
from django.urls import reverse               # Djangoda bir obje ile iletişim kumaya yönelik bu işlemi gerçekleştiriyorum.

# Create your models here.
# Blog sayfası için gerekli olan veri yapısının kurulumunu gerçekleştiriyorum.



# Ben burda bu blog sayfası için atılan postların veri yapılarını ayarlıyorum.
class Post (models.Model):
    title = models.CharField(max_length=200)  # Bu başlık için ayarlamasını yaptığım kısım.
    author = models.ForeignKey(               # Burda her post bir kullanıcı tarafından yazılabilir ve her kullanıcı birden fazla post yazabilmesini sağlayan methodu kullandım.
        'auth.User', on_delete=models.CASCADE,# Burda mane_to_day işlemleri için bu fonksyonu kullanmak zorundayız kullanıcı silinidğinde onunla işişkili postlarında silinmesini sağlar.
    )
    body = models.TextField()                 # Burda yazar için bir metin yazma alanı tanımlaması yapıyorum.
    def __str__ (self):                       # Bu method oluşturacağımız nesnenin ismini daha anlaşılır yapaçak.
        return self.title
    def get_absolute_url(self):               # Bu yeni post sonrasında yapılan postun kaydetmeye yönelik çıkan sorun için yapıyorum.
        return reverse("post_detail", kwargs={"pk": self.pk})
