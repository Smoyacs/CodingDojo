from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages


from acceso.models import Usuario

from core.models import Book
from core.forms import BookForm



def index(request):
    return redirect(reverse('core:books'))


class BookAdd(View):
    def get(self, request):
        
        print(request.session['usuario']['id'])
        print(request.session['usuario']['first_name'])
        
        like = Book.objects.all().filter(users_who_like__id=request.session['usuario']['id'])
        dislike = Book.objects.all().exclude(users_who_like__id=request.session['usuario']['id'])
        
        books = Book.objects.all()
        context = {
            'formModel': BookForm(),
            'books': books.order_by("-created_at"),
            'like_book': like,
            'dislike_book': dislike,
        }
        return render(request, 'core/index.html', context)

    def post(self, request):
        if BookForm(request.POST):
            form = BookForm(request.POST)
            current_user = Usuario.objects.get(id=request.session['usuario']['id'])
            
            if form.is_valid():
                book_received = form.save(commit=False)
                book_received.uploaded_by = current_user
                book_received.save()
                book_added = Book.objects.filter(title__iexact=request.POST['title'])
                
                for book in book_added:
                    current_book = Book.objects.get(id=book.id)
                    
                    current_user.liked_books.add(current_book)
                    messages.success(request, 'Book Added')
                    return redirect(reverse('core:books'))
            else:
                books = Book.objects.all()
                contexto = {
                    'formModel': form,
                    'books': books.order_by("-created_at"),
                }
                form = BookForm(request.POST)
                messages.error(request, 'El formulario posee errores')
                return render(request, 'core/index.html', contexto)


def bookprofile(request):
    favorite_books = Book.objects.all().filter(users_who_like__id=request.session['usuario']['id'])
    context = {
        'favorite_books': favorite_books
    }
    return render(request, 'core/profile.html', context)

class BookDetail(View):
    def get(self, request, id):
        current_book = Book.objects.get(id=id)
        users_like = Usuario.objects.all().filter(liked_books__id=current_book.id)
        users_dislike = Usuario.objects.all().exclude(liked_books__id=current_book.id)
        
        if request.session['usuario']['id'] == current_book.uploaded_by.id:
            created_at = Book.objects.get(id=id).created_at
            updated_at = Book.objects.get(id=id).updated_at
            form = BookForm(instance=current_book)
            context = {
                'formModel': form,
                'current_book': current_book,
                'created_at': created_at,
                'updated_at': updated_at,
                'users_like': users_like,
                'users_dislike': users_dislike
            }
            return render(request, 'core/detail.html', context)
        else:
            context = {
                'current_book': current_book,
                'users_like': users_like,
                'users_dislike': users_dislike
            }
            return render(request, 'core/detail.html', context)

    def post(self, request, id):

        current_book = Book.objects.get(id=id)
        form = BookForm(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            messages.success(request, 'book edited')
            return redirect(f'/books/{id}')
        else:
            messages.error(request, 'El formulario posee errores.')
            return redirect(f'/books/{id}')


class BookLike(View):
    def get(self, request, id):
        current_user = Usuario.objects.get(id=request.session['usuario']['id'])
        this_book = Book.objects.get(id=id)
        current_user.liked_books.add(this_book)
        messages.success(request, 'book in your favorites')
        return redirect(reverse('core:books'))

    def post(self, request, id):

        current_book = Book.objects.get(id=id)
        current_user = Usuario.objects.get(id=request.session['usuario']['id'])
        current_user.liked_books.add(current_book)
        messages.success(request, 'book added in your favorites')
        return redirect(f'/books/{id}')



def dislike(request, id):
    current_book = Book.objects.get(id=id)
    current_user = Usuario.objects.get(id=request.session['usuario']['id'])
    current_user.liked_books.remove(current_book)
    messages.success(request, 'book removed from your favorites')
    return redirect(f'/books/{id}')



def bookdelete(request, id):
    deletebook = Book.objects.get(id=id)
    deletebook.delete()
    return redirect(reverse('core:books'))



