# from . import views
# from django.urls import path

# urlpatterns = [
#     path('about/', views.about_view, name='about')
# ]

# in about/urls.py

# from . import views
# from django.urls import path
# urlpatterns = [
#     path('about/', views.about_view, name='about'),
# ]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]
