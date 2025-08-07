from django.urls import path, include

from . import views

app_name = 'myapp'

urlpatterns = [
    path('test/', views.test, name='test'),

    path('doctors/', views.DoctorsListView.as_view(), name='DoctorsListView'),
    path('doctors/<int:pk>', views.DoctorsDetailView.as_view(), name='DoctorsDetail'),
    path('doctors/create', views.DoctorsCreateView.as_view(), name='DoctorsCreate'),
    path('doctors/<int:pk>/update', views.DoctorsUpdateView.as_view(), name='DoctorsUpdate'),
    path('doctors/<int:pk>/delete', views.DoctorsDeleteView.as_view(), name='DoctorsDelete'),
    path('health/', views.HealthCheckView.as_view(), name='health_check'),
]