from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name='home'
urlpatterns = [
    url(r'^$',views.login_user, name ='login_user'),
	
    

]
