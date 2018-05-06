from django.conf.urls import url
from . import views

# All url that system use in this Web Page
app_name = 'save'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),                                    # /mycash/
    url(r'^sign_up/', views.UserCreate.as_view(), name='sign-up'),                          # /mycash/sign_up/    
    url(r'^add/', views.StudentCreate.as_view(), name='add'),                          # /mycash/sign_up/    
]