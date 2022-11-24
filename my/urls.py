from django.urls import path

from my import views

urlpatterns = [
    path('buy/<int:id>', views.BuyItemView.as_view(), name='buy'),
    path('item/<int:id>', views.ItemView.as_view(), name='info'),

]
