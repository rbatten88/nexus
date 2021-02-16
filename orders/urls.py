from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
	path('add/', views.OrderAddView.as_view(), name='order_add'),
	path('list/', views.OrderListView, name="order_list"),
	path('detail/<int:pk>', views.OrderUpdateView, name="order_detail"),
	path('delete/<int:pk>', views.OrderDeleteView.as_view(), name="order_delete"),
]
