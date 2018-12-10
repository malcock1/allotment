from django.conf.urls import url
import plants
from .views import *

urlpatterns = [
    url(r'^$', index, name='plants_home'),
]