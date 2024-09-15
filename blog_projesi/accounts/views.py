from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm  # Buradaki hata düzeltildi
    success_url = reverse_lazy('login')  # Kayıttan sonra login sayfasına yönlendirme
    template_name = 'signup.html'  # Template dosyanızın adı

# Create your views here.
