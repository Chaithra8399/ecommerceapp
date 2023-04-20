from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_details, name='cart_details'),
    path('remove/<int:product_id>',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>', views.full_remove, name='full_remove'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)