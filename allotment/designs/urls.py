from django.urls import path

from . import views

urlpatterns = [
    # /designs/
    path('', views.index, name='designs_index'),
    # /designs/1/
    path('<int:design_id>/', views.detail, name='designs_detail'),
]
