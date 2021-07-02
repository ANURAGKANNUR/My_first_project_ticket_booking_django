from django.urls import path

from . import views

urlpatterns=[

    path('signin',views.view_login),
    path('signup',views.signup),
    path('findbus/',views.findbus),
    path('bookings/', views.bookings),
    path('seebooking',views.seebooking,name='seebooking'),
    path('cancellation/<int:id>',views.cancellation),
    path('viewticket/<int:id>',views.viewticket),
    path('addbus',views.addbus),
    path('viewbus',views.viewbus),
    path('deletebus/<int:id>',views.deletebus),
    path('updatebus/<int:id>',views.updatebus),
    path('totalbooking',views.totalbooking),
    path('todaybooking',views.todaybooking),
    path('logout_view',views.logout_view),
    path('view_user',views.view_user)

]