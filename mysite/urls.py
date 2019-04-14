from django.contrib import admin
from django.urls import path
from USERs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userlist',views.Uerlist.as_view()),
    path('accountlist',views.Accountlist.as_view()),
    path('topup',views.TopUP.as_view()),
    path('balancetransfer',views.BalanceTransfer.as_view()),

]
