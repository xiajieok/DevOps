
from django.conf.urls import url,include
from  Sansa import views
urlpatterns = [
    url(r'report/',views.asset_report),
    #url(r'asset/',include('Sansa.urls')),
]
