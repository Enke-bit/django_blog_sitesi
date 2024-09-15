from django.urls import path
from .views import SignUpView  # Doğru sınıf adıyla import edin

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
