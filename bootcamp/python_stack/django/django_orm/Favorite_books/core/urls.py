from django.urls import path

from .views import index, BookAdd, bookprofile, BookDetail, BookLike, dislike, bookdelete

app_name = "core"

urlpatterns = [
    path('', index, name="index"),
    path('books', BookAdd.as_view(), name="books"),
    path('books/profile', bookprofile, name="profile"),
    path('books/<int:id>', BookDetail.as_view(), name="detail"),
    path('books/<int:id>/like', BookLike.as_view(), name="like"),
    path('books/<int:id>/dislike', dislike, name="dislike"),
    path('books/<int:id>/destroy', bookdelete, name="destroy"),
]