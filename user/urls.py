from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('sign-up/', views.sign_up_view,name='sign-up'),
    path('sign-in/', views.sign_in_view,name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('user/edit/<int:id>/', views.profile_edit, name='profile_edit'),
    path('user/password-edit/<int:id>/', views.change_password, name='password_edit'),
    path('test/', views.test, name='test'),
 
    # path('update/', views.update, name='update'),


]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)