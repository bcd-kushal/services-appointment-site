
from django.contrib import admin
from django.urls import path

from app import views as app


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', app.homepage, name='homepage'),
    path('date-pick/', app.goto_datepick, name='goto-datepick'),
    path('date-pick/<int:id>/', app.datepick, name='datepick'),
    path('payment/', app.payment, name='payment'),
    path('payment/', app.payment, name='payment'),

    path('payment/', app.process_payment, name='process-payment'),
    
]
