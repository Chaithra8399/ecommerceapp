from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.allprodCat, name='allprodCat'),
    path('<slug:c_slug>/', views.allprodCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prod_cat_detail')

]
