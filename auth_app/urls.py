from django.urls import path
from auth_app.views import *

#urlpatterns here
urlpatterns = [
    path('sign_up/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('edit_profile/', ProfileEdit, name="edit_profile"),
    path('profile_page/', ProfilePage, name="profile_page"),
]