from .views import Bags_page
from django.urls import path
from .views import Phones_page
from .views import Animals_page
from .views import Cars_page
from .views import Books_page

urlpatterns = [
    path('', Bags_page, name='bags_page'),
    path('phone/', Phones_page, name='phones_page'),
    path('books/', Books_page, name='book_page'),
    path('animal/', Animals_page, name='animals_page'),
    path('cars/', Cars_page, name='car_page'),
]

# iyeee nima buuuu