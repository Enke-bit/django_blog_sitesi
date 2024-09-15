from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/silme', BlogDeleteView.as_view(), name = 'post_silme'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/yeni/', BlogCreateView.as_view(), name = 'post_yeni'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'), # Bütün post girişleri post ile başlar ve devamındaki int kısım primery keydir.
    path('', BlogListView.as_view(), name='home') # Burda 'as_view' sınıf olduğu için kuulandım. Ve nide ilk başta tırmanğı boş bırakmam home.html haritalar.
    
]

# Burda her post için id eklenir ve bunu id olarak tanımlanır ve işlem yapılmaktedir.
# Bu bir primery key şeklindedir.
# Giriş sayfasında onun url paternin '1' olmaını bekleriz. (ilk ise.)