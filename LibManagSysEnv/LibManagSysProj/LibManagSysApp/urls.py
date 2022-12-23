from json.encoder import py_encode_basestring_ascii
from django.urls import include, path
from . import views
urlpatterns =[ 
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
