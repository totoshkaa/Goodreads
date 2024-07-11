from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:id>/', views.book_detail, name='book_detail'),
    path('<int:id>/comments', views.book_comments, name='comment'),
    path('<int:book_id>/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('<int:comment_id>/edit', views.comment_edit, name='comment_edit'), 
]


