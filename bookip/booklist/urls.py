from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.conf.urls import url,include


app_name='booklist'
urlpatterns = [
        url(r'^search$',views.search,name='search' ),
        url(r'^recent$',views.recent_books,name='recent' ),
        url(r'^all$',views.list_of_books,name='all' ),
        url(r'^genre$',views.list_genre,name='genre' ),
        url(r'^author$',views.list_author,name='author' ),
        url(r'^rating/$',views.rating_books,name='rating_books' ),
        url(r'^add_books/$',views.add_book.as_view(),name='add_books' ),
        url(r'^(?P<book_id>[0-9]+)/$',views.author_books,name='author_books' ),
        url(r'^(?P<_genre>[A-Za-z ]+)/$',views.genre_books,name='genre_books' ),
        url(r'^logout$',views.logout_user, name ='logout_user'),
        
]
