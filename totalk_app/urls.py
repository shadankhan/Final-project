from django.urls import path
from totalk_app import views


urlpatterns = [
    # path('', views.index, name='index')
    path('create_profile/', views.create_profile,name="create_profile"),
    path('invitation/', views.invitation,name="invitation"),
    path('going_out/', views.going_out_requests, name='going_out_requests'),
    path('inv/<id>', views.inv_detail, name='inv_detail'),
    path('profile/', views.profile, name='profile')
    

]
