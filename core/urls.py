from django.urls import path
from . import views
from .views import upload_form, list_dogs, save_image, save_image_bill, save_accepted_item

urlpatterns = [
    path("", views.upload_form, name='upload_form'),
    path('save-image/', save_image, name='save_image'),
    path('delete/<int:pk>/', views.delete_image, name='delete-image'),
    path("list/", views.list_dogs, name='list-view'),
    path("bill", views.bill_upload_form, name='bill'),
    path('save-image-bill/', save_image_bill, name='save_image_bill'),
    path("delete1/<int:pk>/", views.delete_image_bill, name='delete-image-bill'),
    path("list_bill", views.list_bills, name='bill-view'),

    path('test/', views.test, name='test'),
    path('approve/', views.approve, name='approve'),
    path('accept/', views.accept, name='accept'),
    path('entries/', views.entries, name='entries'),
]
