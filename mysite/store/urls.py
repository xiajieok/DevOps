from django.conf.urls import url
from store import views
urlpatterns = [
    url(r'^$', views.login),
    # url(r'^db_handle/$',views.db_handle),
    url(r'^check/', views.check),
    url(r'^reg/', views.reg),
    url(r'^home/', views.home),
    url(r'^books/', views.books),
    url(r'^book_edit/', views.book_edit),
    url(r'^book_del/', views.book_del),
    url(r'^authors/', views.authors),
    url(r'^publishers/', views.publishers),
    url(r'^publisher_edit/', views.publisher_edit),
    url(r'^publisher_del/', views.publisher_del),
    url(r'^author_edit/', views.author_edit),
    url(r'^author_del/', views.author_del),


]
