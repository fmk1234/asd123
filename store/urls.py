from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.welcome, name="welcome"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('pay/', views.pay, name="pay"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('statikus/', views.statikus, name="statikus"),
	path('dinamikus/', views.dinamikus, name="dinamikus"),
	path('complete/', views.paymentComplete, name="complete"),
	

]